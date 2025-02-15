#!/usr/bin/env python
# coding: utf-8

# In[72]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import pickle
from pickle import dump
from pickle import load
import streamlit as st


# In[91]:


# creating a welcome
st.title('Welcome')
st.title('World Development Web')


# In[92]:


# importing dataset 
country = pd.read_excel("D:\\Data Science\\New Project\\k_data.xlsx")
country_select = country['Country'].drop_duplicates()


# In[93]:


# Creating Dataframe
def user_input_contry():
    Country = st.sidebar.selectbox('select a contry:', country_select)
def user_inputs():
    #Country = st.sidebar.selectbox('select a contry:', country_select)
    BirthRate = st.sidebar.number_input('Enter BirthRate')
    BusinessTaxRate = st.sidebar.number_input('Enter BusinessTaxRate')
    CO2Emissions = st.sidebar.number_input('Enter CO2Emissions rate')
    DaystoStartBusiness = st.sidebar.number_input('Enter DaystoStartBusiness')
    EaseofBusiness = st.sidebar.number_input('Enter EaseofBusiness')
    EnergyUsage = st.sidebar.number_input('Enter EnergyUsage')
    GDP = st.sidebar.number_input('Enter GDP')
    HealthExpGDP = st.sidebar.number_input('Enter HealthExpGDP')
    HealthExpCapita = st.sidebar.number_input('Enter HealthExpCapita')
    HourstodoTax = st.sidebar.number_input('Enter HourstodoTax')
    InfantMortalityRate = st.sidebar.number_input('Enter InfantMortalityRate')
    InternetUsage = st.sidebar.number_input('Enter InternetUsage')
    LendingInterest = st.sidebar.number_input('Enter LendingInterest')
    LifeExpectancyFemale = st.sidebar.number_input('Enter LifeExpectancyFemale')
    LifeExpectancyMale = st.sidebar.number_input('Enter LifeExpectancyMale')
    MobilePhoneUsage = st.sidebar.number_input('Enter MobilePhoneUsage')
    Population14 = st.sidebar.number_input('Enter Population14')
    Population64 = st.sidebar.number_input('Enter Population64')
    Populationabove65 = st.sidebar.number_input('Enter Populationabove65')
    PopulationTota = st.sidebar.number_input('Enter PopulationTota')
    PopulationUrban = st.sidebar.number_input('Enter PopulationUrban')
    TourismInbound = st.sidebar.number_input('Enter TourismInbound')
    TourismOutbound = st.sidebar.number_input('Enter TourismOutbound')
    data = {#'Country' : Country,
            'Birth Rate' : BirthRate,
            'Business Tax Rate' : BusinessTaxRate,
            'CO2 Emissions' : CO2Emissions,
            'Days to Start Business' : DaystoStartBusiness,
            'Ease of Business' : EaseofBusiness,
            'Energy Usage' : EnergyUsage,
            'GDP' : GDP,
            'Health Exp % GDP' : HealthExpGDP,
            'Health Exp/Capita' : HealthExpCapita,
            'Hours to do Tax' : HourstodoTax,
            'Infant Mortality Rate' : InfantMortalityRate,
            'Internet Usage' : InternetUsage,
            'Lending Interest' : LendingInterest,
            'Life Expectancy Female' : LifeExpectancyFemale,
            'Life Expectancy Male' : LifeExpectancyMale,
            'Mobile Phone Usage' : MobilePhoneUsage,
            'Population 0-14' : Population14,
            'Population 15-64' : Population64,
            'Population 65+' : Populationabove65,
            'Population Tota' : PopulationTota,
            'Population Urban' : PopulationUrban,
            'Tourism Inbound' : TourismInbound,
            'Tourism Outbound' : TourismOutbound
    }
    features = pd.DataFrame(data, index = [0])
    return features


# In[94]:


df = user_inputs().astype(float)
st.write(df)


# In[95]:


new_fi = country.drop(columns = ['Country','cluster_id'],axis = 1)


# In[96]:


#importing umap
from umap import UMAP
u_map = UMAP(n_components = 23, init = 'random', random_state = 0)
components = u_map.fit_transform(new_fi)


# In[97]:


#importing kmeans
from sklearn.cluster import KMeans
#model = KMeans()


# In[98]:


#Building Cluster algorithm
k_clusters = KMeans(n_clusters=5, algorithm = "lloyd",n_init = 'warn',max_iter = 300,random_state=0)
k_clusters.fit(components.astype('double'))


# In[99]:


#prediction
prediction = k_clusters.predict(df)
#st.success(prediction)


# In[100]:


#creating a Check box
agree = st.sidebar.checkbox('I agree')

if agree:
    st.write('Great!')


# In[101]:


#Creating a Submit Button
country = st.text_input("Enter your Country Name", user_input_contry())
if(st.button('Submit')):
    results = prediction
    st.success(results)
    st.subheader('contry status')
    if (results == 0):
        st.success('Developed Country')
    elif(results >=1 <3):
        st.warning('Developing Country')
    elif(results > 3):
        st.error('Under Developed contry')


# In[102]:




# In[103]:



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




