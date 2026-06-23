students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        students.append(name)
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found")
        else:
            print("\nStudent List:")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student}")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")