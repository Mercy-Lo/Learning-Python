#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Pandas: 被設計來處理表格式和異值資料集。


# In[7]:


# Pandas 的資料結構: Series & DataFrame


# In[8]:


# Series: 一維陣列，為含有一個值的序列，以及資料標籤index。


# In[9]:


import pandas as pd


# In[10]:


from pandas import Series, DataFrame


# In[11]:


obj= pd.Series([4,5,-1,2,0])
obj


# In[12]:


# 由上可知，在Series資料格式中，左邊是index，右邊是值。


# In[13]:


# values, index： 可知道該Series的值與index。


# In[14]:


obj.values


# In[15]:


obj.index


# In[16]:


# 除了預設值的Index，你還可以自己設定index。


# In[17]:


obj2=pd.Series([5,6,-3,7,2], index=['d','b','a','c','e'])
obj2


# In[18]:


obj2.index


# In[19]:


# 使用[index]，可以取得Series的值。


# In[20]:


obj2['a']


# In[21]:


obj2[['a','b','c']] #注意如果要取多個值，也需要使用[]。


# In[22]:


# 使用布林判斷式找到值。


# In[23]:


obj2[obj2>0]


# In[24]:


# 使用加減乘除，每一個值都會跟著變化。


# In[25]:


obj2*2


# In[26]:


# 也可以對Series使用全域函式。


# In[27]:


import numpy as np
np.exp(obj2)  #exp代表ｅ的ｘ次方。


# In[28]:


# in: 確認Series內有無特定值。


# In[29]:


'f' in obj2


# In[30]:


'e' in obj2


# In[31]:


# Python的Dict可以用來建立Series


# In[32]:


a_dict={'Orange':1000, 'Apple':2000, 'Banana':3000, 'Grape':4000, 'Watermelon':5000}


# In[33]:


obj3= pd.Series(a_dict)
obj3


# In[34]:


# Series的順序可以透過[]顯示。


# In[35]:


a_list=['Apple','Banana','Grape','Orange','Peach','Watermelon']


# In[36]:


obj4=pd.Series(a_dict, index=a_list)
obj4


# In[37]:


# NaN表示遺失或是not available。


# In[38]:


# isnull, notnull可以偵測Null值。


# In[39]:


pd.isnull(obj4)


# In[40]:


pd.notnull(obj4)


# In[41]:


obj4.isnull()


# In[42]:


# Series可以彼此加減乘除。


# In[43]:


obj3+obj4


# In[44]:


# Series本身有name屬性，index也會有name屬性。


# In[45]:


obj4.name='Price'


# In[46]:


obj4.index.name='Fruit'


# In[47]:


obj4


# In[48]:


# Series的Index可以直接給值修改。


# In[49]:


obj


# In[50]:


obj.index=['Math', 'English', 'Chinese', 'PE', 'Science']
obj


# In[51]:


# DataFrame: 一個含有資料的方形資料表，裡面包括一堆欄位，每個欄位可以是不同的型態（布林、字串、數字）。有列有欄有index。


# In[52]:


data={'fruit':['Apple','Banana','Grape','Orange','Peach','Watermelon'],
     'weekday':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],
     'price':[1000,2000,3000,4000,5000,6000]}
frame= pd.DataFrame(data)
frame


# In[53]:


# head(): 遇到大型資料庫，可以選取開頭前5列。


# In[54]:


frame.head()


# In[55]:


# columns=[] : 可以用來排序欄位名稱。


# In[56]:


pd.DataFrame(data,columns=['weekday','price','fruit'])


# In[57]:


# index=[] ：可以用來調整index名稱。


# In[58]:


frame2= pd.DataFrame(data,columns=['weekday','price','fruit','farmer'], index=['a','b','c','d','e','f'])
frame2


# In[59]:


# Frame[ 'column_name' ] 或是 Frame.colunm_name: Dataframe中可以使用[]取出一整個欄位。


# In[60]:


frame2['weekday']


# In[61]:


frame2.fruit


# In[62]:


# loc[]: 可以取出index的所有值。


# In[63]:


frame2.loc['b']


# In[64]:


# 取出一個欄位名稱，可以填入值。


# In[65]:


frame2['farmer']=['Nicole','Eason','Juan','Teresa','Johnny','Patrick']
frame2


# In[66]:


frame2=pd.DataFrame(data,columns=['rank','farmer','weekday','fruit','price'],
                   index=['a','b','c','d','e','f'])
frame2['farmer']=['Nicole','Eason','Juan','Teresa','Johnny','Patrick']
frame2


# In[67]:


# 可以透過np.arange()回填值。


# In[68]:


import numpy as np
frame2['rank']=np.arange(1,7)
frame2


# In[69]:


# 可以指定值給特定index，沒有指定的地方會呈現NaN。


# In[70]:


val=pd.Series([7000,8000,9000], index=['b','d','f'])


# In[71]:


frame2['price']=val
frame2


# In[72]:


# 對於不存在的欄位給值，就會建立一個新的欄。


# In[73]:


frame2['taste']=frame2.farmer=='Teresa'
frame2


# In[74]:


# del 可以刪除欄位！


# In[75]:


del frame2['taste']


# In[76]:


frame2.columns


# In[77]:


# dict中包包含dict:加入dataframe後，最外層的dict key會成為欄index，內層的key成為列index。


# In[78]:


farmer={'Nicole':{'age':30, 'gender':'Female'}, 
        'Eason':{'age':40, 'gender':'Male'},
        'Juan':{'age':50, 'gender':'Male'},
        'Teresa':{'age':60, 'gender':'Female'},
        'Johnny':{'age':70, 'gender':'Male'},
        'Patrick':{'age':80, 'gender':'Male'}}


# In[79]:


frame3=pd.DataFrame(farmer)
frame3


# In[80]:


# Ｔ：你可以轉置一個DataFrame，互換欄與行。


# In[81]:


frame3.T


# In[82]:


# index若增加一個不存在的欄位，view會出現該欄位，但是實體不會增加。


# In[83]:


pd.DataFrame(farmer, index=['age','gender','experience'])


# In[84]:


frame3


# In[85]:


# 可以透過[]與slice，切分出另一個dataframe。


# In[86]:


pdata={'Nicole':frame3['Nicole'][:1],
      'Eason':frame3['Eason'][:2]}


# In[87]:


pd.DataFrame(pdata)


# In[88]:


# 可以幫index, colunms 命名。 


# In[89]:


frame3.index.name='personal_information' ; frame3.columns.name='name'


# In[90]:


frame3


# In[91]:


# 可以回傳values


# In[92]:


frame3.values


# In[93]:


frame2.values


# In[94]:


# index物件：你在建立的Series, DataFrame時使用的標籤會被轉成一個物件。


# In[95]:


obj=pd.Series(range(3), index=['a','b','c'])


# In[96]:


index=obj.index


# In[97]:


index


# In[98]:


index[1:]


# In[99]:


# index是immutable不可以改變的。


# In[100]:


index[1]='d'


# In[ ]:


# index物件可以拿來搭配其他資料結構。


# In[ ]:


labels=pd.Index(np.arange(3))


# In[ ]:


labels


# In[ ]:


obj2=pd.Series([2,4,6],index=labels)


# In[ ]:


obj2


# In[ ]:


# index的特性很像固定長度的set。 透過in可以確認index,欄位名稱是否存在。


# In[ ]:


frame3


# In[ ]:


frame3.columns


# In[ ]:


'Johnny' in frame3.columns


# In[ ]:


'experience' in frame3.index


# In[ ]:


# pandas的index和Python的set不一樣在於他可以有重複的標籤。


# In[101]:


dup_labels=pd.Index(['a','a','b','b','c','c'])
dup_labels


# In[102]:


dup_labels.unique() #可以取得不重複的index。


# In[103]:


labels2=pd.Index(['d','e','f'])
dup_labels.append(labels2) # 使用append(index)，括號內必須是index。


# In[104]:


# 重做索引


# In[105]:


# reindex(): 建立新物件時，附帶新索引資料。


# In[106]:


obj=pd.Series([2,4,-6,8,-10],index=['e','d','c','b','a'])
obj


# In[107]:


# 使用reindex時，如果對應的index沒出現，那麼值就會連帶消失，如果index多一個，NaN就會出現在表格內。


# In[108]:


obj2=obj.reindex(['b','c','d','e','f'])
obj2


# In[109]:


# method(): 可以向內插入值。ffill: 插入跟前面一樣的值。


# In[110]:


obj3=pd.Series(['Red','Orange','Green','Blue'],index=[0,1,3,4])
obj3


# In[111]:


obj3.reindex(range(6),method='ffill')


# In[112]:


# 你可以對列、欄同時進行reindex，如果單純只傳一個序列的話，那重做索引的對象就會是列。


# In[113]:


frame=pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['Tree','Forest','Grass'])
frame


# In[114]:


frame2=frame.reindex(['a','b','c','d']) # 什麼都沒放，就會修改index。
frame2


# In[115]:


nature=['Flower','Wind','Seed']
frame.reindex(columns=nature) #放上columns，就可以針對欄位名稱做修改。


# In[116]:


# loc可以用來提取dataframe的值。


# In[117]:


frame.loc[['a','c','d']]


# In[118]:


# 指定軸刪除資料


# In[119]:


# drop(): 可以用來移除特定行。


# In[120]:


obj=pd.Series(np.arange(5),index=['a','b','c','d','e'])
obj


# In[121]:


new_obj=obj.drop('c')


# In[122]:


new_obj


# In[123]:


obj.drop(['d','e'])


# In[124]:


obj


# In[125]:


data=pd.DataFrame(np.arange(16).reshape(4,4),index=['Tea','Milktea','Juice','Cola']
                  ,columns=['one','two','three','four'])
data


# In[126]:


data.drop(['Milktea','Juice'])


# In[127]:


# 如果想要刪除欄位，axis=1，指的就是欄，也可以寫axis='columns'，axis=0(預設值)，就是列。


# In[128]:


data.drop('two',axis=1)


# In[129]:


data.drop('four',axis='columns')


# In[130]:


data


# In[131]:


# inplace: 透過True，真實的將資料從母檔移除。


# In[132]:


obj.drop('c',inplace=True)


# In[133]:


obj


# In[134]:


# 索引、選擇和過濾


# In[142]:


# 相較於Python 陣列，Series除了可以用數字找出值，也可以使用非數字的index找到值。


# In[143]:


obj=pd.Series(np.arange(4),index=['a','b','c','d'])
obj


# In[144]:


obj['b']


# In[145]:


obj[1]


# In[146]:


obj[2:4]


# In[147]:


obj[['b','a','d']]


# In[140]:


obj[[1,3]]


# In[141]:


obj[obj<2]


# In[148]:


# 用標籤做的切片和Python有些差異，並不會排除尾端。


# In[150]:


obj[['b','c']]


# In[151]:


# 如果要給值的畫，就會修改Sereis中對應的區域。


# In[152]:


obj[['b','c']]=5


# In[153]:


obj


# In[154]:


data=pd.DataFrame(np.arange(16).reshape(4,4),
                  index=['Apple','Sony','Samsung','HTC'], columns=['one','two','three','four'])


# In[155]:


data


# In[156]:


data['two']


# In[157]:


data[['three','one']]


# In[158]:


data[:2]


# In[159]:


data[data['three']>5]


# In[160]:


# 使用布林值做索引


# In[161]:


data<5


# In[162]:


data[data<5]=0


# In[163]:


data


# In[164]:


# 用loc, iloc做選擇


# In[167]:


# 順序必須是loc[index,columns]，內容物必須為index與columns的名稱。


# In[168]:


data.loc['Apple',['two','three']]


# In[170]:


# 順序必須是iloc[index, columns]，內容物必須為數字。


# In[171]:


data.iloc[3,[3,0,1]]


# In[174]:


data.iloc[2]


# In[175]:


data.iloc[[1,2],[3,0,1]]


# In[176]:


# : 也支援loc, iloc。


# In[178]:


data.loc[:'Sony','two']


# In[187]:


data.iloc[:,:3][data.three>5]


# In[191]:


# 整數索引


# In[192]:


ser=pd.Series(np.arange(3))


# In[193]:


ser


# In[197]:


# 系統無法判斷此時是要找index的名稱還是index where。


# In[198]:


ser[-1]


# In[199]:


# 把index換成非整數後，就不會混淆了。


# In[202]:


ser2=pd.Series(np.arange(3),index=['a','b','c'])
ser2


# In[203]:


ser2[-1]


# In[204]:


# 為保持一致性，當你想使用整數去取得某個值，可使用loc(標籤用）, iloc（整數用）。


# In[205]:


ser.iloc[-1]


# In[206]:


ser.loc[:1]

