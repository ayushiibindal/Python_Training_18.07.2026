vov = input("Enter an alphabet: ").strip().lower()

if len(vov) != 1 or not vov.isalpha():
    print("Please enter only one alphabet.")
elif vov in "aeiou":
    print(f"{vov} is a vowel.")
else:
    print(f"{vov} is a consonant.")