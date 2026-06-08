import re

password = input("Enter Password: ")

suggestions = []
score = 0

if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters")

if re.search("[A-Z]", password):
    score += 1
else:
    suggestions.append("Add an uppercase letter")

if re.search("[a-z]", password):
    score += 1
else:
    suggestions.append("Add a lowercase letter")

if re.search("[0-9]", password):
    score += 1
else:
    suggestions.append("Add a number")

if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    suggestions.append("Add a special character")

if score == 5:
    print("\nPassword Strength: Very Strong")
elif score == 4:
    print("\nPassword Strength: Strong")
elif score == 3:
    print("\nPassword Strength: Medium")
else:
    print("\nPassword Strength: Weak")

if suggestions:
    print("\nSuggestions:")
    for item in suggestions:
        print("-", item)