n = int(input("Enter the number of elements: "))
if n <= 0:
    print("Please enter a positive number.")
else:
    largest =None
    count=0
    while count < n:
        number=int(input("enter a no:"))
        if largest is None or number>largest:
            largest=number
            count+=1
            print("lagest no is",largest)
        

    