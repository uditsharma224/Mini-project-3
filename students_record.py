
# Student Records and Marks Analyzer
subjects = ("Python", "Maths", "DBMS")
print("Student Subjects:", subjects)
student_records = {}
total_students = int(input("How many students? "))
for i in range(total_students):
    print("\nEnter details of Student", i + 1)
    student_id = input("Enter Student ID: ")
    # Check duplicate Student ID
    if student_id in student_records:
        print("Student ID already exists!")
        continue
    student_name = input("Enter Student Name: ")
    # Enter and validate marks
    python_marks = int(input("Enter Python Marks: "))
    maths_marks = int(input("Enter Maths Marks: "))
    dbms_marks = int(input("Enter DBMS Marks: "))
    if (0 <= python_marks <= 100 and
        0 <= maths_marks <= 100 and
        0 <= dbms_marks <= 100):
        student_records[student_id] = {
            "name": student_name,
            "marks": [python_marks, maths_marks, dbms_marks]
        }
        print("Student Record Added Successfully!")
    else:
        print("Invalid Marks! Enter marks between 0 and 100.")
        continue
for student_id, details in student_records.items():
    total = 0
    for marks in details["marks"]:
        total = total + marks
    average = total / 3
    if average >= 75:
        result = "Distinction"
    elif average >= 40:
        result = "Pass"
    else:
        result = "Fail"
    details["total"] = total
    details["average"] = average
    details["result"] = result
print("\n========== STUDENT REPORT ==========")
for student_id, details in student_records.items():
    print("\nStudent ID:", student_id)
    print("Name:", details["name"])
    print(subjects[0] + ":", details["marks"][0])
    print(subjects[1] + ":", details["marks"][1])
    print(subjects[2] + ":", details["marks"][2])
    print("Total:", details["total"])
    print("Average:", details["average"])
    print("Result:", details["result"])
search_id = input("\nEnter Student ID to search: ")
if search_id in student_records:
    print("\nStudent Record Found")
    print("Student ID:", search_id)
    print("Student Name:", student_records[search_id]["name"])
    print("Student Marks:", student_records[search_id]["marks"])
else:
    print("Student Record Not Found!")
student_ids = list(student_records.keys())
print("\nFirst Two Student IDs:", student_ids[:2])
if len(student_ids) > 0:
    print("First Student's Python Marks:",
          student_records[student_ids[0]]["marks"][0])

update_id = input("\nEnter Student ID to update marks: ")
if update_id in student_records:
    print("Subjects:", subjects)
    subject_position = int(input(
        "Enter subject position (0 for Python, 1 for Maths, 2 for DBMS): "
    ))
    if 0 <= subject_position <= 2:
        new_marks = int(input("Enter new marks: "))
        if 0 <= new_marks <= 100:
            student_records[update_id]["marks"][subject_position] = new_marks
            print("Marks updated successfully!")
        else:
            print("Invalid Marks! Enter marks between 0 and 100.")
    else:
        print("Invalid Subject Position!")
else:
    print("Student ID not found!")
for student_id, details in student_records.items():
    total = 0
    for marks in details["marks"]:
        total = total + marks
    average = total / 3
    if average >= 75:
        result = "Distinction"
    elif average >= 40:
        result = "Pass"
    else:
        result = "Fail"
    details["total"] = total
    details["average"] = average
    details["result"] = result
# STEP 9: Set Analysis - Subjects Passed by Students
passed_subjects = set()
for student_id, details in student_records.items():
    for i in range(3):
        if details["marks"][i] >= 40:
            passed_subjects.add(subjects[i])
print("\nSubjects Passed by At Least One Student:", passed_subjects)
# Select Two Students for Set Operations
first_id = input("\nEnter First Student ID: ")
second_id = input("Enter Second Student ID: ")
if first_id in student_records and second_id in student_records:
    first_passed = set()
    second_passed = set()
    for i in range(3):
        if student_records[first_id]["marks"][i] >= 40:
            first_passed.add(subjects[i])
        if student_records[second_id]["marks"][i] >= 40:
            second_passed.add(subjects[i])
    print("\nFirst Student Passed Subjects:", first_passed)
    print("Second Student Passed Subjects:", second_passed)
    print("Union:",
          first_passed.union(second_passed))
    print("Intersection:",
          first_passed.intersection(second_passed))
    print("Difference (First - Second):",
          first_passed.difference(second_passed))
    print("Symmetric Difference:",
          first_passed.symmetric_difference(second_passed))
else:
    print("One or Both Student IDs Not Found!")
# STEP 10: Class Performance Summary
if len(student_records) > 0:
    total_class_average = 0
    highest_average = 0
    lowest_average = 100
    for student_id, details in student_records.items():
        total_class_average += details["average"]
        if details["average"] > highest_average:
            highest_average = details["average"]
        if details["average"] < lowest_average:
            lowest_average = details["average"]
    class_average = total_class_average / len(student_records)
    print("\n========== CLASS PERFORMANCE SUMMARY ==========")
    print("Total Students:", len(student_records))
    print("Class Average:", class_average)
    print("Highest Average:", highest_average)
    print("Lowest Average:", lowest_average)
else:
    print("\nNo student records available to calculate class performance.")