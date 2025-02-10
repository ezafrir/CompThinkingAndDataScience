**Problem 1: Curve Fitting**

Implement the generate_models function.
x and y are two lists corresponding to the x-coordinates and y-coordinates of the data samples (or data points); for example, if you have N data points, x = [x1 , x2 , ..., xN ] and y = [y1 , y2 , ..., yN ], where x_i and y_i are the x and y coordinate of the i-th data points. In this problem set, each x coordinate is an integer and corresponds to the year of a sample (e.g., 1997); each corresponding y coordinate is a float and represents the temperature observation (will be computed in multiple ways) of that year in Celsius. This representation will be used throughout the entire problem set.
degs is a list of integers indicating the degree of each regression model that we want to create. For each model, this function should fit the data (x,y) to a polynomial curve of that degree.
This function should return a list of models. A model is the numpy 1d array of the coefficients of the fitting polynomial curve. Each returned model should be in the same order as their corresponding integer in degs.
