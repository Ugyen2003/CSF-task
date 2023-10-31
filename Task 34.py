temperature = int(input("Enter temperature: "))
if temperature >= 100:
    print("Boiling")
elif 32 <= temperature <= 99:
    print("Liquid")
else:
    print("Freezing")