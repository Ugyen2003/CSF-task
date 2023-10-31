user_name = input("Enter your name: ")

vowels = ['a', 'e', 'i', 'o', 'u']

i = 0
has_vowel = False
while i < len(user_name):
    if user_name[i] in vowels:
        has_vowel = True
        break
    i += 1

print(has_vowel)
