from collections import Counter
from string import ascii_lowercase
import unicodedata

text = input("Enter UTF-8 text: ").casefold()
unicode_letters = [character for character in text if character.isalpha()]
counts = Counter(unicode_letters)

if not unicode_letters:
    print("No letters found.")
    raise SystemExit

print("Letter frequencies:")

for letter, count in sorted(counts.items()):
    frequency = count / len(unicode_letters) * 100
    print(f"{letter}: {frequency:.2f}%")

characters = set(text)

if characters & set("ßäö"):
    detected_language = "German"
elif characters & set("ñ¿¡"):
    detected_language = "Spanish"
elif characters & set("œæçàâèêëîïôùûÿ"):
    detected_language = "French"
else:
    normalized = unicodedata.normalize("NFD", text)
    normalized = "".join(
        character
        for character in normalized
        if unicodedata.category(character) != "Mn"
    )

    letters = [
        character
        for character in normalized
        if character in ascii_lowercase
    ]

    ascii_counts = Counter(letters)

    language_orders = {
        "English": "etaoinshrdlucmfwypvbgkjqxz",
        "French": "esaitnrulodcmpvqfbghjxykwz",
        "German": "enisratdhulgocmbfkwzpvjyxq",
        "Spanish": "eaosrnidlctumpbgvyqhfzjxkw",
    }

    observed_order = "".join(
        sorted(
            ascii_lowercase,
            key=lambda letter: ascii_counts[letter],
            reverse=True,
        )
    )

    scores = {
    language: sum(
        ascii_counts[letter] / len(letters)
        * abs(
            observed_order.index(letter)
            - expected_order.index(letter)
        )
        for letter in ascii_lowercase
    )
    for language, expected_order in language_orders.items()
}

    detected_language = min(scores, key=scores.get)

print("Detected language:", detected_language)
