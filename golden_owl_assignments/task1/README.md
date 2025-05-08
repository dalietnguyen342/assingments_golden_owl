
# Resume NER Extractor

This project extracts **Name** and **Email** from PDF resumes using Python and SpaCy.

## 🔧 Requirements

- **Python >= 3.8**
- `spacy` (for Named Entity Recognition)
- `PyMuPDF` (for reading PDF files)

### 📦 Install dependencies
1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

---

## ▶️ How to run the script

1. Place the PDF resume files inside the `resume/` folder (or specify the path to any PDF you want to process).
2. Run the Python script with the following command:

   ```bash
   pip install -r requirements.txt
   python main.py /path/to/your/file.pdf
   ```

   Replace `/path/to/your/file.pdf` with the actual path to the file you want to extract information from.

---

## 📦 Output

The script will print the **Name** and **Email** extracted from the provided PDF resume.

Example output:
```bash
📄 File: cv_1.pdf
   👤 Name: Nguyen Thanh Xuan
   📧 Email: xuanusm@gmail.com
```

If the name or email cannot be found, it will output:
```bash
📄 File: cv_1.pdf
   👤 Name: Name not found
   📧 Email: Email not found
```

---

## 🔧 Explanation of the code

### Step 1: **Read the PDF File**

- We use **PyMuPDF** (`fitz`) to extract raw text from the provided PDF file.

### Step 2: **Extract Name**

- **SpaCy's Named Entity Recognition (NER)** model (`en_core_web_sm`) is used to extract entities labeled as `PERSON`. The name is recognized as a **PERSON** entity.

### Step 3: **Extract Email**

- We use **Regex** to find and extract the email address from the text.

---

## ⚠️ Known Limitations

1. **Complex PDF layouts**: The script may have issues with extracting text from PDFs with complex formatting or embedded images. For those cases, **OCR** (Optical Character Recognition) would be needed.
2. **Non-standard names or email formats**: The accuracy of name extraction can be affected by non-standard name formats, especially for non-English names.

---

## 💡 Future Improvements

- **Custom SpaCy model for Vietnamese names**: This will improve the accuracy of extracting names from Vietnamese resumes.
- **Enhanced email detection**: Use more sophisticated Regex or natural language processing methods to better handle complex email formats.
- **OCR support**: Integrating OCR (e.g., using `pytesseract`) could help extract text from scanned images in PDFs.

---

## 📝 Files

1. **`main.py`**: The main Python script for processing PDF files and extracting name and email.
2. **`requirements.txt`**: A list of dependencies required for the project.
3. **`report.md`**: The report explaining the methodology used to solve the task.
4. **`README.md`**: This file providing instructions on how to use the project.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
