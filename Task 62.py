# Define an empty list
user_inputs = []

# Get three user inputs and append them to the list
for i in range(3):
    number = int(input("Enter a number: "))
    user_inputs.append(number)
    
# Definea function that checks if all numbers are even
def is_even(user_inputs):
    return all(number % 2 == 0 for number in user_inputs)

# Call the function with user_inputs as an arguments and print the result
print(is_even(user_inputs))