#!/usr/bin/env python
# coding: utf-8

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
