import sys
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from datetime import datetime
  
POST_LOGIN_URL = 'https://moodle.iitb.ac.in/login/index.php'
REQUEST_URL = 'https://moodle.iitb.ac.in/my/'


user = sys.argv[1]
password = sys.argv[2]
ta_name = sys.argv[3]

with requests.Session() as s:
    d = []
    site = s.get(POST_LOGIN_URL)
    bs_content = BeautifulSoup(site.content, "html5lib")
    token = bs_content.find("input", {"name":"logintoken"})["value"]
    login_data = {"username":user,"password":password, "logintoken":token}
    s.post(POST_LOGIN_URL,login_data)
    home_page = s.get(REQUEST_URL)
    soup = BeautifulSoup(home_page.content,'html5lib')  
    links = soup.find_all('a',class_='list-group-item list-group-item-action')
    course_link = None
    for rows in links:
        if rows.text.strip() == "CS 251-2022-1":
            course_link = rows
    if course_link != None:
        link = course_link['href']
        course_page = s.get(link)
        soup = BeautifulSoup(course_page.content,'html5lib') 
        spans = soup.find_all('span',class_='instancename') 
        for span in spans:
            if "Announcements" in span.text.strip():
                announce_span = span
        announce_class = announce_span.parent
        announce_link = announce_class['href']
        announce_page = s.get(announce_link)
        soup = BeautifulSoup(announce_page.content,'html5lib') 
        trs = soup.find_all('tr',class_='discussion subscribed')
        for tr in trs:
            th = tr.find('th')
            a_link = th.find('a',class_='w-100 h-100 d-block')['href']
            page = s.get(a_link)
            soup = BeautifulSoup(page.content,'html5lib')
            divs = soup.find_all('div',class_='d-flex flex-column w-100')
            for div in divs:
                announcement = div.find('h3').text.strip()
                TA = div.find('a').text.strip()
                if TA == ta_name:
                    date = div.find('time').text.strip()
                    date_time = date.split(', ')
                    date_time.append(announcement)
                    d.append(date_time)
    f = open('announcements.txt','w')
    for item in sorted(d,key = lambda item:(datetime.strptime(item[1], '%d %B %Y'),datetime.strptime(item[2], '%I:%M %p'))):
        f.write(f"{item[0]}, {item[1]}, {item[2]}; {item[3]}\n")
    f.close()
