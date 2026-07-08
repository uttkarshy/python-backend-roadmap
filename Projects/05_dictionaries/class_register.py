"""
=========================================================
Project    : Class Register
Author     : Utkarsh Yadav
Repository : python-backend-roadmap

Description:
Store student information using dictionaries.

Concepts Used:
- Lists
- Dictionaries
- Loops
=========================================================
"""

students = []


def menu():

    print("\n========== Class Register ==========")

    print("1. Add Student")

    print("2. View Students")

    print("3. Search Student")

    print("4. Exit")


while True:

    menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        student = {}

        student["name"] = input("Enter Name: ")

        student["roll_number"] = input("Enter Roll Number: ")

        student["class"] = input("Enter Class: ")

        students.append(student)

        print("Student Added Successfully.")

    elif choice == "2":

        if len(students) == 0:

            print("No Students Found.")

        else:

            for student in students:

                print("-------------------------")

                for key, value in student.items():

                    print(key, ":", value)

    elif choice == "3":

        roll = input("Enter Roll Number: ")

        found = False

        for student in students:

            if student["roll_number"] == roll:

                for key, value in student.items():

                    print(key, ":", value)

                found = True

                break

        if found == False:

            print("Student Not Found.")

    elif choice == "4":

        print("Closing Register.")

        break

    else:

        print("Invalid Choice.")
