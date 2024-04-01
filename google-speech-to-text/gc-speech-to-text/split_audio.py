import math
from pydub import AudioSegment

def split_audio_get_num_chunks(file_path):
    audio_file = AudioSegment.from_mp3(file_path)
    ONE_MINUTE = 1 * 60 * 1000

    # Calculate the number of chunks needed
    num_chunks = math.ceil(len(audio_file)/ONE_MINUTE)

    # Extract 1-minute segments
    audio_chunks = []
    for i in range(num_chunks):
        start_time = i * ONE_MINUTE
        end_time = min((i + 1) * ONE_MINUTE, len(audio_file))
        audio_chunks.append(audio_file[start_time:end_time])

    # Export each chunk as a separate file
    for i, chunk in enumerate(audio_chunks):
        chunk.export(f"temp_audios/chunk_{i+1}.mp3", format="mp3")

    return num_chunks
