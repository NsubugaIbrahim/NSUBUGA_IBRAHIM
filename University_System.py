class Person:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

class Student(Person):
    def __init__(self, Name, Age, Student_Number, Registration_Number, Programme, Year_Of_Study):
        super().__init__(Name, Age)
        self.Student_Number = Student_Number
        self.Registration_Number = Registration_Number
        self.Programme = Programme
        self.Year_Of_Study = Year_Of_Study
    
    def Display_Student_Info(self):
        print(f"Name: {self.Name}")
        print(f"Student Number {self.Student_Number}")
        print(f"Registration Number: {self.Registration_Number}")
        print(f"Programme: {self.Programme}")   
        print(f"Year of Study: {self.Year_Of_Study}")
        
class Lecturer(Person):
    def __init__(self, Name, Age, Staff_ID, College):
        super().__init__(Name, Age)
        self.Staff_ID = Staff_ID
        self.College = College
        
    def Display_Lecturer_Info(self):
        print(f"Name: {self.Name}")
        print(f"Staff ID: {self.Staff_ID}")
        print(f"College: {self.College}")

student = Student("Nsubuga Ibrahim", 22, "23/U", "23007", "BSSE", "II")
Lecturer = Lecturer("Dr. Jeff", 30, "L1234", "COCIS")

student.Display_Student_Info()
Lecturer.Display_Lecturer_Info()

     