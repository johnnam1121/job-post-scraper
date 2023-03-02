import requests
from bs4 import BeautifulSoup
import re

URL = ['https://realpython.github.io/fake-jobs/',
       'https://realpython.github.io/fake-jobs/']

for url in range(0, 2):
    page = requests.get(URL[url])

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='ResultsContainer')
    # print(results.prettify())
    jobElements = results.find_all("div", class_="card-content")

    # for job in jobElements:
    #     # print(job, end="\n"*2)
    #     title = job.find("h2", class_="title")
    #     company = job.find("h3", class_="company")
    #     location = job.find("p", class_="location")
    #     print(title.text.strip())
    #     print(company.text.strip())
    #     print(location.text.strip())
    # "h2", string=lambda text: "python" in text.lower()

    keywords = ['python', 'energy']
    python_jobs = results.find_all(
        'h2', string=lambda string: any(keyword in string.lower() for keyword in keywords)
    )
    # print(python_jobs)

    python_jobs_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    for job in python_jobs_elements:
        # print(job, end="\n"*2)
        title = job.find("h2", class_="title")
        company = job.find("h3", class_="company")
        location = job.find("p", class_="location")
        links = job.find_all("a")
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        for link in links:
            link_url = link["href"]
            print(f"Apply here: {link_url}\n")
