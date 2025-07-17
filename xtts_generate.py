# xtts_generate.py
from TTS.api import TTS

def xtts_generate(text, speaker_wav):
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        language="en",
        file_path="output.wav"
    )
    return "output.wav"