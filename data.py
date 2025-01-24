import random
import json

try:
    # Generating sample data for 100 students
    student_data = {}
    for i in range(1, 101):
        student_id = f"{i:03}"  # Roll number format "001", "002", ..., "100"
        attendance = random.randint(70, 100)  # Random attendance percentage
        CA = random.randint(0, 30)  # Continuous Assessment marks
        MD = random.randint(0, 30)  # Mid Semester marks
        ESE = random.randint(0, 40)  # End Semester marks
        total_marks = CA + MD + ESE
        total_grade = "A" if total_marks >= 70 else "B" if total_marks >= 50 else "C"
        previous_grade = random.choice(["A", "B", "C"])  # Random previous grade

        student_data[student_id] = {
            "attendance": attendance,
            "CA": CA,
            "MD": MD,
            "ESE": ESE,
            "total_marks": total_marks,
            "Total_Grade": total_grade,
            "Previous_Grade": previous_grade
        }

    # Save the data to a file for later use
    with open('student_data.json', 'w') as f:
        json.dump(student_data, f)
    print("Student data generated successfully and saved to student_data.json.")

except Exception as e:
    print(f"An error occurred: {e}")