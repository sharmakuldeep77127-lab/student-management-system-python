students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        student = {
            "roll_no": roll_no,
            "name": name
        }

        students.append(student)
        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found")

        else:
            print("\nStudent Records")

            for student in students:
                print("---------------------")
                print("Roll No:", student["roll_no"])
                print("Name:", student["name"])

    elif choice == "3":

        search_name = input("Enter Student Name to Search: ")

        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("Student Found")
                print("Roll No:", student["roll_no"])
                print("Name:", student["name"])
                found = True

        if not found:
            print("Student Not Found")

    elif choice == "4":

        update_name = input("Enter Student Name to Update: ")

        found = False

        for student in students:
            if student["name"].lower() == update_name.lower():

                new_name = input("Enter New Name: ")

                student["name"] = new_name

                print("Student Updated Successfully!")
                found = True

        if not found:
            print("Student Not Found")

    elif choice == "5":

        delete_name = input("Enter Student Name to Delete: ")

        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():

                students.remove(student)

                print("Student Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found")

    elif choice == "6":

        print("Total Students:", len(students))

    elif choice == "7":

        print("Thank You!")
        break

    else:
        print("Invalid Choice")