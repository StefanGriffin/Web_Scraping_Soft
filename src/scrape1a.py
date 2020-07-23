import requests
from bs4 import BeautifulSoup

my_url = input("Please enter the URL:   ")

print("Grabbing...", my_url)

response = requests.get(my_url)
print("Status is:  ", response.status_code)  # 200, 404, 500
if response.status_code != 200:
    print("You cannot scrape!", response.status_code)
else:
    print("Scraping...")
    print(response.text)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    









