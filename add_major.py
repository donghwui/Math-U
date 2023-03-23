from bs4 import BeautifulSoup
import requests

# prompts user to enter a link to the ugrad major requirements
link = input("Enter Link to Major Requirements: ")

page = requests.get(link)
soup = BeautifulSoup(page.text, "html.parser")

requirements = soup.find("span", attrs="MainContent").ul
major_name = soup.find("span", class_="pageTitle").text

# ensures no slashes are in the majors name
major_name = major_name.replace('/', ' ')

# check if any pre-requirements are needed for this major
include_table2 = False    # refers to MATH table 2 requirements list

pre_requirements = soup.find("span", attrs="MainContent").p.text

if "Table 2" in pre_requirements:
  include_table2 = True


# creates file and stores course requirements
with open(f"majors_data/{major_name}.txt", "w") as file:
  if (include_table2 == True):
    # indicates requirements from table 2 need to be added
    file.write("! include table 2\n")  
  file.write(requirements.text)