#!/usr/bin/env python
# coding: utf-8

# In[56]:


## Set Introduction


# In[57]:


# set 是無序不重複元素的集合。呈現方式：set函式或用中括號寫成set常數。


# In[58]:


set([5,5,5,7,7,1,1,1])


# In[59]:


{0,0,0,5,5,2,2,8,1}


# In[60]:


# set 支援數學上的集合運算，像是聯集、交集、差集、對稱差等計算。


# In[61]:


# union() 或是二元運算子| ，可以將兩個集合做不重複的連集。


# In[62]:


a={1,2,3,4,5}
b={5,6,7,8}
a.union(b)


# In[63]:


a|b


# In[64]:


# ＆ 或是 intersection() 可以取出同時存在於２個set中的元素。


# In[65]:


a.intersection(b)


# In[66]:


a & b


# In[67]:


# 所有的集合運算子都有對應的in-place版本，可以將結果直接取代左側的集合 ->更有效率。


# In[68]:


# add() 將元素加入集合。


# In[69]:


a.add(0)
a


# In[70]:


# clear() 將集合a清空，丟棄所有元素。


# In[71]:


a.clear()
a


# In[72]:


a=set([0,1,2,3,4,5,6,6])
a


# In[73]:


# remove() 移除特定元素。


# In[74]:


a.remove(6)
a


# In[75]:


# pop() 從集合中移除任意元素，如果集合為空，會丟出keyerror例外。


# In[76]:


a.pop()
a


# In[77]:


a.pop()
a


# In[78]:


# update() 或是 |= 代表指定a為a與b的聯集。


# In[79]:


b


# In[81]:


a.update(b)
a


# In[83]:


a |= b
a


# In[84]:


# intersection_update() 或是 &= 代表a為a與b的交集。


# In[85]:


a={2, 3, 4, 5}
b={5, 6, 7, 8}
a.intersection_update(b)
a


# In[86]:


a={2, 3, 4, 5}
b={5, 6, 7, 8}
a &= b
a


# In[87]:


# difference() 或是 a-b 代表在集合a但是不在集合b的元素。


# In[90]:


a={2, 3, 4, 5}
b={5, 6, 7, 8}
a.difference(b)


# In[91]:


a={2, 3, 4, 5}
b={5, 6, 7, 8}
a-b


# In[92]:


# difference_update() 或是 a-=b 代表指定a的內容為在集合a但是不在集合b的元素。


# In[93]:


a={2, 3, 4, 5}
b={5, 6, 7, 8}
a.difference_update(b)
a


# In[94]:


a={2, 3, 4, 5}
b={5, 6, 7, 8}
a -= b
a


# In[96]:


# symmetric_difference() 或是 a^b 代表在集合a、b中的所有元素，但是不能同時存在。


# In[97]:


a={2, 3, 4, 5}
b={5, 6, 7, 8}
a.symmetric_difference(b)


# In[98]:


a={2, 3, 4, 5}
b={5, 6, 7, 8}
a ^ b


# In[99]:


# symmetric_difference_update() 或是 a^=b 代表指定集合a的內容為a,b中的所有元素，但是不能同時存在。


# In[101]:


a={2, 3, 4, 5}
b={5, 6, 7, 8}
a.symmetric_difference_update(b)
a


# In[103]:


a={2, 3, 4, 5}
b={5, 6, 7, 8}
a ^= b
a


# In[104]:


# issubset() 如果集合a所有的元素都包含在b中，則回傳True。


# In[105]:


a={4,5,6}
b={1,2,3,4,5,6}
a.issubset(b)


# In[106]:


# issuperset() 如果集合b所有的元素都包含在a中，則回傳True。


# In[107]:


a={4,5,6,7}
b={5,6}
a.issuperset(b)


# In[108]:


# isdisjoint() 如果a,b都沒有交集，則回傳True。


# In[109]:


a={2,3,4}
b={7,8,9}
a.isdisjoint(b)


# In[110]:


# copy() 可以用來複製set


# In[111]:


c=a.copy()
c |=b
c


# In[114]:


a={1,2,3,4}
b={2,3,4,5}
d = a.copy()
d &= b
d


# In[115]:


# set的元素通常都是immutable，如果希望將list放進set，建議可以把list轉為tuple。


# In[116]:


e={tuple([1,2,3,4])}
e


# In[117]:


# 集合相等必須兩個set的元素都符合。


# In[123]:


{1,2,3} == {3,2,1}

