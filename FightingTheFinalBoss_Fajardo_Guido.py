import unittest

class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentRegistrationSystem:
    def __init__(self):
        self.students = {}

    # CREATE
    def create_student(self, student_id, name, age, major):
        if student_id in self.students:
            return False
        else:
            self.students[student_id] = Student(student_id, name, age, major)
            return True

    # READ
    def read_student(self, student_id):
        if student_id in self.students:
            return str(self.students[student_id])
        else:
            return None

    # READ ALL
    def read_all_students(self):
        return [str(student) for student in self.students.values()]

    # UPDATE
    def update_student(self, student_id, name=None, age=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
            return True
        return False

    # DELETE
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False

# Unit test for StudentRegistrationSystem
class TestStudentRegistrationSystem(unittest.TestCase):
    def setUp(self):
        """Initialize the StudentRegistrationSystem before each test."""
        self.srs = StudentRegistrationSystem()

    def test_create_student(self):
        """Test creating a new student."""
        # Test creating a new student
        self.assertTrue(self.srs.create_student(1, "Alice", 20, "Math"))
        # Test trying to create a student with an existing ID
        self.assertFalse(self.srs.create_student(1, "Bob", 21, "Science"))

    def test_read_student(self):
        """Test reading a student by ID."""
        # Add a student and read it back
        self.srs.create_student(1, "Alice", 20, "Math")
        self.assertEqual(self.srs.read_student(1), "ID: 1, Name: Alice, Age: 20, Major: Math")
        # Test reading a non-existing student
        self.assertIsNone(self.srs.read_student(2))

    def test_read_all_students(self):
        """Test reading all students."""
        # Test reading when no students are present
        self.assertEqual(self.srs.read_all_students(), [])
        # Add students and read all
        self.srs.create_student(1, "Alice", 20, "Math")
        self.srs.create_student(2, "Bob", 21, "Science")
        self.assertEqual(self.srs.read_all_students(), [
            "ID: 1, Name: Alice, Age: 20, Major: Math",
            "ID: 2, Name: Bob, Age: 21, Major: Science"
        ])

    def test_update_student(self):
        """Test updating a student's information."""
        # Add a student to update
        self.srs.create_student(1, "Alice", 20, "Math")
        # Update student name
        self.assertTrue(self.srs.update_student(1, name="Alicia"))
        self.assertEqual(self.srs.read_student(1), "ID: 1, Name: Alicia, Age: 20, Major: Math")
        # Update age and major
        self.assertTrue(self.srs.update_student(1, age=22, major="Physics"))
        self.assertEqual(self.srs.read_student(1), "ID: 1, Name: Alicia, Age: 22, Major: Physics")
        # Attempt to update a non-existing student
        self.assertFalse(self.srs.update_student(2, name="Charlie"))

    def test_delete_student(self):
        """Test deleting a student by ID."""
        # Add a student and delete it
        self.srs.create_student(1, "Alice", 20, "Math")
        self.assertTrue(self.srs.delete_student(1))
        # Confirm student is deleted
        self.assertIsNone(self.srs.read_student(1))
        # Attempt to delete a non-existing student
        self.assertFalse(self.srs.delete_student(2))

if __name__ == '__main__':
    unittest.main()
