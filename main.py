# main.py
from src.turkish_metaphone import TurkishMetaphone

if __name__ == "__main__":
    tm = TurkishMetaphone()

    examples = [
        "Cem ile Can bahçede geziyor.",
        "Şule sessizce şiir söylüyor.",
        "Gökçe ve Kaan güneşli günleri seviyor.",
        "Zeynep, yüzüğünü denize düşürdü."
    ]

    for text in examples:
        print(f"Original: {text}")
        print(f"Normalized: {tm.normalize_text(text)}")
        print("-" * 60)
