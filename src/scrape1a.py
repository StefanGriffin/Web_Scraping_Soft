import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


saved_domain = {
    "tim.blog": "content-area"
}

# if "tim.blog" in saved_domain:
#     div_class = saved_domain['tim.blog']
#     print(div_class)

my_url = input("Please enter the URL:   ")

print("Grabbing...", my_url)
domain = urlparse(my_url).netloc # domain name 
print("via domain", domain)

response = requests.get(my_url)
print("Status is:  ", response.status_code)  # 200, 404, 500

if response.status_code != 200:
    print("You cannot scrape!", response.status_code)
else:
    print("Scraping...")
    # print(response.text)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    if domain in saved_domain:
        div_class = saved_domain[domain]
        body_ = soup.find("div", {"class": div_class})
    else:
        body_ = soup.find("body")
    print(body_.text)




    









