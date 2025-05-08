
# AI Intern Assignment – Named Entity Recognition & Text-to-Speech

This repository contains two mini-projects developed as part of an AI internship assignment:

1. **Named Entity Recognition (NER)** – Extracting name and email from PDF resumes.
2. **Vietnamese Text-to-Speech (TTS)** – Synthesizing Vietnamese speech from normalized text.

---

## 📁 Repository Structure

```
.
├── task1/
│   ├── main.py
│   ├── requirements.txt
│   └── report.md
├── task2/
│   ├── main.py
│   └── report.md
├── Vietnamese_TTS_and_NER_Complete_Report.pdf
└── README.md
```

---

## 🧠 Task 1: Named Entity Recognition (NER)

### 📌 Objective
Extract names and email addresses from resumes in PDF format using SpaCy and Regex.

### 🚀 How It Works
- Extract raw text from PDFs using `PyMuPDF (fitz)`.
- Apply SpaCy's `en_core_web_sm` model to detect `PERSON` entities.
- Use regex to extract email addresses.

### 🛠️ Run the Code

```bash
cd ner/
pip install -r requirements.txt
python main.py resume/sample_cv.pdf
```

### 🗃 Sample Output

```
📄 File: sample_cv.pdf
   👤 Name: Nguyen Thanh Xuan
   📧 Email: xuanusm@gmail.com
```

---

## 🔊 Task 2: Vietnamese Text-to-Speech (TTS)

### 📌 Objective
Build a simple Vietnamese TTS pipeline that:
- Normalizes input text
- Converts text to phonemes (rule-based)
- Synthesizes speech using Google Text-to-Speech (gTTS)

### 🚀 How It Works
- Normalize numbers and abbreviations in Vietnamese.
- Map words to simplified phoneme-like outputs (for demo).
- Use `gTTS` to synthesize and save as an `.mp3` file.

### 🛠️ Run the Code

```bash
cd tts/
pip install gTTS
python tts_pipeline.py
```

Output will be saved as: `output.mp3`

---

## 📄 Reports

- Full write-up for both tasks is available in [`Vietnamese_TTS_and_NER_Complete_Report.docx`](Vietnamese_TTS_and_NER_Complete_Report.docx)

---

## ✅ Dependencies

| Task | Requirements |
|------|--------------|
| NER  | `spacy`, `PyMuPDF`, `re`, `en_core_web_sm` |
| TTS  | `gTTS`, `re`, `os` |

Install via pip:

```bash
pip install -r ner/requirements.txt
pip install gTTS
python -m spacy download en_core_web_sm
```

---

## 📌 Notes

- Task 1 is designed to be modular and could be expanded with a custom NER model for Vietnamese.
- Task 2 uses gTTS for demo purposes. For production, consider Tacotron2 + HiFi-GAN with Vietnamese datasets like VIVOS.

---

## 👨‍💻 Author

[Your Name] – AI Intern Candidate at Golden Owl Solutions  
Date: May 2025

---

## 📄 License

This project is provided for internship assessment purposes only.
