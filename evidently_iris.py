#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd

from sklearn import datasets

from evidently.dashboard import Dashboard
from evidently.tabs import DataDriftTab

from evidently.model_profile import Profile
from evidently.profile_sections import DataDriftProfileSection


# In[19]:


iris = datasets.load_iris()


# In[20]:


iris_frame = pd.DataFrame(iris.data, columns = iris.feature_names)


# # Data Drift Dashboard

# In[21]:


iris_data_drift_dashboard = Dashboard(tabs=[DataDriftTab])
iris_data_drift_dashboard.calculate(iris_frame, iris_frame, column_mapping = None)


# In[22]:


iris_data_drift_dashboard.show()


# In[ ]:


#iris_data_drift_dashboard.save('iris_data_drift.html')


# # Data Drift Profile

# In[23]:


iris_data_drift_profile = Profile(sections=[DataDriftProfileSection])
iris_data_drift_profile.calculate(iris_frame, iris_frame, column_mapping = None)


# In[24]:


iris_data_drift_profile.json()


# In[ ]:




