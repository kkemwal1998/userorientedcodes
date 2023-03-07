

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    A = d.replace("$"," ")
    F = float(A)
    return F 
    
         


def percent_to_float(p):
    
    O = p.replace("%", " ")
    W = float(O)

    return W/100





main()