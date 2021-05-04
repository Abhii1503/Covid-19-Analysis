#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[63]:


data = pd.read_csv(r"C:\Users\user\Downloads\covid19_italy_region.csv")


# In[64]:


data.head()


# In[65]:


data.columns


# In[66]:


data.describe()


# In[67]:


data.isnull()


# # Realting the variables with ScatterPlots

# In[69]:


sns.relplot(x="Recovered", y="HospitalizedPatients", hue ="Deaths" ,data=data)


# In[70]:


sns.pairplot(data)


# In[71]:


sns.relplot(x="HospitalizedPatients", y="IntensiveCarePatients", kind='line', data=data)


# In[ ]:


sns.catplot(x="Recovered", y="Deaths", data=data)


# In[ ]:




