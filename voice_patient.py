import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

#1. record voice 
def record_audio(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking... (Press Ctrl+C to stop)")

            while True:
                try:
                    # Record audio continuously
                    audio_data = recognizer.listen(source)
                    
                    # Convert and save audio
                    wav_data = audio_data.get_wav_data()
                    audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
                    audio_segment.export(file_path, format="mp3", bitrate="128k")

                    logging.info("Audio saved to %s. Keep speaking or press Ctrl+C to stop.", file_path)

                except Exception as e:
                    logging.error("Error recording audio: %s", e)

    except KeyboardInterrupt:
        logging.info("\nRecording stopped by user (Ctrl+C). Exiting...")
    except Exception as e:
        logging.error("Unexpected error: %s", e)

#2. voice to text 
from groq import Groq
def transcribe_with_groq(audiofile,stt_model,groq_api):  
    client=Groq(api_key=groq_api)
    audio_file=open(audiofile, "rb")
    transciption=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )
    return transciption.text


