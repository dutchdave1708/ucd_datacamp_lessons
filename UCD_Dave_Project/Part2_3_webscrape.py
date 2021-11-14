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


#answer is a list


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
print('title of another website, just for trying, is: ' + title_test.title.string)

# 4. Using regex to extract urls ending in .org
#text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html_of_page)
print("The urls on the Wikipedia page are: ",urls)



