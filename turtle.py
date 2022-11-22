"""do_research finds the number of months
    it will take 
    for a researcher to run out of rabbit cages."""
import csv

def do_research(cages, adults, babies):
    
    month = 1
    adult = adults
    baby = babies
    total = adult + baby
    temp = [month, ' '+str(adult), ' '+str(baby), ' '+str(total)]

    with open('rabbits.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        _header = ["# Table of rabbit pairs"]
        _column = ['Month', ' Adults', ' Babies', ' Total']

        writer.writerow(_header)
        writer.writerow(_column)
        writer.writerow(temp)

        while total < cages:
            month += 1 
            baby = adult
            adult = total
            total = adult + baby
    
            writer.writerow([str(month),' '+str(adult),' '+str(baby), ' '+str(total)])

            
        writer.writerow([f'# Cages will run out in month {month}'])
       