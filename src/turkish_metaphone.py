# src/turkish_metaphone.py
# A lightweight Metaphone-like phonetic normalizer for Turkish.

import re

class TurkishMetaphone:
    """
    A simple Turkish Metaphone-like algorithm for phonetic text normalization.
    Groups letters with similar sounds and normalizes text accordingly.
    """

    def __init__(self):
        # Define phonetic groups
        self.rules = [
            (r"[cçj]", "J"),       # c, ç, j -> J
            (r"[şsz]", "S"),       # ş, s, z -> S
            (r"[ğgkq]", "G"),      # ğ, g, k, q -> G
            (r"[pb]", "P"),        # p, b -> P
            (r"[td]", "T"),        # t, d -> T
            (r"[fv]", "F"),        # f, v -> F
            (r"[mn]", "M"),        # m, n -> M
            (r"[r]", "R"),         # r -> R
            (r"[y]", "Y"),         # y -> Y
            (r"[aeıioöuü]", "A"),  # vowels -> A
        ]

    def normalize_word(self, word: str) -> str:
        """Normalize a single Turkish word phonetically."""
        word = word.lower().strip()

        # Remove non-alphabetic chars
        word = re.sub(r"[^a-zçğıöşü]", "", word)

        # Apply rules
        for pattern, repl in self.rules:
            word = re.sub(pattern, repl, word)

        # Collapse consecutive duplicates (e.g. SS -> S)
        word = re.sub(r"(.)\1+", r"\1", word)

        return word

    def normalize_text(self, text: str) -> list[str]:
        """Normalize all words in a text."""
        words = re.findall(r"\b[\wçğıöşü]+\b", text.lower())
        return [self.normalize_word(w) for w in words]
