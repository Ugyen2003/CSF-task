month = input("Enter the month: ")

if month in ["January", "February", "March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")
elif month in ["September", "October", "November"]:
    print("Fall")
elif month == "December":
    print("Winter")
else:
    print("Invalid month")