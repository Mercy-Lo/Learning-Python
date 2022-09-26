#!/usr/bin/env python
# coding: utf-8

# In[57]:


## enumerate(), sorted(), zip(), reversed()


# In[58]:


# enumerate(): 會回傳（index, value)的序列


# In[59]:


a_list=['apple','berry','city','diverse','eliminate']
b={}
for i,v in enumerate(a_list):
    b[v]=i
print(b)


# In[60]:


# enumerate() 的for 迴圈，i,v是個變數，可以置換為其他字母，但是順序很重要，前面的ｉ代表index，置換後會有相反的結果。


# In[61]:


a_list=['apple','berry','city','diverse','eliminate']
b={}
for c,d in enumerate(a_list):
    b[c]=d
print(b)


# In[62]:


# sorted(): 可以將任何序列排序後，以新的序列回傳。


# In[63]:


# sorted()可以回傳新的序列;sort()僅能原地排序，不能新增新的list。


# In[64]:


sorted([20,100,500,300,600,150])


# In[65]:


a=[20,100,500,300,600,150]
a.sort()
print(f'a= {a}')


# In[66]:


# sorted()與sort()只能使用在list，不能將tuple排序。 


# In[67]:


# sorted()可以對文字string進行字母排序，sort()僅能針對文字序列string list進行排序。


# In[68]:


sorted('happy birthday!')


# In[69]:


b=['a','e','b','f']
b.sort()
print(f'b= {b}')


# In[70]:


# zip(): 可以將tuple, list內的元素進行配對，建立一個新的tuple list。


# In[71]:


# zip(a,b)本身為tuple list，若要呈現出資料，需要list()的協助。


# In[72]:


a=['white','black','red']
b=['yellow','orange','green']
ab_list= zip(a,b)
print(f'ab_list= {list(ab_list)}')


# In[73]:


# zip() 會根據要合併的tuple, list找到最小數量的合併呈現方式，多出來不能配對的值，就不會顯現。


# In[74]:


c=['beautiful','ugly']
print(f'abc_list= {list(zip(a,b,c))}')


# In[75]:


# zip() 可以疊代多個序列，也可以與enumerate合併使用。


# In[76]:


a=['white','black','red']
b=['yellow','orange','green']
for i, (a,b) in enumerate(zip(a,b)):
    print('{0}:{1},{2}'.format(i,a,b))


# In[77]:


a=['white','black','red']
b=['yellow','orange','green']
c=['beautiful','ugly']
for i, (a,b,c) in enumerate(zip(a,b,c)):
    print('{0}:{1},{2},{3}'.format(i,a,b,c))


# In[78]:


# zip(*list): 可以將合併後的list, tuple還原成原先的樣貌。


# In[79]:


d=['John','Andrew','David']
e=[60,20,30]
employee=list(zip(d,e))
employee


# In[80]:


name,age=zip(*employee)
print(f'name= {name}')
print(f'age= {age}')


# In[81]:


# reversed(): 會對序列的反序做疊代。


# In[82]:


list(reversed(range(10)))

