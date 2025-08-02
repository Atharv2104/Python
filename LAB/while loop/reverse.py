n = int(input("Enter limit for sum of natural numbers: "))
i = n
result = 0
print("Numbers in reverse order:")
while i >= 1:
    print(i, end=" ")
    result += i
    i -= 1
print("\nSum of natural numbers is", result)