

import re
# IN this, we will be using re sustitute moduloe in order to make sure that the there is a replacement of patterns in our program.
# We can mnake use of dot plus(.+) in order to make sure that our input gets added in our program.  
url = input("URL: ").strip()
# We just added parrallel lines in order to make our program more optional in the application choices such as google.
matches = re.search("^(https?://)?(www\.)?(twitter|yahoo|google)\.(com|org|in)/(.+)$", url, re.IGNORECASE)  # It could be http or https. Thus for this, we will use ?  in front of s in order to provide such particular option. (.+) shows the username which will be included in the user input.
                                                               # In order to highlight the characters, we will be using peretntesis so that the syntax of ? applies to them. This will make things optional for us.
if matches :
    print(f"Username:", matches.group(5))    # We will be using the group syntax in order to extract the second characters under perethesis.
