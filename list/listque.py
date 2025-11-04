
students = []
grades = []


def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))
    students.append(name)
    grades.append(grade)
    print("Student added successfully!")


def update_grade():
    name = input("Enter student name to update: ")
    if name in students:
        index = students.index(name)
        new_grade = float(input("Enter new grade: "))
        grades[index] = new_grade
        print("Grade updated successfully!")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed successfully!")
    else:
        print("Student not found.")


def average_grade():
    if grades:
        avg = sum(grades) / len(grades)
        print("Average grade is:", round(avg, 2))
    else:
        print("No students in the list.")


def high_low_grade():
    if grades:
        print("Highest grade:", max(grades))
        print("Lowest grade:", min(grades))
    else:
        print("No students in the list.")


while True:
    print("\nStudent Grade Management ")
    print("1. Add student")
    print("2. Update grade")
    print("3. Remove student")
    print("4. Average grade")
    print("5. Highest and lowest grade")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        average_grade()
    elif choice == "5":
        high_low_grade()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
