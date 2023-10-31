user_number = int(input("Enter a number: "))
fact = 1
i = 1

while i <= user_number:
    fact *= i
    i += 1

print("Factorial of", user_number, "is:", fact)
