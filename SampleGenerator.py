"""Katie Mishra | July 2019 | katiemishra@gmail.com
Synthesizes speech from the input string of text or ssml.
Exports in wav format, adding one second of silence on each side of clipself.
Requires Google API credential in bash profile. """
from google.cloud import texttospeech
from os import path
from pydub import AudioSegment
import os
from subprocess import call

# Instantiates a client
client = texttospeech.TextToSpeechClient()

#words to generate samples for
words = ["odd","at","hut","ought","cow","hide","be","cheese","thee","Ed","hurt","ate","fee","green","he","it","eat","gee","key","lee","me","knee","ping","oat",
  "toy","pee","read","sea","she","tea","theta","hood","two","vee","we","yield","zee","seizure"]

# create 1 sec of silence audio segment
one_sec_segment = AudioSegment.silent(duration=1000)  #duration in milliseconds

# codes for voices to generate
voice_names = ['en-US-Standard-B','en-US-Standard-C','en-US-Standard-D','en-US-Standard-E','en-US-Wavenet-A','en-US-Wavenet-B','en-US-Wavenet-C','en-US-Wavenet-D','en-US-Wavenet-E','en-US-Wavenet-F']

call("cd ./Samples")

for word in words:

    #create folder and navigate to correct directory
    call("mkdir " + word)
    call("cd " + word)

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=word)

    for voice_name in voice_names:
        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.types.VoiceSelectionParams(
                language_code='en-US',
                name=voice_name)

        # Select the type of audio file you want returned
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        #specify file name based on voice used
        file_type = ".mp3"
        file_name = voice_name + file_type

        # The response's audio_content is binary.
        with open(file_name, 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file ' + file_name)

        # file naming
        src = file_name
        dst = voice_name + ".wav"

        # convert mp3 to wav
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")
        print('Audio content written to file ' + dst)
        os.remove(src)
        print('Deleted' + src)

        #add silence at beginning and end of wav file (necessary for sphinx analysis)
        #read wav file to an audio segment
        initial_audio = AudioSegment.from_wav(dst)
        #Add above two audio segments
        final_audio = one_sec_segment + initial_audio + one_sec_segment
        #Either save modified audio
        final_audio.export(dst, format="wav")

        call("cd ..")
