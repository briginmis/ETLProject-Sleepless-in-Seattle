#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import cleaning_functions as cf
import warnings
warnings.filterwarnings('ignore')

pd.set_option("display.max_columns", None)


# In[2]:


df_all = pd.read_csv("../Resources/listings.csv")
df_all = df_all.rename(columns={"id": "listing_id"})
df_all.head()


# In[4]:


df_all = cf.clean_dollar(df_all,['price',
                'weekly_price',
                'monthly_price',
                'security_deposit',
                'cleaning_fee',
                'extra_people'])
df_all = cf.clean_percent(df_all,['host_response_rate','host_acceptance_rate'])
df_all = cf.clean_boo(df_all,['host_is_superhost',
                            'host_has_profile_pic',
                            'host_identity_verified',
                            'is_location_exact',
                            'has_availability',
                            'requires_license',
                            'instant_bookable',
                            'require_guest_profile_picture',
                            'require_guest_phone_verification'])
df_all.head(2)


# In[5]:


df_Property=df_all[['listing_id',
                'host_id',
                'listing_url',
                'name',
                'property_type',
                'room_type',
                'accommodates',
                'bathrooms',
                'bedrooms',
                'beds',
                'bed_type',
                'square_feet',
                'description',
                'notes',
                'transit',
                'picture_url',
                'guests_included',
                'minimum_nights',
                'maximum_nights',
                'calendar_updated',
                'instant_bookable']]
                
df_Address=df_all[['listing_id',
            'country_code',
            'country',
            'state',
            'city',
            'zipcode',
            'smart_location',
            'neighbourhood',
            'street',
            'latitude',
            'longitude',
            'is_location_exact']]

df_host=df_all[['host_id',
            'host_url',
            'host_name',
            'host_since',
            'host_about',
            'host_is_superhost',
            'host_picture_url',
            'host_listings_count',
            'host_identity_verified',
            'host_location',
            'host_response_time',
            'host_response_rate',
            'host_acceptance_rate',
            'host_neighbourhood']]



df_review_stats=df_all[['listing_id',
                'number_of_reviews',
                'reviews_per_month',
                'first_review',
                'last_review',
                'review_scores_rating',
                'review_scores_accuracy',
                'review_scores_cleanliness',
                'review_scores_checkin',
                'review_scores_communication',
                'review_scores_location',
                'review_scores_value']]

df_Pricing=df_all[['listing_id',
                'price',
                'weekly_price',
                'monthly_price',
                'security_deposit',
                'cleaning_fee',
                'extra_people',
                'cancellation_policy']]

df_Availability = df_all[['listing_id',
                        'has_availability',
                        'availability_30',
                        'availability_60',
                        'availability_90',
                        'availability_365']]


# In[6]:


df_Property.to_csv('../Resources/Property_clean.csv', index=False)
df_Address.to_csv('../Resources/Address_clean.csv', index=False)
df_host.to_csv('../Resources/Host_clean.csv', index=False)
df_review_stats.to_csv('../Resources/Review_Statistics_clean.csv', index=False)
df_Pricing.to_csv('../Resources/Pricing_clean.csv', index=False)
df_Availability.to_csv('../Resources/Availability.csv', index=False)

