# 2. Advanced List Methods and Identity Operators
# Objective: The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

# Problem Statement:
# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists: Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both = [submitted[0], attended[0]]

print(f"Students that submitted assignments and attended class = {both}")

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

print(f"The two lists are not identical = {submitted is not attended}")

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

attended.sort()
attended.pop()
attended.pop()

print(f"Attended list, after removing students without submitted assignments = {attended}")