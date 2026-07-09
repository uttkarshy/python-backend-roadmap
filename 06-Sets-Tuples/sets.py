"""
=========================================================
Topic      : Sets
Author     : Utkarsh Yadav
Repository : python-backend-roadmap

Description:
Basic practice of Python Sets.

Concepts Used:
- Creating Sets
- add()
- remove()
- len()
- for loop
=========================================================
"""
print("----- Creating Set -----")
students = {"Rahul", "Aman", "Utkarsh"}
print(students)
print()
print("----- Adding Student -----")
students.add("Rohit")
print(students)
print()
print("----- Duplicate Student -----")
students.add("Rahul")
print(students)
print()
print("----- Removing Student -----")
students.remove("Aman")
print(students)
print()
print("----- Length -----")
print(len(students))
print()
print("----- Loop -----")
for student in students:
    print(student)