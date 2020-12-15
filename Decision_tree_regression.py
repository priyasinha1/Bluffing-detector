#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


dataset = pd.read_csv('position_salaries.csv')


# In[3]:


dataset.head()


# In[4]:


X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values


# In[6]:


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X,Y)


# In[9]:


Y_pred = regressor.predict([[6.5]])
print(Y_pred)


# In[13]:



plt.scatter(X,Y, color = 'red')
plt.plot(X,regressor.predict(X) , color = 'blue')
plt.title("Decision Tree")
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.rcParams["figure.figsize"]=20,20
plt.show()


# In[15]:


X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X,Y, color = 'red')
plt.plot(X_grid,regressor.predict(X_grid), color = 'blue')
plt.title("Decision Tree")
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.rcParams["figure.figsize"]=20,20
plt.show()


# In[ ]:




