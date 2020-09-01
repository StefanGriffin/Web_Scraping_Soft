import csv
import datetime
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from collections import Counter
from stop_words import get_stop_words


def clean_word(word):
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace(";", "")
    word = word.replace(",", "")
    word = word.replace(".", "")
    return word

def clean_up_words(words):
    new_words = []
    pkg_stop_words = get_stop_words('en')
    print(pkg_stop_words)
    my_stop_words = ['the', 'is', 'and', 'themselves']
    for word in words:
        word = word.lower()
        if word == 'themselves':
            print(word)
        if word in my_stop_words or word in pkg_stop_words:
            pass
        else:
            cleaned_word = clean_word(word)
            new_words.append(cleaned_word)
    return new_words

def create_csv_path(csv_path):
     if not os.path.exists(csv_path):
        with open(csv_path, 'w') as csvfile:
            header_colums = ['word', 'count', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=header_colums)
            writer.writeheader()

saved_domain = {
    "tim.blog": "content-area"
}

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
    # print(body_.text)
    words = body_.text.split() # removing the stop words like the , and, etc
    # print(words)
    # print("Number of words is", len(words))
    clean_words = clean_up_words(words)
    word_counts = Counter(clean_words)
    print(word_counts.most_common(30))
    filename = domain.replace(".", "-") + '.csv'
    path = 'csv/' + filename
    create_csv_path(path)


   

    











    








