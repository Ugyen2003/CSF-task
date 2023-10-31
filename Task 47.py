user_number = int(input("Enter a number: "))
fact = 1

for i in range(1, user_number + 1):
    fact *= i

print("Factorial of", user_number, "is:", fact)
