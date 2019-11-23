#!/usr/bin/env python
# coding: utf-8

# # University of Kentucky Daily Crime Log

# The University of Kentucky provides publically available information on crimes commited on campus property.
# The following process is the extraction, analysis, and visualization of the data.

# ## Scraping the Data

# In[1]:


# Import the support libraries
from os import getenv
import requests
from bs4 import BeautifulSoup
import pandas as pd
from dateutil.parser import parser
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')


# In[3]:


# we are going to scrape crime data from the UK crime http://www.uky.edu/crimelog/
# substitute variables to fill in REST query criteria
start_month, start_day, start_year = 1, 1, 2019
end_month, end_day, end_year = 12, 31, 2019
crime_data_raw = requests.get('http://www.uky.edu/crimelog/log?field_log_category_value=All' +
                              '&field_log_report_value%5Bmin%5D%5Bmonth%5D=' + str(start_month) +
                              '&field_log_report_value%5Bmin%5D%5Bday%5D=' + str(start_day) +
                              '&field_log_report_value%5Bmin%5D%5Byear%5D=' + str(start_year) +
                              '&field_log_report_value%5Bmax%5D%5Bmonth%5D=' + str(end_month) +
                              '&field_log_report_value%5Bmax%5D%5Bday%5D=' + str(end_day) +
                              '&field_log_report_value%5Bmax%5D%5Byear%5D=' + str(end_year)
                             )


# In[4]:


# create a soup object 
crime_bs_proc = BeautifulSoup((crime_data_raw.text), "html.parser")


# ## Processing the Data

# In[5]:


# find the table header in the data
crime_data_header = crime_bs_proc.find('thead')


# In[6]:


# find all the table headers
crime_data_heads = crime_data_header.find_all('th')


# In[7]:


# create an empty list for the header
header = []

# iterate through the header element to get text
for col in crime_data_heads:
    cols = col.find_all('a')
    cols = [ele.text.strip() for ele in cols]
    header.append([ele for ele in cols if ele])

# flatten the list to a single list
header = [item for sublist in header for item in sublist]


# In[8]:


# find the table rows in the data
crime_data_body = crime_bs_proc.find('tbody')


# In[9]:


# find all table rows
crime_data_rows = crime_data_body.find_all('tr')


# In[10]:


# create an empty list for the rows of data
data = []

# iterate through the header element to get the rows
for row in crime_data_rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])


# In[11]:


# create a dataframe with our data using our header list
uk_crime_data = pd.DataFrame(data, columns=header)
uk_crime_data.head()


# In[12]:


# backup the raw scraped data to CSV file
uk_crime_data.to_csv('data/ukpd_crimelog_2018.csv', index=False)


# ## Structuring the Data

# In[13]:


# create a new dataframe from the CSV
uk_crime_csv = pd.read_csv('data/ukpd_crimelog_2018.csv')
uk_crime_csv.head()


# In[14]:


# descriptive statistical summary
uk_crime_csv.describe()


# In[15]:


uk_crime_csv['Street'] = [i[0] for i in (uk_crime_csv.Location.apply(lambda x: x.split(' - ')))]
uk_crime_csv['Area'] = [i[-1] for i in (uk_crime_csv.Location.apply(lambda x: x.split(' - ')))]


# In[16]:


del uk_crime_csv['Location']


# In[17]:


uk_crime_csv.head()


# In[18]:


uk_crime_csv['Street'] = uk_crime_csv.Street.apply(lambda x: x + ', LEXINGTON, KY')


# In[19]:


uk_crime_csv.head()


# In[20]:


# backup the raw scraped data to CSV file
uk_crime_csv.to_csv('data/ukpd_crimelog_2018_geo.csv', index=False)


# ## Geocoding the Data

# In[21]:


uk_crime_geo = pd.read_csv('data/ukpd_crimelog_2018_geo.csv')
uk_crime_geo.head()


# In[22]:


unique_locations = list(uk_crime_geo.Street.unique())


# In[23]:


unique_locations


# ### Still to finish

# In[7]:


#import the geocoder API (you'll need an api key)
from geopy.geocoders import OpenCage
geolocator = OpenCage(api_key='')


# In[8]:


geolocator.geocode('1120 UNIVERSITY DRIVE, LEXINGTON, KY')


# In[ ]:


street_locs = [geolocator.geocode(i) for i in uk_crime_geo.Street]
#locs = pd.DataFrame([(i, i.latitude, i.longitude) for i in street_locs], columns=['Location', 'Latitude', 'Longitude'])
#streets_geocoded = uk_crime_geo.combine_first(locs)


# In[ ]:





# ## Time Series Analysis

# In[24]:


# plot the number of crime categories in 2018
category_summary = pd.DataFrame(uk_crime_csv.Category.value_counts())
category_summary.plot(kind='barh')


# In[25]:


# plot the number of residential occurences in 2018
residential_summary = pd.DataFrame(uk_crime_csv['Residential occurrence'].value_counts())
residential_summary.plot(kind='bar')


# In[26]:


# plot the number of crime case outcomes in 2018
disposition_summary = pd.DataFrame(uk_crime_csv.Disposition.value_counts())
disposition_summary.plot(kind='barh')


# In[27]:


# import data with datetime group as index
uk_crime_datetime = pd.read_csv('data/ukpd_crimelog_2018.csv', index_col='Crime date and time', parse_dates=True)


# In[28]:


uk_crime_datetime.head()


# In[ ]:




