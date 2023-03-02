import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def main():
    URLs = ['https://emdz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions']
    keywords = ['engineer', 'software', "developer", "analyst"]

    for URL in URLs:
        # get the url, open it in a seperate chrome browser, then wait 5 seconds for it to load
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(URL)
        time.sleep(5)
        SCROLL_PAUSE_TIME = 5
        last_height = 0
        while True:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        # after it loads, use this specific browsers page for soup to search through
        page = browser.page_source
        soup = BeautifulSoup(page, "html.parser")
        results = soup.find(class_="app")
        # print(results)
        jobElements = results.find_all("li", class_="joblist-grid-item")
        # print(jobElements)

        for job in jobElements:
            title = job.find("h3").text.strip()
            location = job.find(
                "div", class_="job-locations icon-location-pin").text.strip()
            link = job.find("a")["href"]

            # check if any of the keywords are in the title
            if any(keyword in title.lower() for keyword in keywords):
                print(title)
                print(location)
                print(f"Apply here: {link}\n")


if __name__ == "__main__":
    main()
