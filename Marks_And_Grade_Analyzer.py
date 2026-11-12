
students = {}

while True:

    print("\n===== MARKS AND GRADE ANALYZER =====")
    print("1. Add Student Result")
    print("2. Search Student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

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

        
        students[name.lower()] = {
            "subjects": subject_names,
            "marks": marks,
            "total": total,
            "percentage": percentage,
            "highest": highest,
            "lowest": lowest,
            "grade": grade,
            "result": result
        }

        print("\nStudent result saved successfully!")

    elif choice == "2":

        search_name = input("Enter student name to search: ")

        if search_name.lower() in students:

            student = students[search_name.lower()]

            print("\n===== STUDENT RESULT =====")
            print("Student Name:", search_name)

            print("\nSubjects and Marks:")

            for i in range(len(student["subjects"])):
                print(student["subjects"][i], ":", student["marks"][i])

            print("\nTotal Marks:", student["total"])
            print("Percentage:", student["percentage"], "%")
            print("Highest Marks:", student["highest"])
            print("Lowest Marks:", student["lowest"])
            print("Grade:", student["grade"])
            print("Result:", student["result"])

        else:
            print("Student not found!")

    elif choice == "3":
        print("Thank you for using Marks and Grade Analyzer!")
        break

    else:
        print("Invalid choice! Please try again.")