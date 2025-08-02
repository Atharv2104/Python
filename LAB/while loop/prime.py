x=int(input("enter a number:"))
i=2
while i<x:
    if x%i==0:
        print("not prime no")
        break
    i+=1
else:
    print("prime No")
    
