import csv
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
from pyppeteer import launch
import asyncio

PATH = '/opt/homebrew/bin/chromium'

async def get_session():
    browser = await launch(executable_path=PATH)
    session = HTMLSession(browser_args=['--no-sandbox', '--disable-setuid-sandbox'])
    session._browser = browser
    return session

async def course_scrapper(course_code):
    session = await get_session()
    page = session.get(f"https://uwflow.com/course/{course_code}")

    page.html.render()

    div_element = page.html.find('div.sc-ptDSg eYGQDi', first=True)
    print(div_element)
    await session.close()

async def main():
    await course_scrapper('cs246')

asyncio.run(main())