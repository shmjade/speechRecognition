#import transcribe_audio
from split_audio import split_audio
from transcribe_audio import transcribe_audio

from pydub import AudioSegment
import math
ONE_MINUTE = 1 * 60 * 1000
file_path = "audio-files/test1.mp3"
# split_audio(file_path)
audio_file = AudioSegment.from_mp3(file_path)
num_chunks = math.ceil(len(audio_file)/ONE_MINUTE)

for i in range(1, num_chunks+1):
    transcribe_audio("temp_audios/chunk_"+str(i)+".mp3")
    # print(i)