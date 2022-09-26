#!/usr/bin/env python
# coding: utf-8

# In[131]:


## List Introduction


# In[132]:


# list: 長度可變，內容也可以變，使用 [] 定義list，或透過 list() 型態函數定義list。


# In[133]:


a_list=[1,2,3,4,5]
tup=('a','b','c','d','e')
b_list=list(tup)
print(f'b_list: {b_list}')


# In[134]:


# [] : 可以透過中括號存取list中的值外，還可以變換值。


# In[135]:


b_list[0]='apple'
print(f'b_list: {b_list}')


# In[136]:


# list常用來實體化一個疊代器或是產生器述句。


# In[137]:


a=range(10)
print(f'a: {a}')
print(f'list(a): {list(a)}')


# In[138]:


# append() 可以加入尾端元素。(一次只能加入一個元素（one tuple/list)


# In[139]:


print(f'b_list: {b_list}')
b_list.append(['f','g','h'])
print(f'b_list: {b_list}')


# In[140]:


# insert()可以將元素插入到list中任何位置。


# In[141]:


b_list.insert(3,'different')
print(f'b_list: {b_list}')


# In[142]:


# 注意到insert()的動作計算量比append()來的多，如果要增加最前面或最後面，可使用collections.deque


# In[143]:


# pop() 可以移除指定位置的元素，並回傳該元素內容。


# In[144]:


b_list.pop(4) 


# In[145]:


print(f'b_list: {b_list}')


# In[146]:


# remove() 可以刪除第一個符合的元素。


# In[147]:


b_list.append('apple')
print(f'b_list: {b_list}')


# In[148]:


b_list.remove('apple')


# In[149]:


print(f'b_list: {b_list}')


# In[150]:


# 透過 in, not in 可以用來檢查是否有指定值。不過，list的執行效率比dict, set慢許多，因為list是線性掃描; dict, set是hash table。


# In[151]:


3 in a_list


# In[152]:


'app' not in b_list


# In[153]:


# + 可以連結2個list


# In[154]:


a_list + b_list


# In[155]:


# extend() ：可用來一次加入多個元素。


# In[156]:


a_list.extend([6,7,8,True])
print(f'a_list: {a_list}')


# In[157]:


# 由於加號需要開一個新的list，在效率上，使用extend()會更好。


# In[158]:


# sort(): 可以in-place不建立新物件的進行排序。


# In[159]:


a=[8,9,4,6,2,0]
a.sort()


# In[160]:


a


# In[161]:


# sort(): 可以輸入sort key，例如len()


# In[162]:


b=['hi','ocean','sky','blue','fantastic']
b.sort(key=len)


# In[163]:


b


# In[164]:


# bisect(): 可以對已排序的list進行二元搜尋與插入，並不會破壞原本的排序。


# In[165]:


# bisect.bisect 用來找到元素應該插入的正確位置。 bisect.insort 用來實際插入該元素。


# In[166]:


import bisect


# In[170]:


print(f'a={a}')
bisect.bisect(a,1) # bisect.bisect: 搜尋結果為1可插入在index=1的位置。


# In[171]:


bisect.insort(a,1)
print(f'a= {a}')  # bisect.insort()： 執行1插入到a內的指令。


# In[169]:


# bisect() 本身並不會先排序好list()再執行插入，建議可以搭配sort()，先行整理好資料，再透過bisect()將元素插到正確的位置。

