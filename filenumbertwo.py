import sys


from filenumberone import hello 

if len(sys.argv) == 2 :
    hello(sys.argv[1])     

# This helps us in avoiding the use of function again and again instead of wrinting another one.