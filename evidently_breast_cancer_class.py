#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Data Drift and Model Performance Dashboards for Breast cancer dataset

import pandas as pd

from datetime import datetime
from sklearn import datasets, ensemble, model_selection

from evidently.dashboard import Dashboard
from evidently.tabs import ProbClassificationPerformanceTab

from evidently.model_profile import Profile
from evidently.profile_sections import ProbClassificationPerformanceProfileSection


# # Breast Cancer Data

# In[2]:


bcancer = datasets.load_breast_cancer()


# In[3]:


bcancer_frame = pd.DataFrame(bcancer.data, columns = bcancer.feature_names)


# In[4]:


bcancer_frame.head()


# # Model Performance Dashboard

# In[5]:


bcancer_frame = pd.DataFrame(bcancer.data, columns = bcancer.feature_names)


# In[6]:


reference, production, y_train, y_test = model_selection.train_test_split(bcancer_frame, 
                                                                          bcancer.target, 
                                                                          random_state = 0)


# In[8]:


model = ensemble.RandomForestClassifier(random_state = 11)


# In[9]:


model.fit(reference, y_train)


# In[10]:


train_probas = pd.DataFrame(model.predict_proba(reference))
train_probas.columns = bcancer.target_names
test_probas = pd.DataFrame(model.predict_proba(production))
test_probas.columns = bcancer.target_names


# In[11]:


reference.reset_index(inplace=True, drop=True)
reference['target'] = [bcancer.target_names[x] for x in y_train]
merged_reference = pd.concat([reference, train_probas], axis = 1)

production.reset_index(inplace=True, drop=True)
production['target'] = [bcancer.target_names[x] for x in y_test]
merged_production = pd.concat([production, test_probas], axis = 1)


# In[12]:


column_mapping = {}

column_mapping['target'] = 'target'
column_mapping['prediction'] = bcancer.target_names.tolist()
column_mapping['numerical_features'] = bcancer.feature_names


# In[13]:


model_performance_dashboard = Dashboard(tabs=[ProbClassificationPerformanceTab])
model_performance_dashboard.calculate(merged_reference, merged_production, column_mapping = column_mapping)
model_performance_dashboard.show()


# In[14]:


#model_performance_dashboard.save('bcancer_prob_classification_performance.html')


# # Model Performance Profile

# In[15]:


model_performance_profile = Profile(sections=[ProbClassificationPerformanceProfileSection])


# In[16]:


model_performance_profile.calculate(merged_reference, merged_production, column_mapping = column_mapping)


# In[17]:


model_performance_profile.json()


# In[ ]:





# In[ ]:




