from pydub import AudioSegment
import os

# file naming
src = "katie.mp3"
dst = "katie.wav"

# convert mp3 to wav
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
print('Audio content written to file ' + dst)
os.remove(src)
print('Deleted' + src)

#add silence at beginning and end of wav file (necessary for sphinx analysis)
#read wav file to an audio segment
initial_audio = AudioSegment.from_wav(dst)
# create 1 sec of silence audio segment
one_sec_segment = AudioSegment.silent(duration=1000)  #duration in milliseconds
#Add above two audio segments
final_audio = one_sec_segment + initial_audio + one_sec_segment
#Either save modified audio
final_audio.export(dst, format="wav")
