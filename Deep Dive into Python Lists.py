# 4. Deep Dive into Python Lists
# Objective: The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

# Problem Statement: You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"

position = 2
transcript = [students[position], grades[position], activities[position]]

print(f"Students with grades below 80 = {transcript}")


# Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]

students_approved = students.copy()
students_approved.remove("Jane")

# Task 3: Print the list students_approved

print(f"Students approved = {students_approved}")