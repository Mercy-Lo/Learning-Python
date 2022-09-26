#!/usr/bin/env python
# coding: utf-8

# In[212]:


## Tuple Introduction


# In[213]:


# Tuple 元件：是一個固定長度、immutable的Python序列物件。


# In[214]:


tup=1,2,3,4,5,6,7
print(f'tup: {tup}')


# In[215]:


# () 可以用來定義不同內容的tuple。


# In[216]:


nested_tup=('w','o'),('r','l','d')
print(f'nested_tup: {nested_tup}')


# In[217]:


# tuple() 可以將任何序列或疊代器轉化爲tuple。


# In[218]:


num_tup=tuple([1,2,3,4])
print(f'num_tup: {num_tup} ')


# In[219]:


str_tup=tuple('python')
print(f'str_tup: {str_tup}')


# In[220]:


# [] 可以存取tuple中的個別元素，0為Index的開頭。


# In[221]:


print(f'num_tup[3]: {num_tup[3]}')
print(f'str_tup[3]: {str_tup[2]}')


# In[222]:


# tuple 內的物件不可被修改。'tuple' object does not support item assignment


# In[223]:


print(f'num_tup: {num_tup}')
num_tup[0]=10


# In[224]:


# 如果tuple內存在list，可以針對list本身進行修改。


# In[225]:


tup=tuple(['cool',[1,2],False])
tup[1].append(3)
print(f'tup: {tup}')


# In[226]:


# 可以使用 + 將不同tuple連接起來。 文字(string)後面務必加上逗號, 才可以順利連成tuple。


# In[227]:


tup2=tup+('starfish',)+(4,5,6)+('ocean',)
print(f'tup2: {tup2}')


# In[228]:


# ＊可以重複tuple內的物件。


# In[229]:


print(f'tup: {tup*3}')


# In[230]:


# 提供一串變數給tuple，tuple會自動將值依序拆分給變數。


# In[231]:


print(f'num_tup: {num_tup}')
a,b,c,d=num_tup
print(d)


# In[232]:


# 拆分變數的功能，可以將變數內容互換。


# In[233]:


print(f'num_tup: {num_tup}')
a,b,c,d=num_tup
print(f'a={a}; b={b} ; c={c}; d{d}')
d,c,b,a=a,b,c,d
print(f'a={a}; b={b} ; c={c}; d{d}')


# In[234]:


# 拆分變數的時機：對list做疊代。


# In[235]:


seq=[(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    print('a={0},b={1},c={2}'.format(a,b,c))


# In[236]:


# *rest 可抓取任意位置、長度的list (rest可改為任何的英文字母或是底線_)


# In[237]:


print(f'str_tup: {str_tup}')
a,b,*_=str_tup
print(f'a,b= {a,b}')
print(f'_= {_}')


# In[ ]:


# .count可以計算tuple內物件的數量。


# In[238]:


print(f'tup:{tup*3}')
tup=tup*3
tup.count(False)


# In[ ]:





# In[ ]:




