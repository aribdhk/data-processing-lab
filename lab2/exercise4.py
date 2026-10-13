text = input("Enter a word or short sentence: ")

characters = 0
vowels = 0
spaces = 0

for ch in text:
    characters += 1
    if ch.lower() in "aeiou":
        vowels += 1
    if ch == " ":
        spaces += 1

print("Number of characters:", characters)
print("Number of vowels    :", vowels)
print("Number of spaces    :", spaces)