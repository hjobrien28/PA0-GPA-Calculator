# Creates a dictionary to store letter grades as keys and their corresponding grade point values.
# A dictionary is a fast way to look up a value when you have its key.
grade_values = {
    "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67,
    "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33, "D": 1.0, "F": 0.0
}

# Creates a variable to keep a running total of all quality points, starting at 0.0.
cumulative_points = 0.0
# Creates a variable to keep a running total of all credit hours.
cumulative_credits = 0.0

# Starts an infinite 'while True' loop that will continue running until a 'break' statement is executed.
while True:
    # Prompts the user for a letter grade and uses .upper() to immediately convert the input to uppercase.
    # This makes the dictionary lookup case-insensitive.
    letter_grade = input("Enter letter grade: ").upper()

    # Prompts the user for credit hours and converts the input string into a floating-point number.
    course_credits = float(input("Enter credit hours: "))

    # Looks up the grade point value in the 'grade_values' dictionary using the user's 'letter_grade' as the key.
    point_value = grade_values[letter_grade]
    # Calculates the quality points for this specific course by multiplying the grade's value by the credits.
    course_points = point_value * course_credits

    # Adds the points from this course to the running total.
    cumulative_points += course_points
    # Adds the credits from this course to the running total.
    cumulative_credits += course_credits

    # Asks the user if they want to add another course and converts their response to lowercase.
    # This makes the check work with inputs like "YES", "Yes", or "yes".
    response = input("Add another course? (yes/no): ").lower()

    # Checks if the user's response is anything other than "yes".
    if response != "yes":
        # If the user did not type "yes", the 'break' statement exits the 'while' loop.
        break

# After the loop has ended, this check prevents an error from dividing by 0 if the user didn't enter any courses.
if cumulative_credits > 0:
    # Calculates the final GPA by dividing the total points by the total credits.
    final_gpa = cumulative_points / cumulative_credits
else:
    # If no credits were entered, the GPA is set to 0.0.
    final_gpa = 0.0

# Prints the final GPA to the user.
# The 'f' before the string lets you embed variables inside {}.
# The ':.2f' makes the number to round to two decimal places, which is the usual way to display GPAs.
print(f"Final GPA: {final_gpa:.2f}")