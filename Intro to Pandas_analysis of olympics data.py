#!/usr/bin/env python
# coding: utf-8

# In[136]:


import pandas as pd
import pandas


# In[137]:


pandas.show_versions()


# In[138]:


pd.__version__


# In[139]:


get_ipython().run_line_magic('pinfo', 'pd.show_versions')


# In[140]:



#a dataframe is a two dimenational array 
#it is spreadsheet with rows and columns

#A series is a one dimensional array of indexed data
# series can be a row in the dataframe 


# In[141]:


oo = pd.read_csv("athlete_events.csv")
oo


# In[142]:


#accessing a series 


# In[143]:


# the best will be to use the [""]


# In[144]:


#accessing series 

oo = pd.read_csv("athlete_events.csv")
oo


# In[145]:


oo['City']


# In[146]:


type(oo.City)


# In[147]:


#challenge 


# In[148]:


oo


# In[149]:


oo["NOC"] #listing NOC using the [] method 


# In[150]:


oo.NOC #listing NOC using the . method 


# In[151]:


oo[["Year","City","Name","Medal"]]


# In[152]:


#data inputs and Validation


# In[153]:


oo.shape # diemension of the dataset 


# In[154]:


oo.head(10)


# In[155]:


oo.tail(20)


# In[156]:


oo.info()


# In[157]:


#list our olympics df 


# In[158]:


oo


# In[159]:


#list noc
oo["NOC"]


# In[160]:


type(oo.NOC)


# In[161]:


oo[["Year","City","Name","Medal"]]


# In[162]:


# data input and validation 


# ### Basic Analysis 

# In[163]:


#value Counts 

# it counts all the unique elements 

# it doesnt count NAN

oo.Year.value_counts()


# In[164]:


oo.Sex.value_counts()


# In[165]:


oo.sort_values(by=["Age","Sex"])


# In[166]:


#Boolean Indexing 


# In[167]:


oo.head()


# In[168]:


oo.Medal


# In[169]:


oo[oo.Medal=="Gold"]


# In[170]:


oo.Medal=="Gold"


# In[171]:


#string handling 


# In[172]:


oo[oo.Name.str.contains("Florence")]


# In[173]:


oo[oo.Name.str.contains("Jesse")]


# In[174]:


### Basic PLotting 


# In[175]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[176]:


oo.Sport.value_counts().plot(kind="line");


# In[177]:


oo.Sport.value_counts().plot(kind="bar")


# In[178]:


oo.Sport.value_counts().plot(kind="pie")


# In[179]:


#plot color 


# ther are three types of color maps 
#sequential 
#Diverging 
#Qualitative 


# In[180]:


oo.Sport.value_counts().plot(kind="bar",color="maroon")


# In[181]:


oo.Sport.value_counts().plot(kind="bar",color="maroon",figsize= (15,3))


# In[182]:


#Seaborn is a visualization tool bui;t on matplotlib

import seaborn as sns


# In[183]:


oo.set_index("Name",inplace = True)


# In[184]:


oo.head()


# In[185]:


oo.reset_index()


# In[186]:


oo.head()


# In[187]:


oo.set_index("Names", inplace=True)


# In[ ]:


#loc 
   
   #selection by the labels 
   
# key errors means items are not found 


# In[ ]:


oo.loc["A Dijiang"]


# In[ ]:


# iloc allows for the traditional pythonic slicing 


# In[ ]:


oo.head()


# In[ ]:


oo.iloc[1200]


# In[ ]:


#challenge of the day 


# 1.plot the total number of medals awarded at each of the olympic games throughout history 
# 
# 2. which countries did not win a medal 

# In[ ]:


# question 1 


# In[189]:


oo.Year.Value_counts()


# In[191]:


list(oo.groupby("Age"))


# In[195]:


oo.groupby("Year").size()


# In[196]:


oo.stack()


# In[202]:


lo = oo[oo.Year==2000]


# In[210]:


g=lo.groupby(["NOC","Medal"]).size().unstack("Medal",fill_value=0)
g.sort_values(["Gold","Silver","Bronze"],ascending=False)[["Gold","Silver","Bronze"]]


# In[214]:


sns.heatmap(g)


# In[215]:


g=g.transpose()
g


# In[216]:


sns.heatmap(g)


# In[ ]:




