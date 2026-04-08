# Name: Cassiddy Ginoza
# Date: Apr. 7, 2026

# parse itm website to find the people (faculty, grads, lecturers)

import urllib.request
from bs4 import BeautifulSoup

itm_url = "https://shidler.hawaii.edu/itm/people"

itm_html = urllib.request.urlopen(itm_url)
html_to_parse = BeautifulSoup(itm_html, "html.parser")

print(html_to_parse.prettify())
print(type(html_to_parse))

'''# find and print just the names of the faculty members
list_of_faculty = html_to_parse.find_all("h2", class_="title")

itm_faculty = [] # creating empty list to store the names of the faculty members
for person in list_of_faculty:
    itm_faculty.append(person.text.strip()) # appending the names of the faculty members to the list
    print(person.text.strip()) 

# people appear twice because listed as both faculty and lecturers, so we need to remove duplicates

print("Faculty members found: ", len(itm_faculty)) # print the number of faculty members found
unique_faculty = set(itm_faculty) # using set to remove duplicates
print("Unique faculty members found: ", len(unique_faculty)) # print the number of unique faculty members found'''
