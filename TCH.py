import requests
from bs4 import BeautifulSoup

URLs = ['https://www.texaschildrenspeople.org/career_search/']
keywords = ['engineer', 'software']

for URL in URLs:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='data_wrapper')
    # print(results.prettify())
    jobElements = results.find_all("div", class_="dataTables_wrapper")
    # print(jobElements)

    for job in jobElements:
        title = job.find("a").text.strip()
        location = job.find("span", class_="location").text.strip()
        link = job.find("a")["href"]

        # check if any of the keywords are in the title
        if any(keyword in title.lower() for keyword in keywords):
            print(title)
            print(location)
            print(f"Apply here: {link}\n")