import requests   # After successfully installing requests module of python, we will import it in order to get access data from web browser.

import sys  # We will import and make use of system module so that we can apply input from command line argument in the function.

if len(sys.argv) != 2 :
    sys.exit()

response = requests.get("http://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])  # We will assinging the variable  named response to use the url of the itunes and adding the command line argument into this. The API that we have used is contract.
                                                                                      # After we download the text file of the url in json text format. It is not necesarry.  

print(response.json())             # After we run our program, the python language will convert the json text format of the file into a dictionary.

# API contracts: A format is decided between user and API creater under which, whenever the user will use an input and will request the output from the creater. That output will be given in that particular format which was decided earlier.    