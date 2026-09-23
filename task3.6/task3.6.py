import unicodedata
from collections import Counter

language_weights = {
    "English": {
        "a": 8.2, "b": 1.5, "c": 2.8, "d": 4.3, "e": 12.7,
        "f": 2.2, "g": 2.0, "h": 6.1, "i": 7.0, "j": 0.2,
        "k": 0.8, "l": 4.0, "m": 2.4, "n": 6.7, "o": 7.5,
        "p": 1.9, "q": 0.1, "r": 6.0, "s": 6.3, "t": 9.1,
        "u": 2.8, "v": 1.0, "w": 2.4, "x": 0.2, "y": 2.0,
        "z": 0.1
    },

    "French": {
        "a": 7.6, "b": 0.9, "c": 3.3, "d": 3.7, "e": 14.7,
        "f": 1.1, "g": 0.9, "h": 0.7, "i": 7.5, "j": 0.6,
        "k": 0.1, "l": 5.5, "m": 3.0, "n": 7.1, "o": 5.8,
        "p": 2.5, "q": 1.4, "r": 6.7, "s": 7.9, "t": 7.2,
        "u": 6.3, "v": 1.8, "w": 0.1, "x": 0.4, "y": 0.3,
        "z": 0.1
    },

    "German": {
        "a": 6.5, "b": 1.9, "c": 3.1, "d": 5.1, "e": 16.4,
        "f": 1.7, "g": 3.0, "h": 4.6, "i": 6.6, "j": 0.3,
        "k": 1.4, "l": 3.4, "m": 2.5, "n": 9.8, "o": 2.6,
        "p": 0.7, "q": 0.02, "r": 7.0, "s": 7.3, "t": 6.2,
        "u": 4.2, "v": 0.8, "w": 1.9, "x": 0.03, "y": 0.04,
        "z": 1.1
    },

    "Spanish": {
        "a": 12.5, "b": 1.4, "c": 4.7, "d": 5.9, "e": 13.7,
        "f": 0.7, "g": 1.0, "h": 0.7, "i": 6.2, "j": 0.4,
        "k": 0.1, "l": 5.0, "m": 3.2, "n": 6.7, "o": 8.7,
        "p": 2.5, "q": 0.9, "r": 6.9, "s": 8.0, "t": 4.6,
        "u": 3.9, "v": 0.9, "w": 0.1, "x": 0.2, "y": 0.9,
        "z": 0.5
    }
}

def normalize_text(text):
    text = text.lower()
    text = text.replace("ß", "ss")
    text = text.replace("œ", "oe")
    text = text.replace("æ", "ae")

    return "".join(
        character
        for character in unicodedata.normalize("NFD", text)
        if unicodedata.category(character) != "Mn"
    )


text = normalize_text(input("Enter text: "))

letters = [
    letter for letter in text
    if "a" <= letter <= "z"
]

if not letters:
    print("No letters found.")

else:
    counts = Counter(letters)
    total = len(letters)
    scores = {}

    for language, weights in language_weights.items():
        score = 0

        for letter, expected_weight in weights.items():
            actual_weight = counts[letter] / total * 100
            score += abs(actual_weight - expected_weight)

        scores[language] = score

    detected_language = min(scores, key=scores.get)

    print("Detected language:", detected_language)
