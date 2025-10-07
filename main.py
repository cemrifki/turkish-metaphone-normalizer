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

        # Split text into tokens by whitespace
        tokens = text.strip().split()

        # Normalize each token separately
        normalized_tokens = [tm.encode(token) for token in tokens]

        # Join back into a sentence
        normalized_text = " ".join(normalized_tokens)

        print(f"Normalized: {normalized_text}")
        print("-" * 60)
