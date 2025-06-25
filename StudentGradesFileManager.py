# Objective:

# Use file handling to:

# a) Write student names and grades to a file.

# b) Read and display content.

# c) Search for a student’s grade.

while True:
    print("1. Add student")
    print("2. View all records")
    print("3. Search by student name")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        with open("grades.txt", "a") as file:
            file.write(f"{name},{grade}\n")
        print("Student added successfully.")
    elif choice == "2":
        with open("grades.txt", "r") as file:
            print(file.read())
    elif choice == "3":
        name = input("Enter student name: ")
        with open("grades.txt", "r") as file:
            for line in file:
                if name in line:
                    print(line)
                    break
            else:
                print("Student not found.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")