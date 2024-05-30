import easyocr
import re
import tkinter.filedialog

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

def extract_name_and_birth_date(image_path):
    # Perform OCR on the image
    results = reader.readtext(image_path, detail=0)

    # Join all text pieces into a single string with newlines
    text = '\n'.join(results)

    # Define regex patterns for name and birth date with better matching
    name_pattern = re.compile(r'Name:\s*([A-Za-z ]+)\s*(?:\n|$)', re.IGNORECASE)
    birth_date_pattern = re.compile(r'Date of Birth:\s*(\d{2}/\d{2}/\d{4})', re.IGNORECASE)

    # Search for the patterns in the text
    name_match = name_pattern.search(text)
    birth_date_match = birth_date_pattern.search(text)

    # Extract the matched groups or set to None if not found
    name = name_match.group(1).strip() if name_match else None
    birth_date = birth_date_match.group(1).strip() if birth_date_match else None

    return name, birth_date

def upload_file():
    file_path = tkinter.filedialog.askopenfilename(title="Select Document Image", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    return file_path

def extractDetails():
    print("Please select the document image.")
    image_path = upload_file()

    if image_path:
        name, birth_date = extract_name_and_birth_date(image_path)
    return name, birth_date

#extractDetails()