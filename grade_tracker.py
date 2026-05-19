# =========================================================
# ENGINEERING SGPA & GRADE TRACKER
# Created by Harry Fernando
# =========================================================

from tabulate import tabulate

# ---------------------------------------------------------
# Evaluation Components and Maximum Marks
# ---------------------------------------------------------

evaluation_scheme = {
    "TH ISE 1": 20,
    "TUT ISE 1": 20,
    "PRAC ISE 1": 20,
    "MSE": 30,
    "TH ISE 2": 20,
    "TUT ISE 2": 30,
    "PRAC ISE 2": 30,
    "ESE": 30
}


# ---------------------------------------------------------
# Grade Calculation Function
# ---------------------------------------------------------

def calculate_grade(percentage):

    if percentage >= 90:
        return 10
    elif percentage >= 85:
        return 9
    elif percentage >= 70:
        return 8
    elif percentage >= 60:
        return 7
    elif percentage >= 50:
        return 6
    elif percentage >= 45:
        return 5
    elif percentage >= 40:
        return 4
    else:
        return 0


# ---------------------------------------------------------
# Input Validation Function
# ---------------------------------------------------------

def get_marks(component, max_marks):

    while True:

        marks = input(f"{component} (Max {max_marks}) [-]: ")

        # Handle Not Applicable Case
        if marks.strip() == "-":
            return "-", 0, 0

        try:
            marks = float(marks)

            if 0 <= marks <= max_marks:
                return marks, marks, max_marks

            else:
                print(f"Invalid input! Enter marks between 0 and {max_marks}.")

        except:
            print("Invalid input! Please enter a number or '-'.")


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------

print("\n======================================================")
print("         ENGINEERING SGPA & GRADE TRACKER")
print("======================================================\n")

student_name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number  : ")

while True:

    try:
        number_of_subjects = int(input("\nEnter Number of Subjects : "))

        if number_of_subjects > 0:
            break

        else:
            print("Please enter a valid number.")

    except:
        print("Invalid input! Please enter a number.")


# ---------------------------------------------------------
# Variables for SGPA
# ---------------------------------------------------------

subject_records = []

total_grade_points = 0
total_credits = 0


# ---------------------------------------------------------
# Subject Loop
# ---------------------------------------------------------

for subject_index in range(number_of_subjects):

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"              SUBJECT {subject_index + 1}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    subject_name = input("Subject Name : ")

    while True:

        try:
            credits = int(input("Credits      : "))

            if credits > 0:
                break

            else:
                print("Credits must be positive.")

        except:
            print("Invalid input! Please enter a number.")

    print("\nEnter obtained marks:")
    print("(Use '-' if component is not applicable)\n")

    obtained_total = 0
    maximum_total = 0

    # -----------------------------------------------------
    # Component Loop
    # -----------------------------------------------------

    for component, max_marks in evaluation_scheme.items():

        entered_value, obtained_marks, max_component_marks = get_marks(component, max_marks)

        obtained_total += obtained_marks
        maximum_total += max_component_marks

    # -----------------------------------------------------
    # Percentage and Grade
    # -----------------------------------------------------

    percentage = (obtained_total / maximum_total) * 100

    grade = calculate_grade(percentage)

    grade_points = grade * credits

    total_grade_points += grade_points
    total_credits += credits

    result = "Pass" if grade != 0 else "Fail"

    # -----------------------------------------------------
    # Store Data
    # -----------------------------------------------------

    subject_records.append([
        subject_name,
        f"{obtained_total:.2f}",
        f"{maximum_total}",
        f"{percentage:.2f}%",
        grade,
        credits,
        grade_points,
        result
    ])


# ---------------------------------------------------------
# Final SGPA Calculation
# ---------------------------------------------------------

sgpa = total_grade_points / total_credits


# ---------------------------------------------------------
# Final Report
# ---------------------------------------------------------

print("\n\n======================================================")
print("                    FINAL REPORT")
print("======================================================\n")

print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")

headers = [
    "Subject",
    "Obtained",
    "Max Marks",
    "Percentage",
    "Grade",
    "Credits",
    "Grade x Credits",
    "Result"
]

print("\n")

print(
    tabulate(
        subject_records,
        headers=headers,
        tablefmt="fancy_grid"
    )
)

print("\n------------------------------------------------------")
print(f"TOTAL CREDITS      : {total_credits}")
print(f"TOTAL GRADE POINTS : {total_grade_points}")
print(f"FINAL SGPA         : {sgpa:.2f}")
print("------------------------------------------------------")

print("\nThank you for using the Grade Tracker.\n")