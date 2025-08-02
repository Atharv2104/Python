n = int(input("Enter the number of elements: "))
if n <= 0:
    print("Please enter a positive number.")
else:
    smallest=None
    count=0
    while count<n:
        number=int(input("enter a no:"))
        if smallest is None or number<smallest:
            smallest=number
            count-=1
            print("smallestno is",smallest)
       

    