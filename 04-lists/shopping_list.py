"""
=========================================================
Project    : Shopping List Manager
Author     : Utkarsh Yadav
Repository : python-backend-roadmap

Description:
A simple shopping list manager using Python lists.

Concepts Used:
- Lists
- Functions
- Loops
- if / elif / else
=========================================================
"""

shopping_list = []


def menu():
    print("\n========== Shopping List ==========")
    print("1. View Items")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Count Items")
    print("5. Exit")


while True:

    menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        if len(shopping_list) == 0:
            print("Shopping list is empty.")

        else:

            print("\nShopping Items")

            count = 1

            for item in shopping_list:

                print(count, ".", item)

                count = count + 1

    elif choice == "2":

        item = input("Enter item name: ")

        shopping_list.append(item)

        print("Item added successfully.")

    elif choice == "3":

        item = input("Enter item name to remove: ")

        if item in shopping_list:

            shopping_list.remove(item)

            print("Item removed successfully.")

        else:

            print("Item not found.")

    elif choice == "4":

        print("Total Items :", len(shopping_list))

    elif choice == "5":

        print("Closing Shopping List.")

        break

    else:

        print("Invalid Choice.")
