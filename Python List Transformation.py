# 1. Python List Transformation
# Objective: The aim of this assignment is to practice advanced list operations and transformations.

# Problem Statement:
# You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

# Given the list of grades:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Task 1: Sort the grades in descending order and display the sorted list.

grades.sort()
grades.reverse()
print(f"Sorted grades in descending order = {grades}")

# Task 2: Calculate the average grade and display it.

average_grade = sum(grades) / len(grades)

print(f"Average grade = {average_grade}")

# Task 3: Replace any grade below 80 with the value Failed.
grades.sort()
grades.reverse()
grades[7:] = ["Failed", "Failed", "Failed"]

print(f"Replaced grades = {grades}")