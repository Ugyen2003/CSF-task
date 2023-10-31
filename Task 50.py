num1 = int(input("Enter the first number: "))  
num2 = int(input("Enter the second number: "))  

# Make sure num1 is smaller than num2
if num1 > num2:
    num1, num2 = num2, num1

sum_of_numbers = 0  # Initialize the sum to 0

# Iterate through the numbers between num1 and num2 (inclusive)
current_num = num1
while current_num <= num2:
    sum_of_numbers += current_num  # Add the current number to the sum
    current_num += 1  # Increment the current number

print("The sum of numbers between", num1, "and", num2, "is", sum_of_numbers)


