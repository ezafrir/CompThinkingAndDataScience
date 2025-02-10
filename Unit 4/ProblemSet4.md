**Problem 1: Curve Fitting**

Implement the generate_models function.
x and y are two lists corresponding to the x-coordinates and y-coordinates of the data samples (or data points); for example, if you have N data points, x = [x1 , x2 , ..., xN ] and y = [y1 , y2 , ..., yN ], where x_i and y_i are the x and y coordinate of the i-th data points. In this problem set, each x coordinate is an integer and corresponds to the year of a sample (e.g., 1997); each corresponding y coordinate is a float and represents the temperature observation (will be computed in multiple ways) of that year in Celsius. This representation will be used throughout the entire problem set.
degs is a list of integers indicating the degree of each regression model that we want to create. For each model, this function should fit the data (x,y) to a polynomial curve of that degree.
This function should return a list of models. A model is the numpy 1d array of the coefficients of the fitting polynomial curve. Each returned model should be in the same order as their corresponding integer in degs.

**Problem 2: R^2**

After we create some regression models, we also want to be able to evaluate our models to figure out how well each model represents our data, and tell good models from poorly fitting ones. One way to evaluate how well the model describes the data is computing the model's R^2 value. R^2 provides a measure of how well the total variation of samples is explained by the model.
Implement the function r_squared. This function will take in:
list, y, that represents the y-coordinates of the original data samples
estimated, which is a corresponding list of y-coordinates estimated from the regression model
This function should return the computed R^2 value. You can compute R^2 as follows, where  is the estimated y value for the i-th data point (i.e. predicted by the regression),  is the y value for the ith data point, and  is the mean of the original data samples.
![image](https://github.com/user-attachments/assets/14d1af83-05be-41a0-aca3-b7725290f682)
