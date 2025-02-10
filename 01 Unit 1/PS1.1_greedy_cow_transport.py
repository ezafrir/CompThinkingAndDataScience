def greedy_cow_transport(cows, limit=10):
    trips = []
    cowsCopy = cows.copy()
    sortedCows = sorted(cowsCopy.items(), key=lambda x: x[1], reverse = True)
    while sum(cowsCopy.values()) > 0:
        ship = []
        total = 0
        for cow, value in sortedCows:
            if cowsCopy[cow] != 0 and value + total <= limit:
                ship.append(cow)
                total += value
                cowsCopy[cow] = 0
        trips.append(ship)
    return trips
