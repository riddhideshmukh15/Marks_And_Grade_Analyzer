print("MARKS AND GRADE ANALYZER")

name = input("Enter student name: ")
subjects = int(input("Enter number of subjects: "))

subject_names = []
marks = []
print("\nEnter Subject Names")
for i in range(subjects):
    subject = input("Enter subject name: ")
    subject_names.append(subject)

print("\nEnter Marks:")
for subject in subject_names:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)
total = sum(marks)
percentage = total / subjects
highest = max(marks)
lowest = min(marks)
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 50:
    result = "Pass"
else:
    result = "Fail"

print("\n==== RESULT ====")
print("Student Name:", name)

print("\nSubjects and Marks:")
for i in range(subjects):
    print(subject_names[i], ":", marks[i])

print("\nTotal Marks:", total)
print("Percentage:", percentage, "%")
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Grade:", grade)
print("Result:", result)

print("\nTHANK YOU FOR USING MARKS AND GRADE ANALYZER")