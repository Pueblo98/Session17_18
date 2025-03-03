class Student:
    # Data members
    def __init__(self,name):
        if not isinstance(name,str):
            raise TypeError("needs to be a name") 
        self.name = name
        self.courses = []

    # Method
    def enroll(self,course):
        self.courses.append(course)
    
    # Prints courses
    def get_courses(self):
        print(self.courses)
           

