import fitz  # PyMuPDF
import docx

def extract_text_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_docx(file):
    doc = docx.Document(file)
    return " ".join([para.text for para in doc.paragraphs])
