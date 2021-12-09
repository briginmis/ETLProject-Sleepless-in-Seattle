#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


attractions_df = pd.read_csv("../Resources/Attractions.csv")
attractions_df.head(2)


# In[3]:


addresses_df = pd.DataFrame({
        "place": ["aibrnb1","airbnb2"],
        "thing1": ["stuff","stuff"],
        "latitude": [39.9522322,39.9501234],
        "longitude":[-75.12523533,-75.160000]
        
    })
addresses_df
addresses_df=pd.read_csv("../Resources/Address_clean.csv")
addresses_df.head(2)


# In[5]:


# Add Distance
from math import radians, cos, sin, asin, sqrt
from Haversine_Function import haversine

# Read in the philly coorindates variables from another Jupyter Notebook

for index,eachaddressesrow in addresses_df.iterrows():
    list_of_lng_for_this_row=[]
    for index,eachattraction in attractions_df.iterrows():
        list_of_lng_for_this_row.append(addresses_df.apply(lambda row: haversine(
                                            eachattraction['lng'], 
                                            eachattraction['lat'], 
                                            row['longitude'], 
                                            row['latitude']), axis=1)
    )
    addresses_df["distance"]=sum(list_of_lng_for_this_row)/len(list_of_lng_for_this_row)
addresses_df


# In[7]:


addresses_df.to_csv("../Resources/Address_clean2.csv")

