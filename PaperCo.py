import requests
from bs4 import BeautifulSoup

def main():
    URLs = ['https://boards.greenhouse.io/paper']
    keywords = ['engineer', 'software', 'developer']

    for URL in URLs:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id='main')
        # print(results.prettify())
        jobElements = results.find_all("div", class_="opening")
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

if __name__ == "__main__":
    main()
