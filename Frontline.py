#not working why is this site so convoluted
import requests
from bs4 import BeautifulSoup

URLs = ['https://recruiting.ultipro.com/FRO1005FTECH/JobBoard/f325dba5-1721-42a7-bbc9-214a445fdeb2/?q=&o=postedDateDesc&w=&wc=&we=&wpst=']
keywords = ['engineer', 'software']

for URL in URLs:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='OpportunitiesContainer')
    # print(results.prettify())
    jobElements = results.find_all("div", class_="opportunity")
    print(jobElements)

    # for job in jobElements:
        # print(job, end="\n"*2)
        # title = job.find("h3")
        # location = job.find("span", class_="location").text.strip()
        # link = job.find("a")["href"]
        # print(title)
        # check if any of the keywords are in the title
        # if any(keyword in title.lower() for keyword in keywords):
        #     print(title)
            # print(location)
            # print(f"Apply here: {link}\n")