import fitz  # PyMuPDF
import spacy
import re
import os
import argparse

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Step 1: Read text from PDF using PyMuPDF
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Step 2: Extract name using SpaCy (PERSON entities)
def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Name not found"

# Step 3: Extract email using Regex
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else "Email not found"

# Setup argument parser
def parse_arguments():
    parser = argparse.ArgumentParser(description="Extract Name and Email from a PDF Resume")
    parser.add_argument("pdf_file", help="Path to the PDF file")
    return parser.parse_args()

if __name__ == "__main__":
    # Parse arguments from command line
    args = parse_arguments()

    # Check if the file exists
    if os.path.exists(args.pdf_file) and args.pdf_file.lower().endswith(".pdf"):
        # Extract text from PDF
        text = extract_text_from_pdf(args.pdf_file)
        
        # Extract name and email
        name = extract_name(text)
        email = extract_email(text)

        # Print results
        print(f"📄 File: {args.pdf_file}")
        print(f"   👤 Name: {name}")
        print(f"   📧 Email: {email}\n")
    else:
        print(f"Error: The file '{args.pdf_file}' does not exist or is not a PDF.")
