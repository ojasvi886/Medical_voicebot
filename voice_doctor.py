# Text to Speech using gTTS
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    audio = AudioSegment.from_mp3("final.mp3")
    audio.export("final.wav", format="wav")
    print("Playing the audio file")
    play(AudioSegment.from_wav("final.wav"))
    





