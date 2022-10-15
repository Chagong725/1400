
def do_research(cages, adults, babies):
    total = adults + babies
    month = 1
    while total < cages:
        babies = adults
        adults = total
        total = babies + adults
        month += 1
    with open('rabbits.csv','w',newline='')as csvfile:
        print("# Table of rabbit pairs", file=csvfile)

.do_research(500, 1, 0)
