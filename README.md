# NeuroTutor - Your AI-Powered Personal Teacher 🧠📖🎙️

NeuroTutor is an AI-driven personal tutor that enhances learning by leveraging the **Feynman technique**. It allows you to **upload class notes (PDFs), converse via microphone, and receive AI-powered explanations** that reference your materials and online sources.

## Features
✅ **Upload & Extract Notes** – Store class notes (PDFs) and retrieve relevant information.  
✅ **Voice Interaction** – Speak to your AI tutor using real-time speech-to-text.  
✅ **Feynman-Based Learning** – AI simplifies concepts by encouraging you to "teach" them.  
✅ **Context-Aware Answers** – AI references both your notes and online sources.  
✅ **Seamless Integration** – FastAPI backend with OpenAI GPT and Whisper for a smooth experience.  

## Tech Stack
- **Backend**: FastAPI
- **AI Models**: OpenAI GPT, Whisper (Speech-to-Text)
- **Data Processing**: FAISS (Vector Search), PyMuPDF (PDF Parsing)
- **Frontend**: Streamlit (or React for scalability)

## Installation & Setup

### Prerequisites
- Python 3.8+
- `pip` installed
- OpenAI API Key

### Clone Repository
```bash
git clone https://github.com/yourusername/NeuroTutor.git
cd NeuroTutor
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set OpenAI API Key
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Run the Backend
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### Running the Frontend (Streamlit Example)
```bash
streamlit run frontend.py
```

## Usage
1. Upload a PDF containing class notes.
2. Speak to NeuroTutor using your microphone.
3. Receive AI-powered explanations based on your notes.
4. Use the Feynman technique to reinforce understanding.

## Future Enhancements
- Implement real-time conversation mode.
- Add better note organization and search capabilities.
- Improve retrieval-based AI responses with fine-tuned models.

## Contributing
Contributions are welcome! Fork this repo and submit a pull request.

## License
MIT License
