# 🇹🇷 Turkish Metaphone Text Normalization

This repository provides an **original Metaphone implementation for Turkish**, developed to normalize words phonetically and reduce variations in spelling caused by pronunciation differences.

Metaphone is a phonetic algorithm for indexing words by their sound, primarily used in English.  
This project adapts the idea for **Turkish phonetics**, accounting for similar-sounding consonant and vowel groups.

---

## 🧠 Motivation

Turkish words may often differ in **spelling but not in pronunciation** — for instance:
- `meclis` and `mejlis` sound almost identical, though spelled differently.  
- `güzel` → `gsl`, simplifying pronunciation-based matching.
- `şeker`, `seker`, and `zheker` could all normalize to a similar phonetic root.

This algorithm aims to support **text normalization, fuzzy matching, and search applications** in Turkish Natural Language Processing (NLP).

---

## 🧩 Features

- Groups Turkish letters with **phonetically similar sounds**:
  - `c`, `ç`, `j` → same group
  - `s`, `ş`, `z` → same group
  - `k`, `ğ`, `g` → same group
  - `ı`, `i` → vowel group
- Converts words into **metaphone representations**
- Handles **case-insensitive** text
- Designed to integrate easily into other Turkish NLP pipelines

---

## 📁 Repository Structure

```bash
turkish-metaphone/
│
├── src/
│ ├── init.py
│ └── turkish_metaphone.py # Main algorithm implementation
│
├── main.py # Example usage
└── README.md # You are here
```

---

## 🚀 Usage

### 1️⃣ Run example script

```bash
python main.py
```

### 2️⃣ Example output


```bash
Original: meclis
Metaphone: MJLS

Original: güzel
Metaphone: GSL

Original: şeker
Metaphone: SKR
```

### 🔧 Example Python usage

```bash
from src.turkish_metaphone import turkish_metaphone

words = ["meclis", "güzel", "şeker", "mejlis", "zeki", "çocuk"]
for w in words:
    print(f"{w:10s} → {turkish_metaphone(w)}")
```

#### Output:

```bash 
meclis     → MJLS
güzel      → GSL
şeker      → SKR
mejlis     → MJLS
zeki       → SK
çocuk      → CCK
```

---

## 🧪 Applications

- Text normalization for noisy Turkish text

- Fuzzy matching in databases and search engines

- Duplicate detection in NLP preprocessing

- Phonetic clustering of Turkish names or place names

---

## 📜 License

MIT License © 2025 Cem Rıfkı Aydın

Free to use and modify with attribution.

---

## 🌟 Contributing

Pull requests and improvements are warmly welcome —
especially for expanding the Turkish phonetic ruleset!