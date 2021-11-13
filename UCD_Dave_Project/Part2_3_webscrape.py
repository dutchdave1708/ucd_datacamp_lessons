######## open a html page and read into a variable ############
# Import packages
from urllib.request import urlopen, Request
import re
from bs4 import BeautifulSoup

# Specify the url & package the request
url = "https://en.wikipedia.org/wiki/Pancake"
request = Request(url)
# Sends the request and save the response
response = urlopen(request)
# Extract & print the response: html_of_page
#html_of_page = response.read() # this returns value as bytes
# need to convert to string, so read the file in with a decode
html_of_page = response.read().decode('utf-8')

#print(html_of_page)
print(type(html_of_page))
# close the response
response.close()

#print(html_of_page)
# execute some regular expressions
# 0. start simple: find all Pannekoek and pancake
answer = re.findall(r"pannekoek", html_of_page)
print(answer)
answer = re.findall(r"pancake", html_of_page)
print(answer)

html_of_page_NL = html_of_page.replace('pancake','Mighty Dutch pannekoek').replace('pancakes','Mighty Dutch Pannekoeken')
#print(html_of_page_NL)

#1. replace pancake en pannekoek with Mighty Dutch Pannekoek
Dutch_Pancake = re.sub(r"pancake","Mighty Dutch pannekoek", html_of_page)
Dutch_Pancake = re.sub(r"pancakes","Mighty Dutch pannekoeken", Dutch_Pancake)
Dutch_Pancake = re.sub(r"Pancake","THE Mighty Dutch Pannekoek", Dutch_Pancake)
#print(Dutch_Pancake)

#3 Use BeautifulSoup to display updated text from html
Wikipedia_Pannekoek = BeautifulSoup(Dutch_Pancake, features="html.parser")
#print(Wikipedia_Pannekoek.get_text())

#4 extract title from another website
title_test = BeautifulSoup(urlopen("https://stackoverflow.com/questions/14694482/converting-html-to-text-with-python"), features="html.parser")
print('title of website is: ' + title_test.title.string)

# 4. Using regex to extract urls ending in .org



#regex = r'https(\w*)</title>'  #
#titleonpage = re.findall('https', html_of_page)
#print(titleonpage)

#answer  = re.split(r"!","Nice place! We should come back!")
#print(answer)

#answer = re.findall(r"User\d","The winners are:User9,UserN,User8")
#print(answer)

#answer = re.findall(r"User\D","The winners are:User9,UserN,User8")
#print(answer)

#answer = re.findall(r"User\w","The winners are:User9,UserN,User8")
#had to replace d with w from the slide text
#print(answer)

#answer = re.findall(r"\W\d","The price is:$1,$2,$3")
#had to replace " at the start, error copying from slide
#print(answer)

#answer = re.findall(r"Data\s{3}Science","This is Data   Science")
# added 3 spaces. use either \s\s\s or \s{3}
#print(answer)

#answer = re.sub(r"ice\Scream","ice cream","I like ice cream")
#print(answer)

#answer = re.findall(r"colou?r", "This is my color. Love this colour")  #change from capital Colour from slides
#print(answer)

#answer = re.findall(r"@\w*", "This is @John$")  #needs to be lower case w
#print(answer)

#answer = re.findall(r"\d+-\d+", "start: 4-3, registration: 10-04")
#print(answer)

#answer = re.findall(r"\+\d{3}-\d{5}\s\d{4}", "+353-98765 4321" )
#print(answer)
