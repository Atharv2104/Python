x=int(input("enter a  first number:"))
y=int(input("enter a  second number:"))
z=int(input("enter a  third number:"))

if x<y or x<z:
    print("small no",x)
elif y<z:
    print("small no",y)
else:
    print("small no",z)