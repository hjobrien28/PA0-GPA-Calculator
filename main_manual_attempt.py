grade_to_points = {
    "A": 4.000, "A-": 3.670, "B+": 3.330, "B": 3.000, "B-": 2.670,
    "C+": 2.330, "C": 2.000, "C-": 1.670, "D+": 1.330, "D": 1.000,
    "F": 0.000
}

total_quality_points = 0.0
total_credits = 0.0

keep_going = True
while keep_going:
    grade = input("Enter letter grade: ").upper()
    credits = float(input("Enter credits hours: "))

    points = grade_to_points.get(grade)
    quality_points = points * credits

    total_quality_points += quality_points
    total_credits += credits

    another_course = input("Add another course? (yes/no): ")
    if another_course.lower() != "yes":
        keep_going = False

if total_credits > 0:
    final_gpa = total_quality_points / total_credits
else:
    final_gpa = 0.0

print(f"Final GPA: {final_gpa:.3f}")