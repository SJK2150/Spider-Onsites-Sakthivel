
import re

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
