age = int(input("enter your age:\n"))
if age >= 18:
    print("you are eligible to vote")
elif 0 < age < 18:
    print("not eligible to vote")
else:
    print("invalid input")

