import requests

my_url = input("Please enter the URL:   ")

print("Grabbing...", my_url)

response = requests.get(my_url)

print("Status is:  ", response.status_code)  # 200, 404




