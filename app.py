import streamlit as st
import requests

st.title("NeuroTutor - AI Personal Teacher")

# Upload PDF
tab1, tab2 = st.tabs(["Upload Notes", "Ask AI"])

with tab1:
    st.header("Upload Class Notes (PDF)")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/upload_pdf/", files=files)
        if response.status_code == 200:
            st.success("PDF uploaded successfully!")
        else:
            st.error("Error uploading PDF")

with tab2:
    st.header("Ask AI Your Questions")
    pdfs_response = requests.get("http://127.0.0.1:8000/list_pdfs/")
    if pdfs_response.status_code == 200:
        pdf_options = pdfs_response.json().get("uploaded_pdfs", [])
    else:
        pdf_options = []
    
    pdf_name = st.selectbox("Select a PDF (Optional)", [None] + pdf_options)
    query = st.text_area("Enter your question")
    if st.button("Explain"):
        data = {"query": query, "pdf_name": pdf_name}
        response = requests.post("http://127.0.0.1:8000/explain/", data=data)
        if response.status_code == 200:
            st.success("AI Explanation:")
            st.write(response.json()["explanation"])
        else:
            st.error("Error fetching explanation")
