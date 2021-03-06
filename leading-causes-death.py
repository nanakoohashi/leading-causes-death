#!/usr/bin/env python
# coding: utf-8

# # How has death changed in the United States from 1980 to 2009?
# 
# This is a dataset hosted by the Centers for Disease Control and Prevention. The organization has an open data platform found [here](https://data.cdc.gov/) and they update their information according the amount of data that is brought in. 
# 
# Selected Trend Table from Health, United States, 2011. Leading causes of death and numbers of deaths, by sex, race, and Hispanic origin: United States, 1980 and 2009.
# 
# #### Note:
# 1. Rank order is based on the number of deaths.

# ## Gather

# In[1]:


import pandas as pd
import zipfile
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:
with zipfile.ZipFile('leading-causes-of-death-and-numbers-of-deaths.zip', 'r') as myzip:
    myzip.extractall()

    
# In[3]:
df_death = pd.read_csv('selected-trend-table-from-health-united-states-2011.-leading-causes-of-death-and-numbers-of-deaths-by-sex-race-and-hispanic-origin-united-states-1980-and-2009.csv')
df_death


# In[4]:
# Make a copy of df
df = df_death.copy()

# ## Assess


# In[6]:
df_death.info()


# In[7]:
# Rename column to contain underscores instead of spaces to assess further possible issues
df_death.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)


# In[8]:
df_death.rank_order.unique()


# In[9]:
df_death.query('rank_order == "NaN"')


# In[10]:
df_death.rank_order.value_counts()


# In[11]:
df_death.group.unique()


# In[12]
df_death.group.value_counts()


# In[13]:
df_death.year.unique()


# In[14]:
df_death.year.value_counts()


# In[15]:
df_death.cause_of_death.value_counts()


# In[16]:
df_death.query('cause_of_death == "NaN"')


# In[17]: 
if math.isnan(df_death.cause_of_death[77]):
    print('hello')


# In[18]:
df_death.flag.unique()


# In[19]:
df_death.query('Flag == "1"')


# In[20]:
df_death.query('deaths == "NaN"')


# In[20]:
df_death.describe()


# In[21]:
df_death.sample()


# ### Issues
# 1. Column names contain spaces.
# 2. 'Group' contains both sex and race information.
# 3. 'Flag' contains one entry that is flagged.
# 4. 'Cause of Death' NaN entries cannot be queried.
# 5. Missing entries in "Rank order", "Cause of Death", and "Deaths".
# 6. Remove Cause of Death entries that equal "NaN".


# ### Clean
# ### 1. Column names contain spaces
# #### Code
# - This was completed while assessing data in order to properly assess the data.
# - df_death columns were renamed to replace spaces with underscores in the Assess Data section using the following code: `df_death.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
