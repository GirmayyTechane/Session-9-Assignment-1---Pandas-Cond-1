
#!/usr/bin/env python
# coding: utf-8

# Read the dataset from the below link https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv

# In[18]:


import numpy as np
import pandas as pd


# In[33]:


url='https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
df = pd.read_csv(url)


# 1. Delete unnamed columns

# In[ ]:


df.head()


# In[36]:


mydf=df.drop('Unnamed: 0',axis=1)


# In[37]:


mydf.head()


# 2. Show the distribution of male and female

# In[44]:


len(mydf)


# In[54]:


len(mydf[mydf['Gender']=='M'])


# In[53]:


len(mydf[mydf['Gender']=='F'])


# In[59]:


mydf['Gender'].value_counts()


# 3. Show the top 5 most preferred names

# In[49]:


mydf['Name'].value_counts().head()


# 4. What is the median name occurence in the dataset

# In[ ]:


mydf.head()


# 5. Distribution of male and female born count by states

# In[104]:


mydf.groupby(['State','Gender']).size().head(10)


# In[ ]:




