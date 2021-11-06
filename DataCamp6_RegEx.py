# Import the re module
import re



#  * zero or more times, + once or more, ? zero or once.
#  . is 'any character'  \. is a .  Note this for splitting strings for example
# split with re.split(), search(), findall(), sub(), match()
#  use .+ for "any character zero or more times
#  difference between * and + is...
# use ? for non-greedy matching.. it will be greedy search by default
#r"(love|like|enjoy).+?(movie|concert)\s(.+?)\.": .+? = "any characters until movie|concert
# the ? means 'non-greedy, so look for the first instance
#regex_negative = r"(hate|dislike|disapprove).+(?:movie|concert)\s(.+?)\."  --> (?:..) means match but dont capture the subsequent string

#Only if you use .search() and .match(), you can use .group() to retrieve the groups.


# Write the regex
regex = r'@robot\d\W'

#write an example string
sentiment_analysis = ('@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%')

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))

# Write a regex to match pattern separating sentences
# \W is non letter character
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)


# Import re module
import re

for tweet in sentiment_analysis:
	# Write regex to match http links and print out result
	print(re.findall(r"http\w+://\w*.\w*.\w*", tweet))

	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w*\d*", tweet))


    # EMAIL validation example
# Write a regex to match a valid email address
regex = r"[!#%&*$0-9a-zA-Z.]@\w+\.com"

for example in emails:
    # Match the regex to the string
    if re.findall(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))

# GROUPING
# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."
# print(regex_positive)
for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)

    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))

# print(regex_positive)

# MORE example code from DataCamp
# extract day month year and put into a dictionary with labels day, monht, year.
# then extract and put into a print
# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}
# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))