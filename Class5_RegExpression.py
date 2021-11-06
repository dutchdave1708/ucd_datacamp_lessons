#importing the right packages
import requests as requests
import numpy as np
import re

print ('hello - here is the homework from class 5, including the corrections made')
#answer = re.findall(r"#excited", "I am so #excited to present this certificate!")
#print(answer)

#answer  = re.split(r"!","Nice place! We should come back!")
#print(answer)

#answer = re.sub(r"red","blue", "I have a red car")
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

answer = re.findall(r"@\w*", "This is @John$")  #needs to be lower case w
print(answer)

answer = re.findall(r"\d+-\d+", "start: 4-3, registration: 10-04")
print(answer)

answer = re.findall(r"\+\d{3}-\d{5}\s\d{4}", "+353-98765 4321" )
print(answer)