def main():
    '''
    Program starts here.
    '''
    try:
        # (1) replace pass with your code
        #input variables
        
        # This asks how many crew members there are.
        print("How many reavers are on the ship? (Including Yondu & Peter)")
        reavers = int(input(""))
        print(f"You have entered {reavers} reavers.")
        
        # This asks how much money they enter the port with.
        print("What is the plunder when the reavers enter the port?")
        units = int(input(""))
        print(f"You have entered {units} units.")
        
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    # (2) replace pass with your code
    # Total amount of units after the crew goes out to celebrate
    post_lotus_total = units-(3*(reavers-2))

    # Yondus initial share
    yondus_share = post_lotus_total * .13
    yondus_share = int(yondus_share)

    # The total amount remaining after yondu takes his intitial share
    plunder = post_lotus_total - yondus_share

    # Peters initial share
    peters_share = plunder * .11
    peters_share = int(peters_share)

    # The total amount remaining after peter takes his initial share
    plunder = plunder-peters_share

    # Crew members final share
    crews_share = plunder/reavers
    crews_share = int(crews_share)

    # Peters final share
    yondus_share += crews_share

    # Peters final share
    peters_share += crews_share

    # The total amount given to the rbf
    rbf = plunder-(crews_share*reavers)
    #  - (10*20)

    # Prints the results
    print("Yondu's share: " + str(yondus_share))
    print("Peter's share: " + str(peters_share))
    print("Crew: " + str(crews_share))
    print("RBF: " + str(rbf))

if __name__ == "__main__":
    main()
    