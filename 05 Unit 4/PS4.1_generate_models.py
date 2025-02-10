import numpy as np

def generate_models(x, y, degs):
  
    # TODO
    return [np.polyfit(x, y, z) for z in degs]
    
