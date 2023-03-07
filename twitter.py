
import re
# The main objective of our program is to extract the username from the URL.
# IN this, we will be using re sustitute moduloe in order to make sure that the there is a replacement of patterns in our program.
url = input("URL: ").strip()
# We just added parrallel lines in order to make our program more optional in the application choices such as google.
username = re.sub("^(https?://)?(www\.)?(twitter|google|yahoo).com/", "", url)  # It could be http or https. Thus for this, we will use ?  in front of s in order to provide such particular option.
                                                               # In order to highlight the characters, we will be using peretntesis so that the syntax of ? applies to them. This will make things optional for us.
print(f"Username: {username}")


# The only problem with our programm is that it does not extract the username in additional user inputs.