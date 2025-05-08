# Named Entity Recognition (NER) Report – Resume Extraction

## 🎯 Objective
To extract name and email from CV PDF files using NLP tools, specifically SpaCy and Regex.

## 🧪 Methodology

### 1. PDF Text Extraction
- Used **PyMuPDF (fitz)** to extract raw text from PDF documents.

### 2. Name Extraction
- Applied **SpaCy's `en_core_web_sm` model**
- Filtered entities labeled as `PERSON`.

### 3. Email Extraction
- Used Regular Expression to capture common email formats.

## 🔎 Example Output
From the test file `cv_1.pdf`, the system extracted:
- Name: **Nguyen Thanh Xuan**
- Email: **xuanusm@gmail.com**

## ⚠️ Challenges
- Some names may be missed or split if SpaCy is uncertain or if layout is inconsistent.
- Email formats can be non-standard and not easily captured.

## 💡 Future Improvements
- Train custom NER model for Vietnamese names using SpaCy or HuggingFace Transformers.
- Improve email detection with layout heuristics or multiple regex checks.
- Add PDF layout parsing (like table detection or heading recognition).
