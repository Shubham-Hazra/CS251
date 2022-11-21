import json
import os
import shutil

def check_equality(file_path, student):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    val =  (data['name'] == student.get_name()) and (data['gender'] == student.get_gender()) \
        and (data['age'] == student.get_age()) and (data['cgpa'] == student.get_cgpa()) \
        and (data['home_town'] == student.get_home_town())

    return val

def evaluator_func():
    outs = []

    MAX_GRADE = 10
    with open('test_cases_q1/marks.json', 'r') as file:
        mark_data = json.load(file)
    with open('test_cases_q1/expected.json', 'r') as file:
        expected_class_data = json.load(file)

    test_grades = {test_code: 0 for test_code in mark_data.keys()}
    for test_code, test_grade in mark_data.items():
        expected_class = eval(expected_class_data[test_code])
        
        try:
            
            json_file_path = 'test_cases_q1/' + test_code + '.json'
            student = StudentBuilder.build_student_object(json_file_path)
            if isinstance(student, expected_class):
                if check_equality(json_file_path, student):
                    test_grades[test_code] = test_grade
            obt_data = {"name":student.get_name(),"gender":student.get_gender(), "age":student.get_age(), "cgpa":student.get_cgpa(), "home_town":student.get_home_town()}
            outs.append(obt_data)

        except Exception as exp:
            if isinstance(exp, expected_class): 
                test_grades[test_code] = test_grade
    
    total_grades = float((sum(list(test_grades.values()))) / len(test_grades)) * MAX_GRADE
    total_grades = round(total_grades, 2)
    return (total_grades,outs)

try:
    from exception import Lab5Exception
    from student import Student
    from q1 import StudentBuilder

    try:
        score,obt = evaluator_func()
        if score == 10:
            remarks = "Congrats!!! Your code passed all the test cases"
        else:
            remarks = "Your code failed for some test cases!"
    except:
        score = 0
        remarks = "Some issue with evaluation"
        obt = "Nil"
except:
    score = 0
    remarks = "All required files are not present"
    obt = "Nil"

with open('out.txt','w') as f:
    f.write("Score = " + str(score) + '\n')
    f.write("Remarks = " + str(remarks) + '\n')
    f.write("Obtained out = " + str(obt) + '\n')

if os.path.exists("__pycache__"):
    shutil.rmtree("__pycache__")

if os.path.exists("q1.pyc"):
    os.remove("q1.pyc")

if os.path.exists("student.pyc"):
    os.remove("student.pyc")

if os.path.exists("exception.pyc"):
    os.remove("exception.pyc")

if os.path.exists("q1_grader.pyc"):
    os.remove("q1_grader.pyc")

try:
    print(str(score),str(remarks))
except:
    pass