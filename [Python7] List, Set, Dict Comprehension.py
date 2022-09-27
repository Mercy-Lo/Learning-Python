#!/usr/bin/env python
# coding: utf-8

# In[8]:


# List Comprehension 包含式


# In[9]:


# [] 內放入for迴圈，if 條件句，可以將特定的list元素選出來。
# upper() : 可使string的字母變成大寫。


# In[10]:


a_list=['hi','can','trip','road','ice']
[x.upper() 
for x 
in a_list 
if len(x)>3]


# In[11]:


# Set Comprehension


# In[12]:


unique_lengths={len(x) for x in a_list}
unique_lengths


# In[13]:


# 使用map()語法: 可以更快速且精簡的生成set。


# In[15]:


set(map(len,a_list))


# In[ ]:


# Dict Comprehension: 搭配enumerate() 一起使用，可以找到dict中，每一個value的index。


# In[16]:


loc_mapping={val: index for index, val in enumerate(a_list)}
loc_mapping


# In[17]:


# 巢式list包含式: 今有一個list叫做all_data，請找出包含2個e的名字。


# In[ ]:


# 善用2個fo迴圈，找到list與vaule的相互關係。


# In[34]:


all_data=[['John','Emily','Michael','Mary','Steven'],['Maria','Juan','Javier','Natalia','Pilar']]

# 先給答案設定一個list，叫做name_of_interest
names_of_interest=[]

# 第一個for迴圈表示all_data內的每一個元素name。
for names in all_data:
    
# 第二個for迴圈表示all_data內的name在e>=2的條件下，才可以成為enough_as這個list的元素，而且元素是name。
    enough_as=[name for name in names if name.count('e')>=2]

# 找到enough_as的value後，其實答案也出來了，再透過extend()增加多個元素給name_of_interest這個List。
    names_of_interest.extend(enough_as)
    
print(f'names_of_interest: {names_of_interest}')


# In[35]:


#其實答案可以用一句話就寫完，迴圈的迴圈，還有一樣的value，構成了巢式list包含式。
# result的目標要找到name。
# 第一個迴圈代表all_date內的每一個值。
# 第二個迴圈代表真正的答案在每一個值的裡面，條件必須是e>=2，就可以找到答案了！


result=[name for names in all_data for name in names if name.count('e')>=2]
result


# In[39]:


# 將一個包含許多tuple的list，變成一條單一的list。


# In[45]:


some_tuples=[(1,2,3),(4,5,6),(7,8,9)]

#第一個ｘ代表one_list內的value。
#第一個for迴圈代表 some_tuples這個 list內的每一個tuple。
#第二個for迴圈代表 one_list的value x來自於tuple in some_tuples。

one_list=[x for tup in some_tuples for x in tup]
print(f'one_list= {one_list}')


# In[46]:


a=[('a','b','c'),('d','e','f'),('g','h','i')]
b=[x for y in a for x in y ]
print(f'b= {b}')


# In[53]:


one_list=[]

# 由大到小，第一個迴圈先找到每一個tuple，第二個迴圈再找到每一個tuple內單一的value x，最後再把每次增加的x透過append()增加給one_list()
for tup in some_tuples:
    for x in tup:
        one_list.append(x)
one_list

