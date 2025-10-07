# src/turkish_metaphone.py
# A lightweight Metaphone-like phonetic normalizer for Turkish.

import re

class TurkishMetaphone:
    """
    A simple Turkish Metaphone-like algorithm for phonetic text normalization.
    Groups letters with similar sounds and normalizes text accordingly.
    """

    def __init__(self):
        # Define Turkish phonetic equivalence rules
        self.rules = [
            (r"[cçj]", "J"),       # c, ç, j -> J
            (r"[şsz]", "S"),       # ş, s, z -> S
            (r"[ğgkq]", "G"),      # ğ, g, k, q -> G
            (r"[pb]", "P"),        # p, b -> P
            (r"[td]", "T"),        # t, d -> T
            (r"[fv]", "F"),        # f, v -> F
            (r"[mn]", "M"),        # m, n -> M
            (r"[r]", "R"),         # r -> R
            (r"[l]", "L"),         # l -> L
            (r"[y]", "Y"),         # y -> Y
            (r"[aeıioöuü]", "A"),  # all vowels -> A
        ]

    def encode(self, word: str) -> str:
        # Normalize input
        word = word.lower().strip()

        # Step 1: Remove non-Turkish letters/symbols
        word = re.sub(r"[^a-zçğıöşü]", "", word)

        # Step 2: Drop duplicate adjacent letters at the beginning
        word = re.sub(r"(.)(\1)+", r"\1", word)

        # Step 3: Apply phonetic rules **progressively**
        w = word
        for pattern, replacement in self.rules:
            w = re.sub(pattern, replacement, w)

        # Step 4: Keep only leading vowel
        if w and w[0] == "A":
            w = w[0] + re.sub(r"A", "", w[1:])
        else:
            w = re.sub(r"A", "", w)

        return w

