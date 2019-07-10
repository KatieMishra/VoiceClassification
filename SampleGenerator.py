"""Katie Mishra | July 2019 | katiemishra@gmail.com
Synthesizes speech from the input string of text or ssml.
Exports in both mp3 and wav format. Requires Google API credential in bash profile. """
from google.cloud import texttospeech
from os import path
from pydub import AudioSegment

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(text="with")

# codes for voices to generate
voice_names = ['en-US-Standard-B','en-US-Standard-C','en-US-Standard-D','en-US-Standard-E','en-US-Wavenet-A','en-US-Wavenet-B','en-US-Wavenet-C','en-US-Wavenet-D','en-US-Wavenet-E','en-US-Wavenet-F']

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
    dst = "Samples/" + voice_name + ".wav"

    # convert mp3 to wav
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    print('Audio content written to file ' + dst)
