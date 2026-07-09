visitors=set()
while True:
    print("--------Visitor Registration--------")
    print("1. Register Visitor")
    print("2. View Visitors")
    print("3. Search Visitor")
    print("4. Remove Visitor")
    print("5. Count Visitors")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input")
        continue

    if choice == 1:
        name = input("Enter visitor name: ")
        if name in visitors:
            print("Visitor already registered.")
        else:
            visitors.add(name)
            print("Visitor registered successfully.")
    elif choice == 2:
        print("Registered Visitors:")
        for visitor in visitors:
            print(visitor)
    elif choice==3:
        name=input("Enter visitor name to search: ")
        if name in visitors:
            print(name +" is registered.")
        else:
            print(name +" is not registered.")
    elif choice==4:
        name=input("Enter visitor name to remove: ")
        if name in visitors:
            visitors.remove(name)
            print(name +" removed successfully.")
        else:
            print(name +" is not registered.")
    elif choice==5:
        print("Total Visitors:", len(visitors))
    elif choice==6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")