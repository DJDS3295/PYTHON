#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


churn_rates = pd.read_csv(r'C:\Users\Asus\Downloads\telecom_customer_churn.csv')


# In[3]:


churn_rates


# In[4]:


churn_rates.shape


# In[8]:


df_churn_rates= churn_rates


# In[9]:


df_churn_rates


# In[10]:


mask = df_churn_rates['contract_type'] == 'Month-to-Month'


# In[11]:


df_churn_rates[mask]


# In[12]:


df_churn_rates[mask].shape


# In[37]:


df_churn_rates[mask].where(df_churn_rates[mask]['churn_status'] == 'Not Churned').isnull().sum()


# In[ ]:


# total churned while month to month contract type is 1650, while not churned is 1685.


# In[39]:


df_churn_rates.where(df_churn_rates['churn_status'] == 'Not Churned').isnull().sum()


# In[ ]:


# total churned from total data is 4957 and not churned is 5043


# In[ ]:


# WHETHER CHURN RATES ARE SIMILAR FOR BOTH GENDERS


# In[41]:


mask_gender = df_churn_rates['gender'] == 'Male'


# In[42]:


df_churn_rates[mask_gender]


# In[46]:


df_churn_rates[mask_gender].where(df_churn_rates[mask_gender]['churn_status'] == 'Not Churned').isnull().sum()


# In[ ]:


# total male churn data is 4967
# total churned for male is 2429 and for Not churned is 2538. 


# In[47]:


mask_gender = df_churn_rates['gender'] == 'Female'


# In[49]:


df_churn_rates[mask_gender]


# In[ ]:


# total female data is 5033


# In[50]:


df_churn_rates[mask_gender].where(df_churn_rates[mask_gender]['churn_status'] == 'Not Churned').isnull().sum()


# In[ ]:


# total churned data for female is 2528 andd Not churned data is 2505.


# In[51]:


df_churn_rates


# In[55]:


df_mean_charge = df_churn_rates['monthly_charges'].mean()


# In[56]:


df_mean_charge


# In[77]:


df_abvavg_rates = df_churn_rates.where(df_churn_rates['monthly_charges'] > 64.8632)


# In[79]:


df_abvavg_rates


# In[ ]:





# In[62]:


df_churn_rates


# In[63]:


df_contract = df_churn_rates['contract_type']== 'One Year'


# In[65]:


df_churn_rates[df_contract]


# In[85]:


df_churn_rates[df_contract].where(df_churn_rates[df_contract]['churn_status'] == 'Not Churned').isnull().sum()


# In[ ]:


# total 1668 churned for one year contract and 1675 Not churned for one year


# In[86]:


df_contract2 = df_churn_rates['contract_type']== 'Two Year'


# In[87]:


df_churn_rates[df_contract2]


# In[88]:


df_churn_rates[df_contract2].where(df_churn_rates[df_contract2]['churn_status'] == 'Not Churned').isnull().sum()


# In[ ]:


# total 1639 churned for 2 year and 1683 for Not churned for 2 year contract

