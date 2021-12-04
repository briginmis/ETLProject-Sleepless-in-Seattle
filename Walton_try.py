#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[56]:


df = pd.read_csv("Resources/listings.csv")


# In[57]:


df1=df[['id','amenities']]


# In[58]:


df1['amenities']=df1['amenities'].str.replace('{','')
df1['amenities']=df1['amenities'].str.replace('}','')
df1['amenities']= df1['amenities'].str.replace('"','')


# In[59]:


id_list=[]
amen_list=[]

for index, row in df1.iterrows():
  id_list.append(row[0])
  amen_list.append(row[1].split(','))


# In[60]:


df_final=pd.DataFrame({'id':id_list,"amenities":amen_list})
df_final.explode("amenities")

