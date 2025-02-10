def rabbitGrowth():
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    #pass
    for i in range(CURRENTRABBITPOP):
        if random.random() <= (1 - (CURRENTRABBITPOP/MAXRABBITPOP)):
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    #pass
    for i in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if random.random() <= (CURRENTRABBITPOP/MAXRABBITPOP):
                CURRENTRABBITPOP -= 1
                # fox reproducing
                if random.random() <= (1/3):
                    CURRENTFOXPOP += 1
        else:
            # fox dying
            if random.random() <= 0.1:
                CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    # TO DO
    #pass
    rabbits = []
    foxes = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    return rabbits, foxes
    
