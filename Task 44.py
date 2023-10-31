user_name = input("Enter your name: ")

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
i = 0
while i < len(user_name):
    if user_name[i].lower() in vowels:
        count += 1
    i += 1

print(f"Number of vowels in {user_name}: {count}")
