import os
os.environ["COQUI_TOS_AGREED"] = "1"  # MUST be before TTS import

from TTS.api import TTS
import gradio as gr

# Load model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# Define speaker reference folder
SPEAKER_DIR = "voices/atishay"
SPEAKER_WAVS = [os.path.join(SPEAKER_DIR, f) for f in os.listdir(SPEAKER_DIR) if f.endswith(".wav")]

def clone_and_speak(text, language, speaker_index):
    if not text.strip():
        return "Please enter text.", None

    speaker_wav = SPEAKER_WAVS[speaker_index]
    output_path = "output.wav"

    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        language=language,
        file_path=output_path
    )

    return f"Generated in: {language}", output_path

demo = gr.Interface(
    fn=clone_and_speak,
    inputs=[
        gr.Textbox(label="Text to Synthesize"),
        gr.Dropdown(choices=["en", "hi", "es"], value="en", label="Language"),
        gr.Slider(0, len(SPEAKER_WAVS)-1, step=1, value=0, label="Speaker Sample Index")
    ],
    outputs=[
        gr.Text(label="Status"),
        gr.Audio(type="filepath", label="Generated Audio")
    ],
    title="Multilingual Voice Cloning with Coqui XTTS",
    description="Uses XTTS v2 and your voice samples to synthesize speech in multiple languages."
)

if __name__ == "__main__":
    demo.launch()