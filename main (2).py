class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"{self.name} ({self.roll_number}) - CGPA: {self.cgpa}"

def sort_students(student_list):
    # Sort the student list in descending order of CGPA using a lambda function
    student_list.sort(key=lambda x: x.cgpa, reverse=True)

def main():
    # Create a list of student objects
    students = [
        Student("Alice", "A001", 3.8),
        Student("Bob", "B002", 3.9),
        Student("Charlie", "C003", 3.5),
        Student("David", "D004", 3.7),
        Student("Eve", "E005", 3.6),
    ]

    # Call the sort_students function to sort the students
    sort_students(students)

    # Print the sorted list of students
    print("Sorted List of Students:")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()