
from text_extraction import extract_text_from_file
from personal_info_detection import detect_personal_info

def main(file_path):
    text = extract_text_from_file(file_path)
    personal_info = detect_personal_info(text)
    
    print("Detected Personal Information:")
    for info_type, values in personal_info.items():
        print(f"{info_type}:")
        for value in values:
            print(f" - {value}")


if __name__ == "__main__":
    file_path = 'data.pdf' 
    main(file_path)
