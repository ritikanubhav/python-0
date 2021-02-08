a = input("what is your name?\n")
b = int(input("what is your age?\n"))
c = input("what is your sex?\n")
d= c.lower()
e= a.upper()
if d=="male":
    print("MR.",e,"your age is",b,"and your sex is",d )
elif d=="female":
    print("MRS.",e,"your age is",b,"and your sex is",d)
else:
    print("your name is ",e,"your age is",b,'your sex is',d,)