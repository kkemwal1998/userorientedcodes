


import csv



with open('911.csv') as data :
        
    A = csv.reader(data)

    count = 0

    for column in data :
        print(column)


        
            
