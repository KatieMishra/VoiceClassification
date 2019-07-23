"""Katie Mishra | July 2019 | krmishra@stanford.edu
Extracts phonemes from wav files and writes time to say each phoneme and audio score into a JSON dictionary file. """

from pocketsphinx import Pocketsphinx
import os
import subprocess
from os import system
import string
import json
from nltk.tokenize import sent_tokenize, word_tokenize
import wave
import struct
import numpy as np
from scipy.io.wavfile import read

modulePath = '/Users/katiemishra/Desktop/VoiceClassification/AudioLibraries' # change as appropriate
import sys
sys.path.append(modulePath)
# now you're good to import the modules
import generalUtility
import dspUtil
import matplotlibUtil

# codes for voices to generate
voice_names = ['en-US-Standard-B','en-US-Standard-C','en-US-Standard-D','en-US-Standard-E','en-US-Wavenet-A','en-US-Wavenet-B','en-US-Wavenet-C','en-US-Wavenet-D','en-US-Wavenet-E','en-US-Wavenet-F']

#words to generate samples for
words = ["odd","at","hut","ought","cow","hide","be","cheese","thee","Ed","hurt","ate","fee","green","he","it","eat","gee","key","lee","me","knee","ping","oat",
  "toy","pee","read","sea","she","tea","theta","hood","two","vee","we","yield","zee","seizure"]

for chosen_voice in voice_names:
    cmd = "pocketsphinx_continuous -infile Samples/" + chosen_voice +  ".wav -jsgf wordFiles/with-align.jsgf -dict wordFiles/phonemes.dict -backtrace yes -fsgusefiller no -bestpath no 2>&1 > wordFiles/with-alignment.txt"
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]

    # create temporary file to store terminal output
    filename = "Samples/output.txt"
    f = open(filename, "a")
    f.write(output)

    # read through file and store phoneme-important lines in an array
    linesToSave = []
    file = open(filename,'r')
    lines = file.readlines()
    last_lines = lines[-20:]
    reached_start = False
    for line in last_lines:
        if (line.startswith("INFO:	sil") == True):
            reached_start = True
        if (reached_start and line.startswith("INFO:	sil") == False and line.startswith("INFO:	(NULL)") == False):
            linesToSave.append(line)
    file.close()

    # find min and max frequency
    data_size = 4000
    frate = 11025.0
    wav_file = wave.open("Samples/with/with-" + chosen_voice + ".wav", 'r')
    data = wav_file.readframes(data_size)
    wav_file.close()
    data = struct.unpack('{n}h'.format(n=data_size), data)
    data = np.array(data)

    w = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(w))
    min_freq = freqs.min()
    max_freq = freqs.max()

    # Find the peak in the coefficients (aka sampling frequency)
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * frate)

    # convert wav file to numpy array
    a = read("Samples/with/with-" + chosen_voice + ".wav")
    arrFromWav = np.array(a[1],dtype=float)
    """for test in arrFromWav:
        if(test != 0.0):
            print test
            print np.where(arrFromWav == test)"""

    # find fundamental frequency
    print dspUtil.calculateF0(arrFromWav, freq_in_hertz, min_freq, max_freq, 0.3, False)

    # tokenize phoneme analysis lines to save duration and acsr score in a new json file
    json_file = "possible_voices/chosen_voice" + ".json"
    with open(json_file, 'w') as outfile:
        word_analysis = {}
        for line in linesToSave:
            tokens = word_tokenize(line)
            duration = int(tokens[4]) - int(tokens[3])
            acsr = int(tokens[6])
            data = {}
            data["duration"] = duration
            data["acsr"] = acsr
            phoneme = tokens[2]
            phoneme_analysis = {phoneme : data}
            word_analysis.update(phoneme_analysis)
        word_analysis.update({"freq":freq_in_hertz})
        json.dump(word_analysis, outfile)
