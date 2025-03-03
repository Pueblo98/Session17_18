import pytest
from First_class import Student

try:
    bob = Student(13)  
except TypeError as e:
    print(e)
    
try:
    bob = studen("bob")
    bob.enroll("science")
    bob.enroll("polysci")
    if len(bob.get_courses) != 2:
        raise KeyError("classes are not bieng cumulated")
except KeyError as e:
    print(e)