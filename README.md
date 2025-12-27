# XTTS Multilingual Voice Cloning 🎙️

This project is a web-based **multilingual voice cloning app** powered by [Coqui XTTS v2](https://coqui.ai/), hosted on **Hugging Face Spaces** and built using **Gradio**.

🔗 **Live Demo**: [xtts-atishay-voice-clone on Hugging Face](https://huggingface.co/spaces/atishay04/xtts-atishay-voice-clone)

##  Features

-  **Speaker cloning** using your own voice samples (`.wav`)
- 🌐 **Multilingual text-to-speech** (supports English, Hindi, Spanish, etc.)
-  Dynamic voice sample selection
-  Clean UI built with Gradio
-  Python backend powered by Coqui TTS

---

## 📁 Project Structure

xtts-atishay-voice-clone/
├── app.py # Gradio UI + inference script
├── requirements.txt # All required dependencies
├── speaker/ # Folder with your .wav voice samples
├── .gitattributes # Enables Git LFS
└── .gitignore # Python & system ignores


## 🔧 Setup Instructions (Local)

1. Clone the repo:
   ```bash
   git clone https://github.com/atishay04/xtts-atishay-voice-clone.git
   cd xtts-atishay-voice-clone
(Optional) Create a virtual environment:

(optional)
python -m venv venv
venv\Scripts\activate   # Windows
Install requirements:

pip install -r requirements.txt
Run the app:

python app.py


📄 License
Licensed under the Non-Commercial CPML by Coqui — details here.
For commercial use, contact Coqui.

 Author: Atishay Jain
📧 LinkedIn: www.linkedin.com/in/atishay-jain-0465aj
 CSE student 
 Voice samples & model integration by me!


##  `.gitignore` (Python Template)

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
.env

# VSCode and system files
.vscode/
.DS_Store
Thumbs.db

# Hugging Face specific
*.safetensors
*.bin

🪪 LICENSE
Since you’re using Coqui XTTS, it’s NOT fully open-source for commercial use.
The model is under CPML (Coqui Public Model License).

You should include this license notice:

txt
Copy code
Coqui XTTS is licensed under the Coqui Public Model License (CPML).
By using this project, you agree to the terms: https://coqui.ai/cpml

For commercial usage, a commercial license must be purchased from:
licensing@coqui.ai
