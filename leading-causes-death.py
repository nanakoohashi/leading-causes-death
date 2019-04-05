#!/usr/bin/env python
# coding: utf-8

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
