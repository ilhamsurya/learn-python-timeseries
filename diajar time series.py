#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[10]:


dataframe = pd.read_csv('daily-total-female-births-CA.csv', header=0)


# CARA MELAKUKAN DATA LOADING MENGGUNAKAN PANDAS

# Mendapatkan 5 data pertama dalam dataset

# In[11]:


dataframe.head()


# Mendapatkan jenis tipe data

# In[18]:


dataframe['date'].dtype


# Melakukan Loading Data dengan parse_dates

# In[19]:


df2 = pd.read_csv('daily-total-female-births-CA.csv', header=0 , parse_dates=[0])


# In[20]:


df2.head()


# In[21]:


df2['date'].dtype


# Melakukan loading data as a series

# In[23]:


series=pd.read_csv('daily-total-female-births-CA.csv', header=0, parse_dates=[0], index_col=[0], squeeze=True)


# In[24]:


series.head()


# EXPLORING TIME SERIES DATA

# Melihat size dari series

# In[26]:


df2.shape


# In[27]:


series.shape


# Query Berdasarkan waktu

# In[28]:


print(series['1959-01'])


# Condition

# In[29]:


df2[(df2['date'] > '1959-01-01') &(df2['date'] <= '1959-01-21')]


# Mendaparkan hasil deskripsi statistik (mean, count, dll)

# In[30]:


series.describe()


# In[31]:


df2.describe()


# DATA VISUALIZATION PT 2

# In[37]:


from matplotlib import pyplot as pit
get_ipython().run_line_magic('matplotlib', 'inline')


# Melakukan copy dari data df2, assign ke variabel lain

# In[39]:


Dataviz_df = df2.copy()


# Nampilin data 10 row

# In[42]:


Dataviz_df.head(10)


# Menampilkan time plot grafik index(bawah) terhadap birth(kiri)

# In[41]:


Dataviz_df['births'].plot()


# Mengubah nilai index yang awalnya di nomor (0,1,2) menjadi date sehingga plotting lebih jelas

# In[43]:


Dataviz_df.index = Dataviz_df['date']


# In[44]:


Dataviz_df.head()


# Melakukan plot ulang sehingga visualisasi data index diganti menjadi date

# In[45]:


Dataviz_df['births'].plot()


# ZOOMING IN DATA : Digunakan untuk mendetailkan tampilan data apabila rentang tahun yang ada sudah terlalu luas

# In[46]:


Dataviz_df2 = Dataviz_df[(Dataviz_df['date'] > '1959-01-01') & (Dataviz_df['date'] <= '1959-01-10')].copy()


# In[47]:


Dataviz_df2


# Menampilkan hasil plot data dengan visualisasi zooming in dari rentang 1959-01 sampai 1959-10

# In[48]:


Dataviz_df2['births'].plot()


# TRENDLINE - Bentuk visualisasi data time series, menampilkan data sesuai garis tren dari tahun ke tahun

# In[51]:


import seaborn as sns


# Menampilkan TRENDLINE pada SCATTERPLOT dengan X merupakan angka kelahiran dan Y index nya (tidak dapat menggunakan date dikarenakan harus numerik)

# In[50]:


sns.regplot(x= df2.index.values, y=df2['births'])


# Menampilkan hasil trendline quadratic

# In[52]:


sns.regplot(x=df2.index.values, y=df2['births'], order=2)


# MENGGANTI DATA SET, Menjadi berapa jauh US-AIRLINE terbang

# In[58]:


miles_df = pd.read_csv('us-airlines-monthly-aircraft-miles-flown.csv', header=0, parse_dates=[0])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[17]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




