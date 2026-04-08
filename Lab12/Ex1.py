# Name: Cassiddy Ginoza
# Date: Apr. 7, 2026

import ssl
import urllib.request 
url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

ssl._create_default_https_context = ssl._create_unverified_context
# ssl is a security protocol that encrypts data transmitted over the internet.
# don't need for this example, but it's a common workaround for SSL certificate issues when making HTTPS requests in Python.

print("Opening URL: ", url)
web_page = urllib.request.urlopen(url)
print(web_page)

# iterate through each line in the web page searching for the <title> tag

for line in web_page:
    line = line.decode("utf-8") # decode the line from bytes to string
    if "<title>" in line:
        print(line.strip()) # print the line with leading and trailing whitespace removed