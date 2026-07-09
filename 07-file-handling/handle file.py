"""
file = open("students.txt", "w")

file.write("Rahul")

file.write("Aman")

file.close()
"""

file=open("students.txt","r")
print(file.read())
file.close()