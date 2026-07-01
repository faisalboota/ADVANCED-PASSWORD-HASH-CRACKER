import random

common_passwords = [
    "123456",
    "123456789",
    "password",
    "admin",
    "welcome",
    "qwerty",
    "abc123",
    "letmein",
    "dragon",
    "monkey",
    "football",
    "baseball",
    "shadow",
    "master",
    "hello",
    "computer",
    "python",
    "cyber",
    "security",
    "trustno1",
    "administrator",
    "login",
    "guest",
    "root",
    "pass123",
]

years = range(1990, 2031)
symbols = ["", "!", "@", "#", "$"]

wordlist = set()

# Add common passwords
for password in common_passwords:
    wordlist.add(password)

# Generate variations
for password in common_passwords:
    for year in years:
        wordlist.add(f"{password}{year}")
        wordlist.add(f"{password}_{year}")
        wordlist.add(f"{password}{year}!")

    for number in range(10000):
        wordlist.add(f"{password}{number}")

    for symbol in symbols:
        wordlist.add(password + symbol)

# Add random passwords
letters = "abcdefghijklmnopqrstuvwxyz"

while len(wordlist) < 50000:
    length = random.randint(6, 12)
    pwd = "".join(random.choice(letters) for _ in range(length))
    wordlist.add(pwd)

with open("wordlists/big_test.txt", "w", encoding="utf-8") as file:
    for password in sorted(wordlist):
        file.write(password + "\n")

print(f"Wordlist created successfully!")
print(f"Total passwords: {len(wordlist):,}")
print("Saved as: wordlists/big_test.txt")