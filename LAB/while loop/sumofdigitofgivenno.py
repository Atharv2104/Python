x = int(input("Enter a number: "))
sum = 0

while x > 0:
    digit = x % 10  # Get the last digit
    sum += digit    # Add it to the sum
    x = x // 10     # Remove the last digit

print("Sum of digits:", sum)