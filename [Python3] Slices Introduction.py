#!/usr/bin/env python
# coding: utf-8

# In[26]:


## Slice Introduction


# In[11]:


# Slice: 序列可以切開成獨立的元素。 形式為[start:stop] ，start的元素會被包含，stop元素不會被包含。


# In[12]:


a=[0,1,2,3,4,5,6]
print(f'a[2:5]= {a[2:5]}')


# In[13]:


# 可以依據序列更換值。


# In[14]:


a[5:6]=[7]
print(f'a= {a}')


# In[15]:


a[0:2]=['x','y']
print(f'a= {a}')


# In[16]:


# 忽略start或是stop代表從頭開始，或是直到序列結尾。


# In[17]:


a[:4]


# In[18]:


a[3:]


# In[19]:


# [start:stop:間隔] ：可以設定slice要間隔多少元素。


# In[20]:


a[::2]


# In[21]:


# [::-1]:可以翻轉一個list或是tuple


# In[22]:


a[::-1] #翻轉list


# In[25]:


b=1,2,3,4,5,6,7
b[::-1] #翻轉tuple

