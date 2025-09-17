# A dictionary to hold the point values for each grade
grade_values = {
    "A": 4.000,
    "A-": 3.670,
    "B+": 3.330,
    "B": 3.000,
    "B-": 2.670,
    "C+": 2.330,
    "C": 2.000,
    "C-": 1.670,
    "D+": 1.330,
    "D": 1.000,
    "F": 0.000,
}

# Start the totals at zero before we loop
cumulative_points = 0.0
cumulative_credits = 0.0

# This loop will run forever until we 'break' out of it
while True:
    # Get the grade and credits from the user in separate steps
    letter_grade = input("Enter letter grade: ")
    letter_grade = letter_grade.upper()  # Convert to uppercase on a new line

    course_credits = input("Enter course credits: ")
    course_credits = float(course_credits)

    # Look up the grade's value using bracket notation
    point_value = grade_values[letter_grade]
    course_points = point_value * course_credits

    # Add the results for this course to the running totals
    cumulative_points = cumulative_points + course_points
    cumulative_credits = cumulative_credits + course_credits

    # Ask the user if they want to stop
    response = input("Add another course? (yes/no): ")
    if response == "no":
        break  # Exit the while loop

# Calculate the final GPA after the loop is done
if cumulative_credits > 0:
    final_gpa = cumulative_points / cumulative_credits
else:
    final_gpa = 0.0

# Print the final result for the user
print(f"Final GPA: {final_gpa:.3f}")