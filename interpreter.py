# 

# Problem set
expression = input("Expression:") 
x,y,z = expression.split(" ")   # We will use the split function in order to split each whitespace between the variable.
A = float(x)
B = float(z)

if y == "+" :
    D = A + B
    print(D)
elif y == "-" :
    D = A - B
    print(D)

elif y == "*" :
    D = A*B
    print(D)
elif y == "/" :
    D = A/B
    print(D)
else :
    print("Error")   # An error will be shown if write anything other than the math signs between our float inputs.




