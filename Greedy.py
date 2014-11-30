# Christina Chan

def greedyAlgorithm():
    # SORT
    # get input from file, store in list of lists
    agencies = list()
    a = 0 # agency number
    with open("lab1input.txt") as f:
        for line in f:
            (d, v) = line.split()
            int(d) # convert from string to number
            int(v)
            agencies.append([v, d, a])
            a+=1

    # remove first line of input
    m = int(agencies[0][0]) # number funding agencies
    n = int(agencies[0][1]) # number days in contract
    agencies.pop(0)
    
    # sort according to first element (v) in descending order
    agencies_sorted = sorted(agencies, key=lambda x: int(x[0]), reverse=True)

    # ALGORITHM
    i = 0
    days_taken = [] # keeps record of days that we have a contract
    output = [0]*n # where we will store our output
    m-=1 # otherwise index (i) is out of range

    total_value = 0 # where we store total value from the selected agencies
    while (len(days_taken) <= n) and (i < m): # while we havnen't covered every day and while we haven't checked every agency
        date = int(agencies_sorted[i][1])
        if len(days_taken) <= n:
            while date > 0 and date <= n:
                if (date not in days_taken): # if angency's due date isn't already taken, we are done (add to solution)
                    output[int(date)-1] = "Day " + str(date) + ": Agency " + str(agencies_sorted[i][2]) + ": value " + str(agencies_sorted[i][0])
                    days_taken.append(date) # this day is now taken
                    total_value+= int(agencies_sorted[i][0]) # add the value to total
                    date = -1
                else:
                    date-=1 # check date before due date
        i+=1 # increment

    # OUTPUT
    output_f = open("output.txt", "w+")
    for o in output:
        print o # print our output
        print>>output_f, o

    print total_value # check total value
        
greedyAlgorithm()
