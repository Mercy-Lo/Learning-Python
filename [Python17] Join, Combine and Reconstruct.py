#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 資料處理：連接、合併和重塑


# In[2]:


# 階層式索引 Hierarchical indexing


# In[3]:


import pandas as pd


# In[4]:


import numpy as np


# In[5]:


data=pd.Series(np.random.randn(9), index=[['a','a','b','b','c','c','d','d','d'],[1,2,3,1,2,3,1,2,3]])


# In[6]:


data


# In[7]:


data.index


# In[8]:


# 部份索引 partical indexing


# In[9]:


data['b']


# In[10]:


data['b':'c']


# In[11]:


data[['b','d']]


# In[12]:


data.loc[:,2]


# In[13]:


# unstack(): 可以將多重index的Seriest轉成DataFrame。


# In[14]:


data.unstack()


# In[15]:


# stack(): unstack()的相反。


# In[16]:


data.unstack().stack()


# In[17]:


# DataFrame也可以有多重的index與column name。


# In[18]:


frame=pd.DataFrame(np.arange(12).reshape(4,3), index=[['a','b','c','b'],['one','one','two','two']],
                   columns=[['Jerry','Tom','Jerry'],['Water','Tea','Tea']])


# In[19]:


frame


# In[20]:


frame.index.names=['alphabet','numbers']


# In[21]:


frame.columns.names=['names','drinks']


# In[22]:


frame


# In[23]:


# 多重index的dataframe，會將names, drinks視為index，僅能取出欄。


# In[24]:


frame['Jerry']


# In[25]:


frame['Jerry','Tea']


# In[26]:


# pd.MultiIndex.from_arrays: 可以將多個index儲存成物件。


# In[27]:


a=pd.MultiIndex.from_arrays([['Work','Lesiure','Rest'],['KPI','SCRUM','PDCA']], names=['matters','time_management'])


# In[28]:


a


# In[29]:


b_frame=pd.DataFrame(np.arange(6).reshape(3,2),index=a, columns=['a','b'])


# In[30]:


b_frame


# In[31]:


# 重排階層與依階層排序值


# In[32]:


frame


# In[33]:


# swaplevel(): 可以將Index前後對調，數值不會變動。


# In[34]:


frame.swaplevel('alphabet','numbers')


# In[35]:


# sort_index(): 讓數值按照index的level做排序。


# In[36]:


frame


# In[37]:


frame.sort_index(level=0) #按照alphabet排序。


# In[38]:


frame.swaplevel('alphabet','numbers').sort_index(level=1) #按照alphabet排序。


# In[39]:


# 指定階層統計資訊


# In[40]:


frame


# In[41]:


frame.sum(level='alphabet')


# In[42]:


frame


# In[43]:


frame.sum(level='names', axis=1)


# In[44]:


# 用DataFrame的欄當index


# In[45]:


frame=pd.DataFrame({'a':range(7), 'b': range(7,0,-1), 'c': ['one','one','one','two','two','two','two'],
                   'd':[0,1,2,0,1,2,3]})


# In[46]:


frame


# In[47]:


# set_index(['c','d']): 將c,d欄位轉變成frame2的index。


# In[48]:


frame2=frame.set_index(['c','d'])


# In[49]:


frame2


# In[50]:


# set_index(['c','d']): 預設值會把c,d欄位刪除，但是也可以寫上drop=False，就可以保留c,d欄位。


# In[51]:


frame.set_index(['c','d'],drop=False)


# In[52]:


# reset_index(): 和set_index()是相反的功能，會將frame2攤平成一維度的index。


# In[53]:


frame2


# In[54]:


frame2.reset_index()


# In[55]:


# 合併資料集合


# In[56]:


# DataFrame資料庫中的join動作


# In[57]:


df1= pd.DataFrame({'key':['b','b','a','a','c','c','b'], 'data1': range(7)})
df1


# In[58]:


df2=pd.DataFrame({'key':['a','b','d'],'data2':range(3)})
df2


# In[59]:


# pd.merge(df1,df2): 會依據兩個DataFrame共同的key進行值的合併。 
# 預設值為inner join，兩邊的共有值才會出現，故c,d不見了。


# In[60]:


pd.merge(df1,df2)


# In[61]:


# pd.merge(df1,df2, on='key')：可以透過on來指定要合併的欄位。


# In[62]:


pd.merge(df1,df2,on='key')


# In[63]:


df3=pd.DataFrame({'1key':['b','b','a','c','a','a','b'],'data1':range(7)})
df3


# In[64]:


df4=pd.DataFrame({'rkey':['a','b','d'],'data2':range(3)})
df4


# In[65]:


# pd.merge(df3, df4, left_on='1key', right_on='rkey'): 如果都沒有共同的key名稱，可以使用left_on, rigjt_on去定義連接的欄位。
# 因為以左邊為主，右邊如果對應不到的欄位，就會自動移除，像是df4的d就不會出現在合併的欄位內。


# In[66]:


pd.merge(df3,df4, left_on='1key', right_on='rkey')


# In[67]:


# pd.merge(df1, df2, how='outer') ：將預設值從inner改為outer，可以讓對應不到的值也出現。


# In[68]:


df1


# In[69]:


df2


# In[70]:


pd.merge(df1,df2, how='outer') #c,d就出現了！


# In[71]:


pd.merge(df1,df2, how='right') #出現df2所有值。


# In[72]:


pd.merge(df1,df2, how='left') #出現df1所有值。


# In[73]:


pd.merge(df1, df2, how='inner') # 兩邊都有共同值才會出現。


# In[74]:


# 多對多的合併: 會產生笛卡爾積，原本df1只有3個b，合併後出現6個b。


# In[75]:


df1=pd.DataFrame({'key':['b','b','a','c','a','b'],'data1':range(6)})
df1


# In[76]:


df2=pd.DataFrame({'key':['a','b','a','b','d'],'data2':range(5)})
df2


# In[77]:


pd.merge(df1,df2, on='key', how='left')


# In[78]:


pd.merge(df1,df2, how='inner')


# In[79]:


left=pd.DataFrame({'key1':['cool','cool','bar'],'key2':['one','two','one'],'lval':[1,2,3]})
left


# In[80]:


right=pd.DataFrame({'key1':['cool','cool','bar','bar'],'key2':['one','one','two','two'],'rval':[4,5,6,7]})
right


# In[81]:


# 如果遇到多個key，在寫入merge內的時候可以使用list。
# 在進行欄位名稱合併時，系統會自動忽略Index。


# In[82]:


pd.merge(left,right, on=['key1','key2'], how='outer')


# In[83]:


# 當兩個data有重複的欄位名稱，merge內建suffixes的功能，會在欄位後面補上_x, _y作為欄位區分。


# In[84]:


pd.merge(left, right, on='key1')


# In[85]:


# suffiexes=()：你也可以自己定義後綴的名稱要叫做什麼。


# In[86]:


pd.merge(left, right, on='key1', suffixes=('_left','_right'))


# In[87]:


# 依據index做合併


# In[88]:


left1=pd.DataFrame({'key':['a','b','a','a','b','c'],'value':range(6)})
left1


# In[89]:


right1=pd.DataFrame({'group_val':[3.5,7]}, index=['a','b'])
right1


# In[90]:


pd.merge(left1, right1, left_on='key', right_index=True)


# In[91]:


pd.merge(left1, right1, left_on='key', right_index=True, )


# In[92]:


# 如果要使用多個值進行merge，可以使用left_on('key1','key2')，只是要注意合併後的值如果要全數出現，需要how='outer'。


# In[93]:


lefth=pd.DataFrame({'key1':['Sun','Sun','Sun','Moon','Moon'],'key2':[2022,2021,2020,2021,2020],
                   'data':np.arange(5)})
lefth


# In[94]:


righth=pd.DataFrame(np.arange(12).reshape((6,2)),
               index=[['Moon','Moon','Sun','Sun','Moon','Moon'],[2021,2022,2022,2022,2021,2020]],
               columns=['event1','event2'])
righth.sort_index()


# In[95]:


# 只有key1, key2兩邊都有出現的值，才會出現在合併的表格內。


# In[96]:


pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True)


# In[97]:


# how='outer'，即使兩邊有不一樣的key1與key2，會使用NaN的方式全數出現。


# In[98]:


pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True, how='outer')


# In[99]:


# 如果merge的依據為左右兩個表的index，那麼可以寫入left_index=True, right_index=True


# In[100]:


left2=pd.DataFrame([[1,2],[3,4],[5,6]],index=['a','c','e'],columns=['Sun','Moon'])
left2


# In[101]:


right2=pd.DataFrame([[7,8],[9,10],[11,12],[13,14]],index=['b','c','d','e'],columns=['Sky','Cloud'])
right2


# In[102]:


pd.merge(left2, right2, how='outer', left_index=True, right_index=True)


# In[103]:


# join(): 本身合併的條件就是依據兩個表格的Index，如果是要用index合併表格，很簡單的直接寫上join即可。


# In[104]:


left2.join(right2,how='outer')


# In[105]:


left1


# In[106]:


right1


# In[107]:


# join(): 本身採用的預設合併原則為left join，會保留所有左邊表格的資料，以及採用Index為key值。
# left1與right1在合併時，系統會判定left1的連接條件是range(6)，對應到right1的a,b就會找不到值。


# In[108]:


left1.join(right1)


# In[109]:


# 因此要告訴系統left1的連接條件來自key，這樣才能對應到right1的a,b。


# In[110]:


left1.join(right1, on='key')


# In[111]:


another=pd.DataFrame([[7,8],[9,10],[11,12],[16,17]],index=['a','c','e','f'],columns=['Rainbow','Rain'])
another


# In[112]:


left2


# In[113]:


right2


# In[114]:


# 以left2的index=['a','c','e']為主，同時合併right2表格與another表格，left2會全數保留，其餘表格沒有對應到會消失。


# In[115]:


left2.join([right2,another])


# In[116]:


# how='outer'，即使沒有對應到left2的index，其餘沒有對到的值都會以NaN出現。


# In[117]:


left2.join([right2,another],how='outer')


# In[118]:


# 延軸做連接


# In[119]:


# np.concatenate(): 不同於加法，會將兩個表格做垂直或橫向的擴編。


# In[120]:


arr=np.arange(12).reshape(4,3)
arr


# In[121]:


# axis=1 以列位為主的橫向合併。


# In[122]:


np.concatenate([arr,arr],axis=1)


# In[123]:


# np.concatenate([arr,arr]): 預設值為以欄位為主的垂直合併。


# In[124]:


np.concatenate([arr,arr])


# In[125]:


arr+arr


# In[126]:


# pandas的concat


# In[127]:


s1=pd.Series([0,1],index=['a','b'])
s2=pd.Series([2,3,4],index=['c','d','e'])
s3=pd.Series([5,6],index=['f','g'])


# In[128]:


# pd.concat預設值也會是垂直的拓展資料。


# In[129]:


pd.concat([s1,s2,s3])


# In[130]:


# 如果axis=1，將會以欄為主橫向拓展資料，形成一個DataFrame。


# In[131]:


pd.concat([s1,s2,s3],axis=1)


# In[132]:


# 對於np.concatenate來說s1,s2,s3=array，只有一個維度，沒辦法使用axis=1。


# In[133]:


np.concatenate([s1,s2,s3])


# In[134]:


s4=pd.concat([s1,s3])
s4


# In[135]:


# axis=1 橫向的拓展欄位。


# In[136]:


# pd.concat的預設值為outer，所以可以看到NAN。


# In[137]:


pd.concat([s1,s4],axis=1)


# In[138]:


# 如果不想要看到NAN的值，可以使用join='inner'，就可以只取兩個表格都有的資料。


# In[139]:


pd.concat([s1,s4],axis=1,join='inner')


# In[140]:


# join_axes=[] 在python3中已經不支援，可改用reindex()去更換Index的值。


# In[141]:


df1=pd.concat([s1,s4],axis=1)
df1=df1.reindex(['a','c','b','e'])
df1


# In[142]:


# 有時候想要標記合併的index區塊，就可以使用keys=[]去標示值原先來自哪裡或是另作區分。


# In[143]:


result=pd.concat([s1,s2,s3],keys=['one','two','three'])
result


# In[144]:


# unstack(): 會將重疊的index攤平，重組成另一個DataFrame。


# In[145]:


result.unstack()


# In[146]:


# 如果同時寫上axis=1, keys=[]，此時的keys會成為欄位的名稱。


# In[147]:


pd.concat([s1,s2,s3],axis=1,keys=['one','two','three'])


# In[148]:


# pd.concat([df1,df2])


# In[149]:


df1=pd.DataFrame(np.arange(6).reshape(3,2), index=['a','b','c'], columns=['one','two'])
df1


# In[150]:


df2=pd.DataFrame(5+np.arange(4).reshape(2,2),index=['a','c'],columns=['three','four'])
df2


# In[151]:


# 同時寫上axis=1, keys=[]，此時keys一樣會變成欄位名稱。


# In[152]:


pd.concat([df1,df2],axis=1,keys=['level1','level2'])


# In[153]:


# pd.concat(dict) 如果是直接傳入dict，dict的key值會直接被當成keys。


# In[154]:


pd.concat({'level1':df1, 'level2':df2}, axis=1)


# In[155]:


# names 可以用來命名軸的名稱。


# In[156]:


pd.concat([df1,df2], axis=1, keys=['level1','level2'], names=['upper','lower'])


# In[157]:


# pd.concat遇到列index和資料完全不相關，也就是想合併的不是index而是columns。


# In[158]:


df1=pd.DataFrame(np.random.randn(3,4), columns=['a','b','c','d'])
df1


# In[159]:


df2=pd.DataFrame(np.random.randn(2,3), columns=['b','d','a'])
df2


# In[160]:


# 如果你想合併的不是index，而是columns，就可以寫上ignore_index=Ture。


# In[161]:


pd.concat([df1,df2],ignore_index=True)


# In[162]:


# 合併有重複的資料


# In[163]:


a=pd.Series([np.nan,2.5,0,3.5,4.5,np.nan], index=['f','e','d','c','b','a'])
a


# In[164]:


b=pd.Series([0,np.nan,2,np.nan,np.nan,5],index=['a','b','c','d','e','f'])
b


# In[165]:


# pd.isnull(): 為布林值，判斷a內誰為null值。
# np.where(‘判斷條件', True的狀況, False的狀況)：如下為如果是null值，填入b值，如果不是null值，填入a值。
# np.where(): 會直接忽略index，直接按照值的排序做資料替換。


# In[166]:


np.where(pd.isnull(a),b,a)


# In[167]:


# combine_first(array): 功用同np.where(pd.isnull(a),b,a)，不過，index會以b為主。


# In[168]:


b.combine_first(a)


# In[169]:


# combine_first(DataFrame)


# In[170]:


# range(start, stop, step)
# range(2,18,4)= [2,6,10,14]


# In[171]:


df1=pd.DataFrame({'a':[1,np.nan,5,np.nan],
                 'b':[np.nan,2,np.nan,6],
                 'c': range(2,18,4)})
df1


# In[172]:


df2=pd.DataFrame({'a':[5,4,np.nan,3,7], 'b':[np.nan,3,4,6,8]})
df2


# In[173]:


# df1.combine_first(df1): 如果df1有缺失值，優先以df2遞補。


# In[174]:


df1.combine_first(df2)


# In[175]:


# 重塑和旋轉 Reshape & Pivot


# In[176]:


# pd.Index([],name='') 可以幫軸命名。


# In[177]:


data=pd.DataFrame(np.arange(6).reshape(2,3), 
                  index=pd.Index(['Sun','Moon'],name='sky'),
                  columns=pd.Index(['one','two','three'],name='number'))


# In[178]:


data


# In[179]:


# stack(): 會將欄位名稱旋轉到列。


# In[180]:


result=data.stack()
result


# In[181]:


# unstack(): 將列旋轉到欄位。


# In[182]:


result.unstack()


# In[183]:


# 可以指定層編號作為stack(), unstack()的變動層。
# sky=0, number=1，unstack(0)即是指將sky變成欄位名稱。


# In[184]:


result.unstack(0)


# In[185]:


# 也可以直接寫入軸名稱。


# In[186]:


result.unstack('sky')


# In[187]:


s1=pd.Series([0,1,2,3],index=['a','b','c','d'])
s2=pd.Series([4,5,6],index=['c','d','e'])


# In[188]:


data2=pd.concat([s1,s2], keys=['one','two'])
data2


# In[189]:


# 進行unstack()時，如果有缺失值，系統會直接補上NAN。


# In[190]:


data2.unstack()


# In[191]:


# 進行stack()時，會自動濾除遺失值。


# In[192]:


data2.unstack().stack()


# In[193]:


# 如果stack(dropna=False)，會先濾除的遺失值還原。


# In[194]:


data2.unstack().stack(dropna=False)


# In[195]:


result


# In[196]:


# columns=pd.Index(['left','right'],name='side')：給予軸名稱。


# In[197]:


df=pd.DataFrame({'left':result,'right':result+5},columns=pd.Index(['left','right'],name='side'))
df


# In[198]:


df.unstack('sky')


# In[199]:


# 在進行stack()由欄轉為列時，也可以指定欄位名稱。


# In[200]:


df.unstack('sky').stack('side')


# In[201]:


# 長格式旋轉成寬格式


# In[230]:


data=pd.read_csv('desktop/python_practice/macrodata.csv')


# In[231]:


data.head()


# In[232]:


#pd.PeriodIndex(): 合併時間欄位。


# In[233]:


period=pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')


# In[234]:


period, type(period)


# In[235]:


# columns=pd.Index() 挑出需要的欄位。


# In[236]:


columns=pd.Index(['realgdp','infl','unemp'],name='item')


# In[237]:


columns, type(columns)


# In[238]:


# data.reindex() 將欄位做置換。


# In[239]:


data=data.reindex(columns=columns)


# In[240]:


data.head()


# In[241]:


# period.to_timestamp 調整日期index的格式，為精簡的日期。


# In[242]:


data.index=period.to_timestamp('D')


# In[243]:


data.index


# In[248]:


data.head()


# In[249]:


data.stack() #將item從欄轉為列。


# In[251]:


data.stack().reset_index() #給予data新的index。


# In[252]:


# rename(columns={0:'value'}) 將欄位名稱從0改為value。


# In[253]:


ldata=data.stack().reset_index().rename(columns={0:'value'})


# In[ ]:


# 確認前10列的資料。


# In[245]:


ldata[:10] 


# In[259]:


# pivot手法(index, columns, value): 使用此功能，可以將折成列的品項，翻轉成欄位的形式。


# In[260]:


ldata


# In[261]:


pivoted=ldata.pivot('date','item','value')


# In[262]:


# 可以看到原先在item內的infl, realgdp, unemp都從行被翻轉為欄位。


# In[263]:


pivoted


# In[271]:


len(ldata) #ldata的總行數有609行。


# In[272]:


#ladta['value2']: 插入一的新的欄位value2，並且給予該欄位隨機亂數609個數值。


# In[273]:


ldata['value2']=np.random.randn(len(ldata))


# In[266]:


ldata[:10]


# In[277]:


# pivot如果省略第三個欄位的值，會出現如下更加完整的表格。


# In[278]:


pivoted=ldata.pivot('date','item')


# In[279]:


pivoted[:5]


# In[280]:


pivoted['value'][:5]


# In[ ]:


# set_index().unstack()=pivot


# In[284]:


ldata[:5]


# In[283]:


ldata.set_index(['date','item']) #先讓date, item成為index


# In[281]:


unstacked=ldata.set_index(['date','item']).unstack('item') #將item從列轉成欄位名稱。


# In[282]:


unstacked[:7] #呈現的結果就會跟pivot一模一樣。


# In[285]:


# 寬格式旋轉成長格式


# In[286]:


# pivot: 把一個欄位，轉為多個欄位。


# In[287]:


# pandas.melt：把多個欄位合併成一個欄位。


# In[288]:


df=pd.DataFrame({'key':['sun','moon','lake'],
                'A':[1,2,3],
                'B':[4,5,6],
                'C':[7,8,9]})


# In[289]:


df


# In[292]:


# pd.melt(DataFrame, ['key']): 可以將多個欄位儲存為一個欄位，並將其value獨立為一個欄位。


# In[293]:


melted=pd.melt(df,['key'])


# In[294]:


melted


# In[295]:


# pivot(index, columns, value): 就可以將一個欄位轉為多個欄位。


# In[296]:


reshaped=melted.pivot('key','variable','value')


# In[297]:


reshaped


# In[298]:


# reset_index(): 可以用來重置index。


# In[299]:


reshaped.reset_index()


# In[301]:


# id_vars=[], value_vars=[]: 可以指定只有哪幾個欄位需要被轉置。


# In[302]:


pd.melt(df,id_vars=['key'],value_vars=['A','B'])


# In[303]:


#pd.melt() 也可以不指定任何分組的欄。


# In[304]:


pd.melt(df,value_vars=['A','B','C'])


# In[305]:


pd.melt(df,value_vars=['key','A','B'])

