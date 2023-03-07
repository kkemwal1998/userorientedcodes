

# In this, we will be dealing the with the formating of user input data. 
# In the  programme, we will be using group() syntax in order to index the characters that we have highlighted in our perinthesis.
# If we write our input as (kemwal, kanishk), then our output will be "hello kanishk kemwal". If we give our user input as (kanishk kemwal), then the matches pattenr will not be applied and will gove our output as "hello kanishk kemwal".
import re
name = input("What's your name ?").strip()

matches = re.search("^(.+), ?(.+)$", name)  # In order to accomodate whitespace as well as no whitespace. We will be using syntax ? for the same.
                                            # In order to avoid many whitespaces at a time, we will use * to avoid in place of ? . Eg: if we write our user input as (kemwal,     kanishk) , * syntax will help in getting our output as "hello kanishk kemwal" .
if matches :
    name = matches.group(2)+ " " + matches.group(1)

print (f"hello, {name}")
