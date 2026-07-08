"""
=========================================================
Project    : Marks Manager
Author     : Utkarsh Yadav
Repository : python-backend-roadmap

Description:
Manage student marks using dictionaries.

Concepts Used:
- Lists
- Dictionaries
- Loops
=========================================================
"""

students = []


def menu():

    print("\n========== Marks Manager ==========")

    print("1. Add Student")

    print("2. View Marks")

    print("3. Update Marks")

    print("4. Highest Marks")

    print("5. Average Marks")

    print("6. Exit")


while True:

    menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        student = {}

        student["name"] = input("Enter Student Name: ")

        student["marks"] = int(input("Enter Marks: "))

        students.append(student)

        print("Student Added Successfully.")

    elif choice == "2":

        if len(students) == 0:

            print("No Records Found.")

        else:

            for student in students:

                print(student["name"], ":", student["marks"])

    elif choice == "3":

        name = input("Enter Student Name: ")

        found = False

        for student in students:

            if student["name"] == name:

                student["marks"] = int(input("Enter New Marks: "))

                print("Marks Updated Successfully.")

                found = True

                break

        if found == False:

            print("Student Not Found.")

    elif choice == "4":

        if len(students) == 0:

            print("No Records Found.")

        else:

            highest = students[0]

            for student in students:

                if student["marks"] > highest["marks"]:

                    highest = student

            print("Highest Marks")

            print(highest["name"])

            print(highest["marks"])

    elif choice == "5":

        if len(students) == 0:

            print("No Records Found.")

        else:

            total = 0

            for student in students:

                total = total + student["marks"]

            average = total / len(students)

            print("Average Marks :", average)

    elif choice == "6":

        print("Closing Marks Manager.")

        break

    else:

        print("Invalid Choice.")
