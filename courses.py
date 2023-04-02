import csv
from requests_html import HTMLSession



def course_scrapper(course_code):
    session = HTMLSession()

    page = session.get(f"https://uwflow.com/course/{course_code}")

    page.html.render()

    div_element = page.html.find('div.sc-ptDSg eYGQDi', first=True)
    print(div_element)


course_scrapper('cs246')