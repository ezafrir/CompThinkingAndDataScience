import numpy as np

def r_squared(y, estimated):
  
    # TODO
    y, estimated = np.array(y), np.array(estimated)
    SEE = ((estimated - y)**2).sum()
    mMean = y.sum()/float(len(y))
    MV = ((mMean - y)**2).sum()
    return 1 - SEE/MV
