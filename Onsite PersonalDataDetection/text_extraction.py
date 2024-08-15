import pytesseract
import cv2
from pdfminer.high_level import extract_text
import pandas as pd

def extract_text_from_excel(file_path):
    xls = pd.ExcelFile(file_path)
    text = ""
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        text += df.to_string(index=False)
    return text

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text

def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    return text

def extract_text_from_textfile(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def extract_text_from_file(file_path):
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        return extract_text_from_image(file_path)
    elif file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)  # Fixed recursive call
    elif file_path.lower().endswith('.txt'):
        return extract_text_from_textfile(file_path)
    elif file_path.lower().endswith(('.xlsx', '.xls')):
        return extract_text_from_excel(file_path)
    else:
        raise ValueError("Unsupported file type")
