# Student Management System
# Python Project

students = []


# Function to add a student
def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


# Function to display students
def view_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("-------------------------")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Course     :", student["course"])
        print("Marks      :", student["marks"])


# Function to search student
def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Course     :", student["course"])
            print("Marks      :", student["marks"])
            return

    print("Student not found.")


# Function to update student
def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            student["name"] = input("Enter New Name: ")
            student["age"] = int(input("Enter New Age: "))
            student["course"] = input("Enter New Course: ")
            student["marks"] = float(input("Enter New Marks: "))

            print("Student updated successfully!")
            return

    print("Student not found.")


# Function to delete student
def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Function to calculate average marks
def average_marks():
    print("\n--- Average Marks ---")

    if len(students) == 0:
        print("No students available.")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Average Marks:", round(average, 2))


# Main menu
while True:

    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        average_marks()

    elif choice == "7":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")