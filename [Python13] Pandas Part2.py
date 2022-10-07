#!/usr/bin/env python
# coding: utf-8

# In[1]:


#算數運算與資料對齊


# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


s1= pd.Series([3,6,9,12],index=['b','a','d','c'])


# In[5]:


s2= pd.Series([4,8,12,16,20],index=['a','b','c','e','f'])


# In[6]:


s1


# In[7]:


s2


# In[8]:


s1+s2


# In[9]:


# 資料沒對上，相加的值就會是NaN。


# In[10]:


df1= pd.DataFrame(np.arange(9).reshape((3,3)), columns=list('bcd'),index=['sun','moon','lake'])


# In[11]:


df2= pd.DataFrame(np.arange(12).reshape((4,3)), columns=list('bde'),index=['chocolate','sun','moon','cake'])


# In[12]:


df1


# In[13]:


df2


# In[14]:


df1+df2


# In[15]:


# 只有moon, sun, b,d 產生交集的地方有數字，其餘都是NaN。


# In[16]:


df1= pd.DataFrame({'A':[1,2]})


# In[17]:


df2= pd.DataFrame({'B':[3,4]})


# In[18]:


df1


# In[19]:


df2


# In[20]:


df1-df2


# In[21]:


# 算數運算與填值


# In[22]:


df1= pd.DataFrame(np.arange(12).reshape(3,4),columns=list('abcd'))


# In[23]:


df2= pd.DataFrame(np.arange(20).reshape(4,5),columns=list('abcde'))


# In[24]:


df1


# In[25]:


df2.loc[1,'b',]=np.nan
df2


# In[26]:


df1+df2


# In[27]:


# add(frame, fill_value=?) ：可以將NaN的地方，用0取代。


# In[28]:


df1.add(df2,fill_value=0)


# In[29]:


# 倒數: 1/df1=df1.rdiv(1)


# In[30]:


1/df1


# In[31]:


df1.rdiv(1)


# In[32]:


# 可以透過reindex把欄位數跟df2切齊，並且透過fill_value，把NaN改為0。


# In[33]:


df1.reindex(columns=df2.columns, fill_value=0)


# In[34]:


# frame的加減運算


# In[35]:


df1.add(df2)


# In[36]:


df1.radd(df2)


# In[37]:


df1.sub(df2) #減法


# In[38]:


df1.rsub(df2)


# In[39]:


df1.div(df2) #除法


# In[40]:


df1.floordiv(df2) #整除


# In[41]:


df1.mul(df2) #相乘


# In[42]:


df1.pow(df2) #取冪


# In[43]:


# 在DataFrame與Series之間的運算


# In[44]:


arr=np.arange(12).reshape(3,4)
arr


# In[45]:


arr[0]


# In[46]:


arr-arr[0]


# In[47]:


# 當進行減法時，每一列都會進行一次，這個動作被稱為廣播（broadcasting)。


# In[48]:


frame=pd.DataFrame(np.arange(12).reshape(4,3),columns=list('bde'),index=['Light','Dark','Full','Empty'])


# In[49]:


series=frame.iloc[0]


# In[50]:


frame


# In[51]:


series


# In[52]:


frame-series  #每一列都被減一次，稱為廣播。


# In[53]:


series2=pd.Series(range(3),index=['b','e','f'])


# In[54]:


frame+series2


# In[55]:


series3=frame['d']


# In[56]:


frame


# In[57]:


series3


# In[58]:


frame.sub(series3,axis='index')


# In[59]:


# apply和applymap


# In[60]:


frame= pd.DataFrame(np.random.randn(4,3),
                    columns=list('bde'),index=['Giant','Specialized','Trek','Raise & Muller'])


# In[61]:


frame


# In[62]:


np.abs(frame)


# In[63]:


f= lambda x: x.max() -x.min()


# In[64]:


# apply(funciton, axis=0) 因為axis=0是預設值，所以計算出來為欄的最大與最小差異。


# In[65]:


frame.apply(f)


# In[66]:


# apply(funciton, axis=1) 因為有特別說明axis='columns'，所以計算出來為列的最大與最小差異。


# In[67]:


frame.apply(f,axis='columns')


# In[68]:


# 除了計算值出來外，也可以透過def回傳dataframe/Series


# In[69]:


def f(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])


# In[70]:


frame.apply(f)


# In[71]:


format= lambda x: '%.2f' % x


# In[72]:


# applymap(): 用來執行lambda的函式。


# In[73]:


frame.applymap(format)


# In[74]:


# map可以對Series級別做運作。


# In[75]:


Series1=pd.Series(np.arange(5), index=['a','b','c','d','e'])


# In[76]:


frame['b'].map[format]


# In[ ]:


# 排序和排名


# In[ ]:


# sort_index(): 可以幫index()排名。


# In[ ]:


obj=pd.Series(range(4),index=['d','a','b','c'])


# In[ ]:


obj.sort_index()


# In[77]:


frame=pd.DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],columns=['d','a','b','c'])
frame


# In[78]:


frame.sort_index()


# In[79]:


frame.sort_index(axis=1)


# In[80]:


# sort_index(axis=1, ascending=boolean)： 除了可以讓column排序外，可以指定column要由小到大(預設值），還是由大到小排序。


# In[81]:


frame.sort_index(axis=1,ascending=False)


# In[82]:


frame.sort_index(axis=1,ascending=True)


# In[83]:


# sort_values: 可以對Series的值做排序。


# In[84]:


obj=pd.Series([-3,6,9,-12,15])


# In[85]:


obj.sort_values()


# In[86]:


# 如果有NaN，會被排在最後面。


# In[87]:


obj=pd.Series([np.nan, 2,-4,np.nan,6,-8,np.nan,10])


# In[88]:


obj.sort_values()


# In[89]:


frame=pd.DataFrame({'b':[5,-10,15,-20],'a':[7, 14,-21,-28]})
frame


# In[90]:


# frame的排序可以指定某一欄位做由小到大的排序。


# In[91]:


frame.sort_values(by='b')


# In[92]:


# frame也可以依據多個欄位做排序，寫入[x,y]即可。


# In[93]:


# 寫入的順序，會影響以誰先做排序。


# In[94]:


frame.sort_values(by=['a','b'])


# In[95]:


# rank(): 可以給Series排名，從1開始排名，遇到一樣大的數值時，會採用他們的平均排名值。


# In[96]:


obj=pd.Series([7,-5,7,6,-4,6,5])


# In[97]:


# 這裡的index代表value原本在Series的所在位置，比如說index=0，指的是7這個數字。
# 因為7在這個數列中，並列第6名與第7名，所以排名顯示為6.5。
# -5在Series中是最小的，因此顯示為第1名。


# In[98]:


obj.rank()


# In[99]:


# rank(method= first()): 代表即時是一樣的值，先出現，就先排名，也就不用平均排名值了。


# In[100]:


obj.rank(method='first')


# In[101]:


# rank(ascending=Boolean): 預設值為True，會由小到大排序，相反的話，會由大到小。
# rank(method='max'): 表示遇到一樣的值時，排名取2個最大的，由於7並列第1名與第2名，故顯示2。


# In[102]:


obj.rank(ascending=False, method='max')


# In[103]:


# rank(method='min'): 表示遇到一樣的值時，排名取2個最小的，由於7並列第6名與第7名，故顯示6。


# In[104]:


obj.rank(method='min')


# In[105]:


# rank(method='dense'): 表示遇到一樣的值時，排名取最小的，此外，不可以跳過，要接續排名。


# In[106]:


obj.rank(method='dense')


# In[107]:


frame= pd.DataFrame({'b':[2,4,6,8,-10],'a':[4,8,12,16,-20],'c':[5,10,15,20,-25]})
frame


# In[108]:


# rank(axis=1): 表示幫每行做排序。（橫向）


# In[109]:


frame.rank(axis='columns')


# In[110]:


# rank(): 預設值為axis=0，表示幫每欄做排序。（直向）


# In[111]:


frame.rank()


# In[112]:


# 軸index有重複標籤: 不論是Series, DataFrame的允許有重複的index標籤。


# In[113]:


obj=pd.Series(range(5),index=['a','a','b','b','c'])
obj


# In[114]:


obj.index.is_unique #表示index有重複值。


# In[115]:


obj['a']


# In[116]:


obj['c']


# In[117]:


df=pd.DataFrame(np.random.randn(4,3),index=['a','a','b','b'])
df


# In[118]:


df.loc['b']


# In[119]:


# 匯總和計算描述性統計量


# In[120]:


df=pd.DataFrame([[2,np.nan],[7,-4],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])


# In[121]:


df


# In[122]:


# sum(): 每欄加總。 sum(axis=1): 每列加總。


# In[123]:


df.sum()


# In[124]:


df.sum(axis='columns')


# In[125]:


# skipna=False: 在進行運算時，na通常會被忽略，但如果不想被忽略可以寫上skipna=False。


# In[126]:


df.mean(axis=1, skipna=False)


# In[127]:


#idxmax(): 回傳每一欄中，哪一個index呈現的值最大，並回傳index。


# In[128]:


df.idxmax()


# In[129]:


#idxmin(): 回傳每一欄中，哪一個index呈現的值最小，並回傳index。


# In[130]:


df.idxmin()


# In[131]:


#cumsum()=a, a+b, a+b+c, a+b+C+d, ...，在frame中，會呈現每欄的累進加總。


# In[132]:


df.cumsum()


# In[133]:


# describe(): 針對該frame，提供多個統計值。


# In[134]:


df.describe()


# In[135]:


# 如果資料不是數值，describe()會顯示另一種統計值。


# In[136]:


obj=pd.Series(['a','b','c','d','e']*4)


# In[137]:


obj.describe()


# In[138]:


# 相關係數與共變異數


# In[139]:


# 前置作業：增加一個新的環境：conda install pandas-datareader


# In[140]:


# 由於2017年Yahoo被Verizon收購，所以pandas-datareader無法使用。


# In[141]:


import pandas_datareader.data as web


# In[142]:


all_data= {'ticker': web.get_data_yahoo(ticker)
          for ticker in ['AAPL','IBM','MSFT','GOOG']}

price= pd.DataFrame({ticker: data['Adj Close']
                    for ticker, data in all_data.items()})

volume=pd.DataFrame({ticker: data['Volume']
                    for ticker, data in all_data.items()})


# In[143]:


returns= price.pct_change()


# In[144]:


returns.tail()


# In[145]:


# 目前是使用yfinance去連接yahoo股市的api


# In[146]:


# 在terminal輸入pip install yfinance 即可安裝


# In[147]:


import yfinance as yf


# In[148]:


# Yahoo的程式跑不動，先用隨機變數代替。


# In[149]:


frame= pd.DataFrame(np.random.randn(20).reshape(5,4), 
                    index=['2022-10-01','2022-10-02','2022-10-03','2022-10-04','2022-10-05'],
                    columns=['AAPL','GOOG','IBM','MSFT'])
frame


# In[ ]:


# corr():代表計算兩個series的關係係數。cov():計算兩個series的共變異數。


# In[150]:


frame['MSFT'].corr(frame['IBM']) #兩者高度正相關


# In[151]:


frame['AAPL'].cov(frame['GOOG']) #兩者低度負相關


# In[153]:


frame.MSFT.corr(frame['IBM']) #兩者高度正相關


# In[155]:


# 如果讓corr()直接與dataframe做搭配，會出現一個關係係數的矩陣。


# In[156]:


frame.corr()


# In[157]:


frame.cov()


# In[158]:


# corrwith(): 可以計算整欄或整列的相關係數。


# In[159]:


frame.corrwith(frame.IBM)


# In[162]:


# 如果是傳入整個frame，就會對應名稱相同的欄，進行變異數值運算。
# 需注意index要一致。


# In[175]:


frame2= pd.DataFrame(np.random.randn(20).reshape(5,4), 
                    index=['2022-10-01','2022-10-02','2022-10-03','2022-10-04','2022-10-05'],
                    columns=['TSML','GOOG','IBM','MSFT'])
frame2


# In[177]:


frame.corrwith(frame2)


# In[178]:


# 不重複值、個數計算和成員關係


# In[179]:


obj= pd.Series(['c','a','b','b','a','c','d','d','a'])


# In[183]:


# unique(): 可以取出不重複的值。


# In[184]:


uniques= obj.unique()
uniques


# In[187]:


uniques.sort() #將取出來的值做排序。


# In[188]:


uniques


# In[191]:


# value_counts(): 可以計算每個元素各有幾個重複值。


# In[197]:


obj.value_counts()


# In[200]:


# pd.value_counts(frame.values, sort=boolean) 可以直接對series的值進行個數加總，以及排序個數值。


# In[201]:


pd.value_counts(obj.values, sort=True)


# In[202]:


obj


# In[ ]:


# isnin()： 可以用來檢查該series有沒有括號內的元素，如此將形成一個布林判斷式。


# In[203]:


mask=obj.isin(['b','c'])


# In[204]:


mask


# In[206]:


obj[mask] #Series放入布林判斷式，會產生另一個子Series


# In[211]:


# get_index: 可以用來找出A_Series的index，套用在B_Series會呈現怎麼樣的array。


# In[212]:


to_match= pd.Series(['c','a','b','b','c','a']) #B_Series


# In[213]:


unique_vals= pd.Series(['c','b','a']) #A_Series(0,1,2)


# In[214]:


pd.Index(unique_vals).get_indexer(to_match) #將c=0, b=1, a=2的Index套用在B_Series上。


# In[234]:


data=pd.DataFrame({'Qu1':[1,3,4,3,4],
                   'Qu2':[2,3,1,2,3],
                   'Qu3':[1,5,2,4,4]}, 
                    index=['a','b','c','d','e'])
data


# In[240]:


# 最左手邊代表值，數字1在Qu1欄位出現了1次。


# In[241]:


result= data.apply(pd.value_counts)


# In[242]:


result


# In[243]:


# fillna(0): 如果表格出現NaN，就回填0。


# In[244]:


result= data.apply(pd.value_counts).fillna(0)
result

