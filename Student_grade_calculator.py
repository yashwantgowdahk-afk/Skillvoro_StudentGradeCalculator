# Student Grade Calculator
# Skillvoro Internship Program 2026

def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    print("=" * 45)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 45)

    student_name = input("Enter student name: ")

    subjects = [
        "Subject 1",
        "Subject 2",
        "Subject 3",
        "Subject 4",
        "Subject 5"
    ]

    marks = []

    for subject in subjects:
        mark = get_marks(subject)
        marks.append(mark)

    total_marks = sum(marks)
    percentage = total_marks / 5
    grade = calculate_grade(percentage)

    print("\n" + "=" * 45)
    print("          STUDENT RESULT")
    print("=" * 45)

    print(f"Student Name : {student_name}")
    print(f"Total Marks  : {total_marks:.2f} / 500")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")

    print("=" * 45)


if __name__ == "__main__":
    main()