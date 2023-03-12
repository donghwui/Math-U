from bs4 import BeautifulSoup
import requests

page = requests.get("https://ugradcalendar.uwaterloo.ca/page/MATH-Pure-Math-Degree-Requirements")

soup = BeautifulSoup(page.text, "html.parser")

maincontent = soup.find("span", attrs="MainContent")
courses = maincontent.findAll("a")

for course in courses:
  print(course.text)
  
