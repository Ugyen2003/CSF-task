user_name = input("Enter your name: ")

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for char in user_name:
    if char.lower() in vowels:
        count += 1

print(f"Number of vowels in {user_name}: {count}")
