import os
from pathlib import Path
from pdfx import PDFx

data_dir = Path('.')

def odp_to_pdf(filename):
    odp_file = data_dir / filename
    os.system(f'libreoffice --headless --convert-to pdf {odp_file}')

def pdf_to_text(filename):
    pdf_file = str(data_dir / filename)
    pdf_data = PDFx(pdf_file)
    pdf_text = pdf_data.get_text()
    return pdf_text

def text_to_md(text):
    text_file = text
    
