import random


def drawing_without_replacement_sim(numTrials):
    counter = 0
    for i in range(numTrials):
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        picks = []
        for j in range(3):
            k = random.choice(bucket)
            picks.append(k)
            bucket.remove(k)
        if picks[0] == picks[1] == picks[2]:
            counter += 1
    return counter/numTrials                    
    
