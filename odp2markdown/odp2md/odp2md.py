import os
from pathlib import Path
from pdfx import PDFx

data_dir = Path('.')

def odp_to_pdf(filename):
    """
    This function converts ODP files to PDF
    """
    odp_file = data_dir / filename
    os.system(f'libreoffice --headless --convert-to pdf {odp_file}')

def pdf_to_text(filename):
    """
    This function converts pdf text to markdown file.
    This file still needs to be cleaned up.
    """
    pdf_file = str(data_dir / filename)
    pdf_data = PDFx(pdf_file)
    pdf_text = pdf_data.get_text()
    with open(f'{filename}.md', 'w') as f:
        f.write(pdf_text)

def clean_text(filename):
    pass
