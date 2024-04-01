import io
from google.oauth2 import service_account
from google.cloud import speech

path_dir = "google-speech-to-text/gc-speech-to-text/"

def transcribe_audio(file_path):
    # configure credentials
    api_key_file = path_dir+'speechrecognition-key.json'
    credentials = service_account.Credentials.from_service_account_file(api_key_file)
    client = speech.SpeechClient(credentials=credentials)

    # get audio content
    with io.open(file_path, 'rb') as f:
        content = f.read()
        audio = speech.RecognitionAudio(content=content)

    # configure according to: https://cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig
    config = speech.RecognitionConfig(
        encoding = speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz = 44100,
        language_code = 'fr-FR',
        enable_automatic_punctuation = True 
    )

    # transcribe audio file
    response = client.recognize(config=config, audio=audio)
    
    return response.results[0].alternatives[0].transcript