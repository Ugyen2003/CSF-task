score = int(input("Enter your score: "))

if score >= 90:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
elif score < 60:
    print("F")
else:
    print("Invalid score")
