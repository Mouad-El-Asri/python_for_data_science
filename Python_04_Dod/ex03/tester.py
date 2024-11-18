from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

# Should return an Error
other_student = Student(name="Edward", surname="agle", id="toto")
print(other_student)
