from transcribe_audio import transcribe_audio
from split_audio import split_audio_get_num_chunks
from pydub import AudioSegment
import math
import time

ONE_MINUTE = 1 * 60 * 1000
file_path = "audio-files/civil.mp3"
# margin_audio = 3 * 1000     # 3 seconds of margin when splitting

num_chunks = split_audio_get_num_chunks(file_path=file_path)

start_time = time.time()  # Record the start time
transcription = ""
for i in range(1, num_chunks+1):
    transcription += transcribe_audio("temp_audios/chunk_"+str(i)+".mp3")
end_time = time.time()  # Record the end time

print("Total transcription time:", end_time-start_time, "seconds")
print("Transcription:", transcription)