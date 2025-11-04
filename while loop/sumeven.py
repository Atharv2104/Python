n = int(input("Enter limit for sum of even numbers: "))
i = 0
result = 0
while i < n:
    if i % 2 == 0:
        result += i
    i += 1
print("Sum of even numbers is:", result)