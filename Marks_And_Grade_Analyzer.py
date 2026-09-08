print("MARKS AND GRADE ANALYZER")
name=input("Enter student name:")
subjects=int(input("Enter number of subjects:"))
marks=[]
for i in range(subjects):
    mark = float(input(f"Enter marks for subjects{i+1}:"))
    marks.append(mark)
total = sum(marks)
percentage = total/subjects
highest=max(marks)
lowest=min(marks)
if percentage >=90:
    grade = "A+"
elif percentage>=80:
    grade="A"
elif percentage>=70:
    grade="B"
elif percentage>=60:
    grade="C"
elif percentage>=50:
    grade="D"
else:
    grade="F"
if percentage>=50:
    result="Pass"
else:
    result="Fail"
print("\n====RESULT====")
print("Student Name:",name)
print("Total Marks:",total)
print("Percentage:",percentage,"%")
print("Highest Marks:",highest)
print("Lowest Marks:",lowest)
print("Grade",grade)
print("Result",result)
print("\nTHANK YOU FOR USING MARKS AND GRADE ANALYZER")
