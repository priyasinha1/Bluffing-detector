#!/usr/bin/env python
# coding: utf-8

# In[48]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[49]:


dataset = pd.read_csv('position_salaries.csv')


# In[50]:


dataset.head()


# In[51]:


dataset.describe()


# In[52]:


X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values


# In[53]:


from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X = sc_X.fit_transform(X.reshape(-1, 1))
Y = sc_Y.fit_transform(Y.reshape(-1, 1))


# In[54]:


from sklearn.svm import SVR
regressor = SVR(kernel ='rbf')
regressor.fit(X,Y)


# In[57]:


y_pred = sc_Y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])))
print(y_pred)


# In[56]:


plt.scatter(X,Y,color='red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.show()


# In[ ]:




