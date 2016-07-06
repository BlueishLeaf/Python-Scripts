#Initial Variables
def calculator():
    value = int(input("Please enter credits amount:    "))
    division = int(input("How many people are involved in this division?:    "))
    equal_div = input("Should the credits be equally divided?:    ")

#If statements
    if equal_div in ["yes", "Yes", "yeah", "Yeah", "yee", "Yee"]:
        equal_dist_total = value / division
        total_string = str(equal_dist_total)
        print ("Each person receives " + equal_dist_total + " credits each.")
    elif equal_div in ["no", "No"]:
        for x in range(1, division+1):
            percentage = int(input("Percentage for person No." + '{}:    '.format(x)))
            print ("Person No." + '{}'.format(x) + "recieves " + str((value / 100) * percentage))
    else:
        print ("Not a valid answer!")
    calculator()

calculator()
