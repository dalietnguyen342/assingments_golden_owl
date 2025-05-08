import re
from gtts import gTTS
import os

def normalize_vietnamese_text(text):
    """
    Normalize Vietnamese text by handling numbers, abbreviations, and special cases.
    """
    text = re.sub(r'\d+', lambda m: num_to_words(int(m.group())), text)
    
    abbreviations = {
        'ông': 'ông',
        'bà': 'bà',
        'tp': 'thành phố'
    }
    for abbr, full in abbreviations.items():
        text = text.replace(abbr, full)
    
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def num_to_words(number):
    """
    Convert numbers to Vietnamese words (simplified for small numbers).
    """
    vietnamese_numbers = {
        0: 'không', 1: 'một', 2: 'hai', 3: 'ba', 4: 'bốn', 
        5: 'năm', 6: 'sáu', 7: 'bảy', 8: 'tám', 9: 'chín'
    }
    return vietnamese_numbers.get(number, str(number))

def vietnamese_g2p(text):
    """
    Convert Vietnamese text to phonemes (simplified rule-based approach).
    Note: In a real system, use a G2P library or model like VNPhoneme.
    """
    phoneme_map = {
        'xin': 's i n',
        'chào': 'c h a o',
        'mọi': 'm o i',
        'người': 'ng u o i'
    }
    
    words = text.split()
    phonemes = []
    for word in words:
        phonemes.append(phoneme_map.get(word.lower(), word))
    return ' '.join(phonemes)

def synthesize_speech(text, output_file="output.mp3"):
    """
    Synthesize Vietnamese speech using gTTS and save to a file.
    """
    try:
        tts = gTTS(text=text, lang='vi', slow=False)
        
        tts.save(output_file)
        print(f"Audio saved as {output_file}")
    except Exception as e:
        print(f"Error during synthesis: {e}")

def vietnamese_tts_pipeline(input_text):
    """
    Run the full Vietnamese TTS pipeline.
    """
    normalized_text = normalize_vietnamese_text(input_text)
    print(f"Normalized text: {normalized_text}")
    
    phonemes = vietnamese_g2p(normalized_text)
    print(f"Phonemes: {phonemes}")
    
    synthesize_speech(normalized_text)

if __name__ == "__main__":
  
    input_text = "Xin chào mọi người."
    vietnamese_tts_pipeline(input_text)