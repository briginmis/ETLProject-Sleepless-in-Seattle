#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import cleaning_functions as cf

# read in csv
df=pd.read_csv("../Resources/listings.csv")

# keep only those columns
df = df[['id','amenities']]
df.head(2)


# In[63]:


df3 = cf.explode_into_rows_in_new_table(input_df = df, id_column = "id", explode_column = "amenities")

# Preview Output
df3.head(5)


# In[64]:


# save as csv
df3.to_csv("../Resources/Amenities_Clean.csv",index=False)


# In[ ]:




