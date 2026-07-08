"""
=========================================================
Project    : Attendance System
Author     : Utkarsh Yadav
Repository : python-backend-roadmap

Description:
A console-based attendance management system.

Concepts Used:
- Lists
- Loops
- Functions
=========================================================
"""

attendance = []


def menu():

    print("\n========== Attendance System ==========")

    print("1. Mark Present")

    print("2. View Attendance")

    print("3. Search Student")

    print("4. Count Students")

    print("5. Exit")


while True:

    menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        student = input("Enter Student Name: ")

        attendance.append(student)

        print("Attendance marked.")

    elif choice == "2":

        if len(attendance) == 0:

            print("No attendance found.")

        else:

            print("\nPresent Students")

            for student in attendance:

                print(student)

    elif choice == "3":

        search = input("Enter Student Name: ")

        found = False

        for student in attendance:

            if student == search:

                found = True

                break

        if found:

            print("Student is Present.")

        else:

            print("Student Not Found.")

    elif choice == "4":

        print("Total Present Students :", len(attendance))

    elif choice == "5":

        print("Closing Attendance System.")

        break

    else:

        print("Invalid Choice.")
