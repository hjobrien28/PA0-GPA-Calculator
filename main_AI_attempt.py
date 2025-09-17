grade_values = {
    "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67,
    "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33, "D": 1.0, "F": 0.0
}

cumulative_points = 0.0
cumulative_credits = 0.0

add_another = True
while add_another:
    letter_grade = input("Enter letter grade: ").upper()
    course_credits = float(input("Enter credit hours: "))

    point_value = grade_values[letter_grade]
    course_points = point_value * course_credits

    cumulative_points += course_points
    cumulative_credits += course_credits

    response = input("Add another course? (yes/no): ").lower()
    if response != "yes":
        add_another = False

if cumulative_credits > 0:
    final_gpa = cumulative_points / cumulative_credits
else:
    final_gpa = 0.0

print(f"Final GPA: {final_gpa:.2f}")