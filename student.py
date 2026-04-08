class Student:
    def __init__(self, _name, _roll_no, _marks):
        self.name = _name
        self.roll_no = _roll_no
        self.marks = _marks
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        else:
            return "C"
    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}, Grade: {self.get_grade()}"
if __name__ == "__main__":
    student1 = Student("Alice", 1, 85)
    student2 = Student("Bob", 2, 90)
    print(student1)
    print(student2)