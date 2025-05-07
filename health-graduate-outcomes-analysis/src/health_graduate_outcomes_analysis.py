#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Importing libraries 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style('darkgrid')


# In[32]:


# Loading the dataset
data  = pd.read_csv('Health Graduate Outcomes.csv')

# Preview the first few rows
data.head()


# In[33]:


# Display info of dataset
data.info


# In[34]:


# Summary statistics for numerical columns
data.describe()


# In[35]:


# Getting the number of rows and columns
data.shape


# In[36]:


# Getting the column names
data.columns


# In[37]:


# Checking column types
data.dtypes


# In[38]:


# Checking for missing values
data.isnull().sum()


# In[39]:


#unique graduate outcomes
data['Graduate Outcomes'].unique()


# In[40]:


data['Fields of Education and Training'].unique()


# In[41]:


data[['Graduation Year', 'Graduate Outcomes', 'VALUE']].value_counts()


# In[42]:


# Select the relevant columns and calculate unique combinations with their counts
unique_counts = data[['Graduation Year', 'Fields of Education and Training', 'Gender', 'VALUE']].value_counts()

# Resetting index to display results as a DataFrame
unique_counts_df = unique_counts.reset_index(name = 'Count')

# Display the result
print(unique_counts_df)


# In[43]:


data['VALUE'].mean()


# In[44]:


data['VALUE'].median()


# In[45]:


data['VALUE'].max()


# In[46]:


data['VALUE'].min()


# In[47]:


# Getting descriptive statistics for the VALUE column
data['VALUE'].describe()


# # Insight 1: Trends in Graduate Outcomes Over Time

# In[48]:


# Grouping the data by Graduation Year and Graduate Outcomes, by summing the VALUE for each group
grad_outcomes_trend = data.groupby(['Graduation Year', 'Graduate Outcomes'])['VALUE'].sum().unstack()

# Plotting the data with a title
grad_outcomes_trend.plot(kind='bar', figsize=(12, 6))
plt.title('Graduate Outcomes by Year') 
plt.xlabel('Graduation Year')          
plt.ylabel('Total VALUE')              
plt.legend(title='Graduate Outcomes')  
plt.show()


# # Insight 2: Gender Differences in Graduate Outcomes

# In[49]:


# Aggregating data by Gender and Graduate Outcomes
gender_dt = data.groupby(['Gender', 'Graduate Outcomes'])['VALUE'].sum().unstack()

# Plotting the data with a title
gender_dt.plot(kind='bar', figsize=(10, 6), colormap='coolwarm')
plt.title('Graduate Outcomes by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Graduates')
plt.show()


# # Insight 3: Impact of Years Since Graduation on Outcomes

# In[50]:


# Aggregating data by Years since Graduation and Graduate Outcomes
time_dt = data.groupby(['Years since Graduation', 'Graduate Outcomes'])['VALUE'].sum().unstack()

# Plotting the data with a title
time_dt.plot(kind='line', figsize=(12, 8), marker='o')
plt.title('Graduate Outcomes vs. Years Since Graduation')
plt.xlabel('Years Since Graduation')
plt.ylabel('Number of Graduates')
plt.legend(title='Graduate Outcomes')
plt.show()


# # Insight 4: Three Statistical Tests of Field Specific Differences in Graduate Outcomes

# i)  ANOVA test

# In[51]:


# Performing one way ANOVA to compare the means of 'VALUE' across different Fields of Education and Training
# Getting unique fields
fields = data['Fields of Education and Training'].unique()  
values = [data[data['Fields of Education and Training'] == field]['VALUE'] 
          for field in fields]

# Runing ANOVA
result = stats.f_oneway(*values)

# Printing the result
print("ANOVA Result: F-statistic = " + str(result.statistic), "p-value = " + str(result.pvalue))

if result.pvalue < 0.05:
    print("There is a big difference in the average graduate outcomes between different fields of education.")
else:
    print("There is no big difference in the average graduate outcomes between different fields of education.")


# In[52]:


# Creating a box plot to show the distribution of VALUE across different fields of education
sns.boxplot(x='Fields of Education and Training', y = 'VALUE', data = data)
plt.xticks(rotation = 90)
plt.title('Graduate Outcomes Across Fields of Education')
plt.show()


# ii) T-test

# In[53]:


# Splitting the data by gender
male_grads = data[data['Gender'] == 'Male']['VALUE']
female_grads = data[data['Gender'] == 'Female']['VALUE']

# Perform t-test
t_stat, p_value = stats.ttest_ind(male_grads, female_grads)

# Print the result
print("T-test Result: t-statistic = " + str(t_stat), "p-value = " +str(p_value))

if p_value < 0.05:
    print("There is a big difference in the graduate outcomes between males and females.")
else:
    print("There is no big difference in the graduate outcomes between males and females.")


# In[54]:


# Creating a box plot to show the distribution of VALUE across different genders
sns.boxplot(x='Gender', y='VALUE', data = data)
plt.title('Graduate Outcomes by Gender')
plt.show()


# iii) Chi-Square test

# In[55]:


# Creatting a contingency for Gender vs Graduate Outcomes
category_counts = pd.crosstab(data['Gender'], data['Graduate Outcomes'])

# Chi-Square Test
chi2_stat, p_value, dof, expected = stats.chi2_contingency(category_counts)

# Print the result
print("Chi-Square Result: chi2-statistic = " + str(chi2_stat), "p-value = " + str(p_value))

if p_value < 0.05:
    print("There is a big relationship between Graduate Outcomes and Gender.")
else:
    print("There is no big relationship between Graduate Outcomes and Gender.")


# In[56]:


# Grouping the data by Years since Graduation, Graduate Outcomes and calculate the median of VALUE
median_data = data.groupby(['Years since Graduation', 'Graduate Outcomes'])['VALUE'].median().reset_index()

# Plotting the median values with a red shades palette
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Years since Graduation', y='VALUE', hue='Graduate Outcomes', data=median_data, palette='Reds', s=100, marker='o')

plt.title('Median Graduate Outcomes by Years Since Graduation')
plt.xlabel('Years Since Graduation')
plt.ylabel('Median Graduate Outcomes')
plt.legend(title='Graduate Outcomes')
plt.show()


