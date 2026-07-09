"""
=========================================================
Topic      : Tuples
Author     : Utkarsh Yadav
Repository : python-backend-roadmap

Description:
Basic practice of Python Tuples.

Concepts Used:
- Creating Tuples
- Indexing
- len()
- for loop
=========================================================
"""
print("----- Creating Tuple -----")
months = (
    "January",
    "February",
    "March"
)
print(months)
print()
print("----- First Month -----")
print(months[0])
print()
print("----- Length -----")
print(len(months))
print()
print("----- Loop -----")
for month in months:
    print(month)