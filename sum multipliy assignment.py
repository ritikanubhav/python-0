a = int(input("enter first no :\n"))
b = int(input("enter second no :\n"))
c = int(input("enter third no :\n"))
d = (a+b)*c
print("your result is:","(",a,"+",b,")","*",c,"=",d)
if d > 100:
    print('that is greater than 100')
elif d == 100:
    print("that is equal to 100")
else:
    print("that is less than 100")


