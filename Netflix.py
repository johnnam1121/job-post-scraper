import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

URL = ['https://jobs.netflix.com/search?page=4&location=Remote%2C%20United%20States',
       'https://jobs.netflix.com/search?page=3&location=Remote%2C%20United%20States',
       'https://jobs.netflix.com/search?page=2&location=Remote%2C%20United%20States',
       'https://jobs.netflix.com/search?location=Remote%2C%20United%20States']
keywords = ['engineer', 'software', 'developer']

for url in range(0, 3):
    browser = webdriver.Chrome()
    browser.get(URL[url])
    time.sleep(5)
    page = browser.page_source
    soup = BeautifulSoup(page, "html.parser")
    results = soup.find(id='__next')

    # print(results.prettify())
    jobElements = results.find_all("section", class_="css-gf7hb5 e1rpdjew3")
    # print(jobElements)

    for job in jobElements:
        title = job.find("h4").text.strip()
        location = job.find("span", class_="css-ipl420 e13jx43x2").text.strip()
        link = job.find("a")["href"]

        # check if any of the keywords are in the title
        if any(keyword in title.lower() for keyword in keywords):
            print(title)
            print(location)
            print(f"Apply here: {link}\n")
