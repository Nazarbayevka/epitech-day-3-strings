from collections import Counter
from string import ascii_lowercase

text = input("Enter text: ").lower()
letters = [character for character in text if character in ascii_lowercase]
counts = Counter(letters)

total = len(letters)

if total == 0:
    print("No letters found.")
    raise SystemExit

print("Letter frequencies:")

for letter in ascii_lowercase:
    if counts[letter]:
        frequency = counts[letter] / total * 100
        print(f"{letter}: {frequency:.2f}%")

language_orders = {
    "English": "etaoinshrdlucmfwypvbgkjqxz",
    "French": "esaitnrulodcmpvqfbghjxykwz",
    "German": "enisratdhulgocmbfkwzpvjyxq",
    "Spanish": "eaosrnidlctumpbgvyqhfzjxkw",
}

observed_order = "".join(
    sorted(ascii_lowercase, key=lambda letter: counts[letter], reverse=True)
)


scores = {}

for language, expected_order in language_orders.items():
    score = sum(
        counts[letter] / total
        * abs(
            observed_order.index(letter)
            - expected_order.index(letter)
        )
        for letter in ascii_lowercase
    )
    scores[language] = score


detected_language = min(scores, key=scores.get)

print("Detected language:", detected_language)
