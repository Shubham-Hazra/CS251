import imp
import json
from student import Student
from exception import Lab5Exception

class StudentBuilder:
    r"""
        You are expected to define a static method
        by the name build_student_object. It should take in 
        path to a json file and read the contents of the file.

        You are also expected to validate the contents read from 
        the JSON file and raise Exception accordingly
    """
    @staticmethod
    def build_student_object(filepath):
        f = open(filepath)
        data = json.load(f)
        for key,value in data.items():
            if(key=="name"):
                name = value
            elif(key=="gender"):
                gender = value
            elif(key=="age"):
                age = value
            elif(key=="cgpa"):
                cgpa = value
            elif(key=="home_town"):
                home_town = value
            else:
                continue
        f.close()
        if(not isinstance(age,int)):
            raise Lab5Exception("Age is not an integer")
        if(not (isinstance(cgpa,float) or isinstance(cgpa,int))):
            raise Lab5Exception("CGPA is not an integer or a float")
        if(not isinstance(name,str)):
            raise Lab5Exception("Name is not a string")
        if(not isinstance(gender,str)):
            raise Lab5Exception("Gender is not a string")
        if(not isinstance(home_town,str)):
            raise Lab5Exception("Home Town is not a string")
        if(age<0 or age>35):
            raise Lab5Exception("Age not between 0 and 35")
        if(cgpa<0 or cgpa>10):
            raise Lab5Exception("CGPA not between 0 and 10")
        if(not (gender=='Male' or gender=='Female' or gender=='Non-Binary' or gender=='Prefer Not To Say')):
            raise Lab5Exception("Gender not valid")
        def __new__(Student):
            if not hasattr(Student, 'instance'):
                Student.instance = super(Student, Student).__new__(Student)
            return Student.instance
        return Student(name,age,cgpa,gender,home_town)