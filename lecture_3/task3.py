students = []

def add_student():
    name = input("Enter your name: ")
    if not name.isalpha():
        print("Enter a valid name")
        return
    for student in students:
        if student["name"] == name:
            print(f"Student with name {name} already exists")
            return
    students.append({"name": name, "grades": []})
    print(f"Student with name {name} created")


def add_grade():
    name = input("Enter your name: ")
    if not name.isalpha():
        print("Enter a valid name")
        return
    for student in students:
        if student["name"] == name:
            while True:
                grade_input = input("Enter your grade (0-10) or 'done': ")
                if grade_input == "done":
                    break
                try:
                    grade = int(grade_input)
                    if 0 <= grade <= 10:
                        student["grades"].append(grade)
                        print(f"Student with name {name} has grade {grade}")
                    else:
                        print("Grade must be between 0 and 10")
                except ValueError:
                    print("Invalid grade: please enter an integer (0-10)")
            return
    print("Student not found")

def print_students():
    if not students:
        print("No student found")
        return
    averages = []
    for student in students:
        grades = student["grades"]
        if grades:
            avg = sum(grades) / len(grades)
            print(f"{student['name']}: {grades}, average grade = {avg:.2f}")
            averages.append(avg)
        else:
            print(f"{student['name']}: {grades}, average grade = N/A")
    if averages:
        print(f"Max average: {max(averages):.2f}, Min average: {min(averages):.2f}, Overall average: {sum(averages)/len(averages):.2f}")
    else:
        print("No grades entered for any students")

def find_top():
    graded_students = [student for student in students if student["grades"]]
    if not graded_students:
        print("No top performer")
        return
    best = max(graded_students, key=lambda s: sum(s["grades"]) / len(s["grades"]))
    avg = sum(best["grades"]) / len(best["grades"])
    print(f"Top performer: {best['name']} with average grade {avg:.2f}")


def menu_students():
    actions = {
        1: add_student,
        2: add_grade,
        3: print_students,
        4: find_top
    }

    while True:
        try:
            print("Menu:")
            print("1. Add a new student")
            print("2. Add a grade for a student")
            print("3. Show all students")
            print("4. Find top performer")
            print("5. Exit")
            choice = int(input("Enter your choice(1-5): "))

            if choice == 5:
                print("Exit...")
                break

            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice")

        except ValueError:
            print("Ошибка! Введите корректное число.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    menu_students()
