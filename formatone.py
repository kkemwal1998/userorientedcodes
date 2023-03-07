

# In this, we will be dealing the with the formating of user input data. 
# In the  programme, we will be using group() syntax in order to index the characters that we have highlighted in our perinthesis.
# If we write our input as (kemwal, kanishk), then our output will be "hello kanishk kemwal". If we give our user input as (kanishk kemwal), then the matches pattenr will not be applied and will gove our output as "hello kanishk kemwal".
import re
name = input("What's your name ?").strip()

matches = re.search("^(.+), (.+)$", name)

if matches :
    name = matches.group(2)+ " " + matches.group(1)

print (f"hello, {name}")

# But because we have put a space between our pattern, thus if we type our user input as (kemwal,kanishk). We will not be able to get our expected output and will have to deal with the problem of space in our pattern.