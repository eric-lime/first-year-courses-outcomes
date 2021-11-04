#!/usr/bin/env python
# coding: utf-8

# # **First-year courses and outcomes**

# In[3]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


df1 = pd.read_excel("STEM Outcomes Individual Data 2002 - 2018.xlsx")
df2 = pd.read_excel("STEM Outcomes Grades 2002 - 2018.xlsx")


# In[8]:


#Merge the data on the Student ID key keeping only those records with IDs in both data sets.
df_merge = pd.merge(df1, df2, left_on = 'Student ID', right_on = 'Student ID', how = 'inner')
df_merge.head()

#Here I called the merge function onto the two datasets of grades and outcomes. I merged together the left dataframe’s "Student ID" column with the right dataframe’s "Student ID" column and intersected the keys from both the frames. Then I stored the output of the merge function into a variable called df_merge.


# In[9]:


common_degree = df_merge['Major 1'].value_counts() 
common_degree.head()
#I decided to print out the top 5 awarded degrees by looking into the column of "Major 1" within the df_merge variable and attaching a value counts method in order to find the number of students who were attached with the certain degree.


# In[10]:


common_classes = df_merge['Course Title'][df_merge['Major 1']== "BIOL"].value_counts() 
#Here looked into the Biology major and compare it to the first year courses which Biology majors have taken.


# In[11]:


common_classes[common_classes>100].plot(kind='bar')
#This figure shows a bar graph of first year classes that have been taken by Biology majors. I also made a limit for the frequency of students who have taken these classes by setting the value of common_classes to be greater than 100.


# In[19]:


gen_chem_bio = df_merge['Grade'][df_merge['Course Title']== "General Chemistry"][df_merge['Major 1']=="BIOL"].value_counts()
gen_chem_bio
#Here I wanted to compare the grades of Biology majors that had taken General Chemistry


# In[20]:


gen_chem_bio.plot(kind="hist")
#Here is a historgram which shows the grades of Biology majors who had taken the first year course of General Chemistry. It was not suprising to see that the majority of Biology majors scored well within the General Chemistry course.


# In[23]:


gen_chem = df_merge['Grade'][df_merge['Course Title']== "General Chemistry"][df_merge['Major 1']!="BIOL"].value_counts() 
gen_chem.plot(kind="hist")
#Now I compared non-biology majors' grades of General Chemistry and plotted the outcome.
#It suprised me at first because I did not think that there would be this many non-Biology majors who had scored well within the course but then I realized that there were probably many students who came in thinking that they would pursue Biology but then the further that they had gotten into the program the more rigorous it would be or that they simply just wanted to pursue another major after their first year.


# In[24]:


student = pd.merge(df1, df2, left_on = 'Student ID', right_on = 'Student ID', how = 'inner')
student
#For my next analysis, I wanted to focus on the relationship between race and majors.


# In[25]:


races = student['Races'].value_counts() 
races
#Got the value counts on what races students identify as.


# In[26]:


major_race = student['Races'][student['Major 1']== "CHEM"].value_counts()
major_race
#I now compared the races with a certain major. Since I noticed that General Chemistry was one of the most popular courses taken while Biology was the most common major, I wanted to focus on another scientific major, Chemistry.


# In[43]:


labels = ['WH (82.5%)','AS (14.3%)','BL (1.5%)','AN (0.9%)','AS, WH (0.8%)']
fig, ax = plt.subplots()
ax.pie(major_race)
plt.legend(labels = labels, loc='best')
plt.show()
#Here I displayed a piechart that shows what percentage of Chemistry majors are associated with what race. As you can tell a vast majority of the chemistry majors are of "White" race.


# In[48]:


major_race1 = student['Races'][student['Major 1']== "ENGL"].value_counts() 
major_race1.head(5)
#I repeated the comparison from above with another major, English.


# In[50]:


labels = ['WH (88.2%)','AS (7.6%)','BL (2.7%)','AN (0.9%)','AS, WH (0.5%)']
fig, ax = plt.subplots()
ax.pie(major_race1.head(5))
plt.legend(labels = labels, loc='best')
plt.show()
#As it turns out, there seems to be slightly larger percentage of English majors that are white than Chemistry majors that are white, while the ratio for Asians are much larger for Chemistry majors.


# In[53]:


#The data above got me curious about the diversity of Whitman at the start(earliest date) of the dataset and at the end(latest date) of the dataset.
time_race = student['Races'][student['Start Term']=="2002FA"].value_counts() 
time_race.plot(kind="bar")
plt.show()
#This bar plot shows that at the earliest recorded semester within the dataset, there were only 5 different races amongst students.


# In[54]:


time_race1 = student['Races'][student['Start Term']=="2017FA"].value_counts()
time_race1.plot(kind="bar")
plt.show()
#As you can see within the latest recorderd semester at Whitman, there is a much larger range of diversity identifications but the overwhelming majority within race is still White. As a student it is nice to see that there are a lot more different types of races being included on campus and I hope that the diversity will further progress rapidly as the years go by.


# In[ ]:


#Within this project, I got a deeper insight on what type of education route students tend to go on depending on race. This gave me the opportunity to go further into detail about the diversity within Whitman and see how it has progressed over the course of 15 years.

