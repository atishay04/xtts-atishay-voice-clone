import os
os.environ["COQUI_TOS_AGREED"] = "1"  # Auto-agree to Coqui's CPML license

from TTS.api import TTS
import gradio as gr

# Load the multilingual XTTS model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# Define speaker reference directory and list
SPEAKER_DIR = "voices/atishay"
SPEAKER_WAVS = [os.path.join(SPEAKER_DIR, fname) for fname in os.listdir(SPEAKER_DIR) if fname.endswith(".wav")]

def clone_and_speak(text, language, speaker_index):
    if not text.strip():
        return "Please enter text.", None

    speaker_wavs = SPEAKER_WAVS[speaker_index]
    output_path = "output.wav"

    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wavs,
        language=language,
        file_path=output_path
    )
    return f"Language: {language}", output_path

# Gradio UI components
demo = gr.Interface(
    fn=clone_and_speak,
    inputs=[
        gr.Textbox(label="Enter text to synthesize"),
        gr.Dropdown(choices=["en", "hi", "es"], value="en", label="Language"),
        gr.Slider(0, len(SPEAKER_WAVS)-1, step=1, value=0, label="Speaker Sample"),
    ],
    outputs=[
        gr.Text(label="Status"),
        gr.Audio(type="filepath", label="Cloned Voice Output"),
    ],
    title="Multilingual Voice Cloning with Coqui XTTS",
    description="Upload your own voice samples in the `voices/atishay/` folder and synthesize speech in multiple languages."
)

if __name__ == "__main__":
    demo.launch()