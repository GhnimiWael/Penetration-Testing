__author__= "Wael Ghnimi"
__date__  = "May, 13,2021"

import requests

f = open("tesla.txt",'r')   # Change list_of_links by your urls

links = f.readlines()
http = "http://"
https = "https://"
urls = []

for link in links:
    link_pure = link.rstrip()
    link = http + link_pure     # To check the http
    link_2 = https + link_pure  # To check the https
    urls.append(link)
    urls.append(link_2)
       

for url in urls:
    try:
        request_response = requests.head(url)
        status_code = request_response.status_code
        if status_code != 400 \
            and status_code != 401 \
            and status_code != 503\
            and status_code != 405    :
            print(url,status_code)
    except requests.exceptions.ConnectionError:
        pass