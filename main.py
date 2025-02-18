from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import fitz  # PyMuPDF for PDF parsing
import openai
import whisper
import os
import tempfile

app = FastAPI()

# Initialize OpenAI API (set your key as env variable or here directly)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load Whisper model (small model for speed)
model = whisper.load_model("small")

# Store PDFs temporarily
pdf_store = {}

def extract_text_from_pdf(pdf_path):
    """Extract text from uploaded PDF."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

@app.post("/upload_pdf/")
def upload_pdf(file: UploadFile = File(...)):
    """Uploads a PDF and stores its text."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(file.file.read())
        pdf_text = extract_text_from_pdf(temp.name)
        pdf_store[file.filename] = pdf_text  # Store extracted text
    return {"message": "PDF uploaded successfully", "filename": file.filename}

@app.post("/speech_to_text/")
def speech_to_text(audio: UploadFile = File(...)):
    """Converts speech to text using Whisper."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
        temp.write(audio.file.read())
        result = model.transcribe(temp.name)
    return {"transcribed_text": result["text"]}

@app.post("/explain/")
def explain_concept(query: str = Form(...), pdf_name: str = Form(None)):
    """Uses GPT to explain concepts using uploaded notes."""
    notes_context = pdf_store.get(pdf_name, "No relevant notes found.") if pdf_name else ""
    prompt = f"""
    Explain the following concept in simple terms using the Feynman technique:
    {query}
    
    Context from notes:
    {notes_context}
    
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a personal teacher using the Feynman technique."},
                  {"role": "user", "content": prompt}]
    )
    return {"explanation": response["choices"][0]["message"]["content"]}

@app.get("/list_pdfs/")
def list_pdfs():
    """Lists uploaded PDFs."""
    return {"uploaded_pdfs": list(pdf_store.keys())}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
