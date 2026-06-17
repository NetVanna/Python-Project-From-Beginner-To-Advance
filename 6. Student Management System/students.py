class Student:
    """
    Student class

    Stores information about a student and provides methods
    to add, update, search, and display students.
    """

    # Class variable shared by all Student objects
    all_students = []

    def __init__(self, name, roll_number, marks):
        """
        Constructor

        Creates a new Student object.
        """

        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def update_marks(self, new_marks):
        """
        Instance Method

        Updates marks for a specific student.
        """

        self.marks = new_marks
        print(f"Marks for {self.name} updated to {self.marks}")

    def show_details(self):
        """
        Instance Method

        Displays details of a specific student.
        """

        print("\nStudent Details")
        print("----------------------")
        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        print(f"Marks       : {self.marks}")

    @classmethod
    def find_student_by_roll_number(cls, roll_number):
        """
        Class Method

        Searches for a student using roll number.
        Returns the student object if found.
        """

        for student in cls.all_students:
            if student.roll_number == roll_number:
                return student

        return None

    @classmethod
    def add_student(cls):
        """
        Class Method

        Creates and stores a new student.
        """

        name = input("Enter student name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        roll_number = input("Enter roll number: ").strip()

        # Check duplicate roll number
        if cls.find_student_by_roll_number(roll_number):
            print("Roll number already exists.")
            return

        try:
            marks = int(input("Enter marks (0-100): "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                return

        except ValueError:
            print("Marks must be a number.")
            return

        student = cls(name, roll_number, marks)

        cls.all_students.append(student)

        print(f"Student '{name}' added successfully.")

    @classmethod
    def update_student_marks(cls):
        """
        Class Method

        Finds a student and updates marks.
        """

        roll_number = input(
            "Enter roll number to update marks: "
        ).strip()

        student = cls.find_student_by_roll_number(roll_number)

        if not student:
            print("Student not found.")
            return

        try:
            new_marks = int(input("Enter new marks (0-100): "))

            if new_marks < 0 or new_marks > 100:
                print("Marks must be between 0 and 100.")
                return

        except ValueError:
            print("Marks must be a number.")
            return

        student.update_marks(new_marks)

    @classmethod
    def show_all_students(cls):
        """
        Class Method

        Displays all students.
        """

        if not cls.all_students:
            print("No students found.")
            return

        print("\n===== Student List =====")

        for student in cls.all_students:
            student.show_details()


def menu():
    """
    Main menu loop
    """

    while True:

        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Show All Students")
        print("4. Exit")

        try:
            choice = int(input("Enter your option (1-4): "))

        except ValueError:
            print("Please enter numbers only.")
            continue

        if choice == 1:
            Student.add_student()

        elif choice == 2:
            Student.update_student_marks()

        elif choice == 3:
            Student.show_all_students()

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    menu()