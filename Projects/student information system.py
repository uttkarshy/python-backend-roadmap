    
students = open("students.txt", "a+")
while True:
    print("--------Student Information System--------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input")
        continue
    students = open("students.txt", "r")
    if choice == 1:
        name = input("Enter student name: ")
        students = open("students.txt", "a")
        students.write(name + "\n")
        students.close()
        print("Student added successfully.")
    elif choice == 2:
        print("Registered Students:")
        for student in students:
            print(student)
    elif choice == 3:
        name = input("Enter student name to search: ")
        found = False
        for student in students:
            if student.strip() == name:
                found = True
                break
        if found:
            print(name, "is registered.")
        else:
            print(name, "is not registered.")
    elif choice == 4:
        name = input("Enter student name to update: ")
        found = False
        students_list = students.readlines()
        for i in range(len(students_list)):
            if students_list[i].strip() == name:
                new_name = input("Enter new name: ")
                students_list[i] = new_name + "\n"
                found = True
                break
        if found:
            students = open("students.txt", "w")
            students.writelines(students_list)
            students.close()
            print(name, "updated successfully.")
        else:
            print(name, "is not registered.")
    elif choice == 5:
        name = input("Enter student name to delete: ")
        found = False
        students_list = students.readlines()
        for i in range(len(students_list)):
            if students_list[i].strip() == name:
                del students_list[i]
                found = True
                break
        if found:
            students = open("students.txt", "w")
            students.writelines(students_list)
            students.close()
            print(name, "deleted successfully.")
        else:
            print(name, "is not registered.")
    elif choice == 6:
        print("Exiting...")
        break
    