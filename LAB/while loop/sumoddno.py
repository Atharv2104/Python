n = int(input("Enter limit for sum of odd numbers: "))
i = 1
result = 0
while i < n:
    if i % 2 != 0:
        result += i
    i += 1
print("Sum of odd numbers is:", result)