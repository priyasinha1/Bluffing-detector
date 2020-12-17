# Bluffing-detector
Bluffing detector using polynomial linear regression, SVR Model and decision tree regression.

# Polynomial Regression
![](flow-chart.png)
Polynomial regression that uses polynomials is still linear in the parameters. This is because you build the equation by only adding the terms together. So, the performance metrics like R-squared (R²-coefficient of determination) are still valid for polynomial regression. Do not get confused polynomial regression with non-linear regression where R² is not valid.
High degrees can cause overfitting. The problem of overfitting is a condition where a statistical model begins to describe the random error in the data rather than the relationships between variables. In overfitting, the model fits training data very well but fails to generalize for new input data which are not in our dataset.
Lower degrees can cause underfitting. In underfitting, the model does not fit training data very well and also the new data.
When we set the value for the degree hyperparameter, we should always try to avoid both overfitting and underfitting conditions
