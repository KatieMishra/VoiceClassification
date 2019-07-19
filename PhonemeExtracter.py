"""Katie Mishra | July 2019 | katiemishra@gmail.com
Extracts phonemes from wav files and writes time to say each phoneme and audio score into a JSON dictionary file. """

from pocketsphinx import Pocketsphinx
import os
import tempfile
import subprocess
from subprocess import call
from os import system

# codes for voices to generate
voice_names = ['en-US-Standard-B','en-US-Standard-C','en-US-Standard-D','en-US-Standard-E','en-US-Wavenet-A','en-US-Wavenet-B','en-US-Wavenet-C','en-US-Wavenet-D','en-US-Wavenet-E','en-US-Wavenet-F']

#words to generate samples for
words = ["odd","at","hut","ought","cow","hide","be","cheese","thee","Ed","hurt","ate","fee","green","he","it","eat","gee","key","lee","me","knee","ping","oat",
  "toy","pee","read","sea","she","tea","theta","hood","two","vee","we","yield","zee","seizure"]

#command to execute
cmd = "pocketsphinx_continuous -infile Samples/en-US-Standard-B.wav  -jsgf with-align.jsgf -dict phonemes.dict -backtrace yes -fsgusefiller no -bestpath no 2>&1 > with-alignment.txt"
call(cmd)

#store output from executing terminal command
"""with tempfile.TemporaryFile() as tempf:
    proc = subprocess.Popen(cmd, stdout=tempf)
    proc.wait()
    tempf.seek(0)
    print tempf.read()"""
