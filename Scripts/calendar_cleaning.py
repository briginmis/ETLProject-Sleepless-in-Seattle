#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies
import pandas as pd
import cleaning_functions as cf
import warnings
warnings.filterwarnings('ignore')



# In[2]:


# Read calendar csv file
calendar_df = pd.read_csv("../Resources/calendar.csv")
calendar_df


# In[4]:


# Create new column 'available_bool' to convert 'available' column to boolean
calendar_df = cf.clean_dollar(calendar_df,['price'])
calendar_df = cf.clean_boo(calendar_df,['available'])


# In[5]:


#Display dataframe
calendar_df


# In[6]:


#Convert clean dataframe to csv
calendar_df.to_csv("../Resources/calendar_clean.csv", index = False)


# In[ ]:




