
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("File handling in Python is simple and efficient.\n")


with open("example.txt", "r") as file:
    content = file.read()
    print("\nReading from the file:")
    print(content)

with open("example.txt", "a") as file:
    file.write("This line is appended to the file.\n")

print("\nContent appended successfully!")


with open("example.txt", "r") as file:
    updated_content = file.read()
    print("\nReading the updated file:")
    print(updated_content)