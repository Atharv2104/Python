n = int(input("Enter number of Fibonacci numbers: "))
a, b = 0, 1
count = 0

print("Fibonacci sequence:")
while count < n:
    print(a, end=" ")
    a,b =b ,a+b
    count+=1
    
