import os
import tempfile
import shutil
import gradio as gr
from TTS.api import TTS

# Load Coqui XTTS model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

def clone_and_speak(text, language, files):
    # Check inputs
    if not text or not files:
        return "Error: Please upload at least one voice sample and provide input text.", None

    # Create a temp directory to store uploaded wavs
    with tempfile.TemporaryDirectory() as temp_dir:
        for i, file in enumerate(files):
            shutil.copy(file.name, os.path.join(temp_dir, f"sample_{i}.wav"))

        try:
            output_path = os.path.join(temp_dir, "output.wav")
            tts.tts_to_file(
                text=text,
                speaker_wav=os.path.join(temp_dir, "sample_0.wav"),
                language=language,
                file_path=output_path,
            )
            return "✅ Voice cloned successfully!", output_path
        except Exception as e:
            return f"❌ Error during synthesis: {str(e)}", None

# Gradio UI
iface = gr.Interface(
    fn=clone_and_speak,
    inputs=[
        gr.Textbox(label="Text to Speak", placeholder="Type something...", lines=2),
        gr.Textbox(label="Language Code", placeholder="e.g., en, hi, es", value="en"),
        gr.File(label="Upload 1 or more voice samples (.wav)", file_types=[".wav"], file_count="multiple")
    ],
    outputs=[
        gr.Textbox(label="Status"),
        gr.Audio(label="Generated Voice", type="filepath")
    ],
    title="Multilingual Voice Cloning with XTTS",
    description="Upload your voice samples, enter text and language code to generate cloned speech using Coqui XTTS v2.",
)

if __name__ == "__main__":
    iface.launch()