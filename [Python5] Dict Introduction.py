#!/usr/bin/env python
# coding: utf-8

# In[91]:


## Dict Introduction


# In[92]:


# dict: 常被稱為hash map, associative array, 可以儲存任意大小的鍵值對(key-value pair)。
# 顯示方式： 大括號{}加上冒號分隔鍵與值。


# In[93]:


d1={'a':1,'b':2,'c':3,'d':True, ('e','f','g'):'Iceland'}
d1


# In[94]:


# [ ] 可以存取、插入或設定dict中的元素。


# In[95]:


d1['h']=4
d1


# In[96]:


d1[10]=100
d1


# In[97]:


d1['d']


# In[98]:


# in 可以檢查key有沒有在dict內。


# In[99]:


'a' in d1


# In[100]:


('e','f','g') not in d1


# In[101]:


# del dict[], dict.pop() 可以刪除值。 pop可以存取刪除的元素。


# In[102]:


del d1['h']


# In[103]:


d1


# In[104]:


d1.pop(10)


# In[105]:


d1


# In[106]:


# keys(), values(): 回傳dict內的keys,values，需搭配list()一起使用。


# In[107]:


list(d1.keys())


# In[108]:


list(d1.values())


# In[109]:


# update() 可以合併2個dict。


# In[110]:


d1.update({10:100,20:200,30:300})
d1


# In[111]:


# update() 會原地更新資料，如果key值一樣，會直接蓋過去。


# In[112]:


d1.update({'a':2, 'b':4, 'c':6})
d1


# In[113]:


# dict 本質上由2個tuple構成，可以接受2個range()


# In[114]:


d2=dict(zip(range(7),reversed(range(7))))
d2


# In[115]:


#get(), pop() 可以回傳預設值。


# In[116]:


a=d1.get('a')
a


# In[117]:


b=d1.pop('b')
b


# In[118]:


# 如果key不存在，get()回傳none, pop()回傳？


# In[119]:


x=d1.get('x')
x


# In[120]:


y=d1.get('y')
y


# In[121]:


words=['Alice','Anthea','Bruce','Bean','Bill']
by_letter={}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter]=[word]
    else:
        by_letter[letter].append(word)


# In[122]:


by_letter


# In[123]:


# collections內的defaultdict可以建立如上的序列。


# In[124]:


from collections import defaultdict


# In[125]:


by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)


# In[126]:


by_letter


# In[127]:


# dict合法的key型態：必須是immutable, 可以為int, float, string, tuple


# In[128]:


# hash(): 可以用來檢查是否可以成為dict的key。


# In[129]:


# string, integer, float, boolean, tuple 都可以是dict的key, 但是list不行。


# In[130]:


hash('a')


# In[131]:


hash((1,2))


# In[132]:


hash(3.14)


# In[133]:


hash(True)


# In[134]:


hash([3,4])


# In[135]:


# 如果希望list成為key，可以將list轉為tuple，即可成為dict的key。


# In[137]:


d3={}
d3[tuple([1,2,3])]=100
print(f'd3= {d3}')

