#!/usr/bin/env python
# coding: utf-8

# In[65]:


import numpy as np
import matplotlib.pyplot as plt


# In[66]:


import pandas as pd


# In[67]:


dataset = pd.read_csv('position_salaries.csv')


# In[113]:


X= dataset.iloc[:,1].values
X =X.reshape(-1,1)
Y= dataset.iloc[:,2].values
Y =Y.reshape(-1,1)
print(X,Y)


# In[114]:


#from sklearn.model_selection import train_test_split


# In[115]:


#X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2, random_state = 0)


# In[116]:


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)


# In[117]:


from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y)


# In[118]:


#X_grid = np.arange(min(X), max(X), 0.1)
#X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X,Y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title("Truth or Bluff")
plt.xlabel('Position level')
plt.ylabel('Salary')
#plt.rcParams["figure.figsize"]=20,20
plt.show()


# In[ ]:





# In[ ]:





# In[124]:


lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))


# In[123]:


lin_reg.predict([[6.5]])


# In[ ]:
#end

