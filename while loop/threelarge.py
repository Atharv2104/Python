x=int(input("enter a  first number:"))
y=int(input("enter a  second number:"))
z=int(input("enter a  third number:"))

if x>y or x>z:
    print("large no",x)
elif y>z:
    print("large no",y)
else:
    print("large no",z)