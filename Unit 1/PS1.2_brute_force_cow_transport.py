def brute_force_cow_transport(cows,limit=10):
    best_yet = None
    
    for partition in get_partitions(cows):
        
        if within_weight_limit(cows, partition, limit):
            
            if (best_yet == None) or len(partition) < len(best_yet): 
                best_yet = partition
                    
    return best_yet
        
def within_weight_limit(cows, partition, limit):
    for cow_set in partition:
        cow_set_weight = 0
        for cow in cow_set:
            cow_weight = cows[cow]
            cow_set_weight += cow_weight
        
        if cow_set_weight > limit:
            return False
        
    return True
   
