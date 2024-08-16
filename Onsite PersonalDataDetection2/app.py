from flask import Flask, request, jsonify, render_template
import os
import re
import pytesseract
import cv2
from pdfminer.high_level import extract_text
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.txt'):
        return extract_text_from_textfile(file_path)
    elif file_path.lower().endswith(('.xlsx', '.xls')):
        return extract_text_from_excel(file_path)
    else:
        raise ValueError("Unsupported file type")

def detect_personal_info(text):
    patterns = {
        'Names': r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b',
        'Addresses': r'\d+\s[A-Za-z]+\s[A-Za-z]+',
        'Phone Numbers': r'\+?\d[\d -]{8,12}\d',
        'Social Security Numbers': r'\b\d{3}-\d{2}-\d{4}\b',
        'Dates of Birth': r'\b\d{2}/\d{2}/\d{4}\b',
        'Credit Card Numbers': r'\b\d{4}-\d{4}-\d{4}-\d{4}\b'
    }
    
    detected_info = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        detected_info[key] = matches
    
    return detected_info

@app.route('/process-file', methods=['POST'])
def process_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    
    try:
        text = extract_text_from_file(file_path)
        personal_info = detect_personal_info(text)
        return jsonify({'personal_info': personal_info})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
