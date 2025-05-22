vowels = "aeiou"

# First vowel
my_str = "flockcin"
for char in my_str:
    if char in vowels:
        print(f"First vowel is\n{char}")
        break

# Last vowel
my_str2 = "hithere"
for char in reversed(my_str2):
    if char in vowels:
        print(f"Last vowel is\n{char}")
        break