import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('code', type=str)
args = parser.parse_args()
code = args.code
if(len(args.code) != 5):
    print("NOT FOUND")
elif(not(args.code[0:2] == 'CS')):
    print("NOT FOUND")
elif(not(args.code[2:].isnumeric())):
    print("NOT FOUND")
else:
    r = requests.get('https://www.cse.iitb.ac.in/academics/courses.php')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_= 'main-overlay')
    collapsible = s.find('ul', class_='collapsible expandable')
    lines = collapsible.find_all('tr')
    l = []
    for line in lines:
        if "Course No" in line.text:
            univ_list = line.text.split()
            institute = univ_list[3]
        else:
            course_list = line.text.split('\n')
            course = course_list[1]
            if(code in course_list[2]):
                l.append(f"{institute}:{course}".format(institute,course))
    i =0
    for item in sorted(l):
        if i == len(l)-1:
            print(sorted(l)[len(l)-1])
            continue
        print(item,end=';')
        i+=1
    if len(l) == 0:
        print("NOT FOUND")