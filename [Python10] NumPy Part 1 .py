#!/usr/bin/env python
# coding: utf-8

# In[1]:


# NumPy: Numerical Python，是計算最重要的基礎。


# In[ ]:


# NumPy的數學運算非常有效率，不需要透過for迴圈也可以將資料計算出來，速度比一般python語法快上10-100倍，記憶體的容量也很少。


# In[2]:


import numpy as np


# In[ ]:


# 使用np.arrange的元素去乘以２倍，計算運算時間。


# In[4]:


my_arr=np.arange(1000000) 


# In[8]:


get_ipython().run_line_magic('time', 'for _ in range(10):my_arr2=my_arr*2')


# In[9]:


# 使用python內建的list，計算運算時間。


# In[10]:


my_list=list(range(1000000))


# In[11]:


get_ipython().run_line_magic('time', 'for _ in range(10): my_list2=[x*2 for x in my_list]')


# In[12]:


# NumPy ndarray: 多維陣列物件


# In[19]:


import numpy as np


# In[20]:


data=np.random.randn(2,3)


# In[21]:


data


# In[22]:


data*10


# In[23]:


data+data


# In[24]:


# ndarray是同質資料的多為容器，每一個元素型態要一致，每一個陣列都有shape與dtype。


# In[25]:


# shape: 標明維度的tuple。dtype: 資料型態。


# In[26]:


data.shape


# In[27]:


data.dtype


# In[34]:


# 建立ndarray: 使用array()，list很適合傳入物件。


# In[35]:


data1=[6,7.5,9,0,2]


# In[36]:


arr1=np.array(data1)


# In[37]:


arr1


# In[38]:


# 使用巢式list，等長的list會形成多維陣列。


# In[53]:


data2=[[1,2,3,4],[5,6,7,8]]


# In[54]:


arr2=np.array(data2)


# In[55]:


arr2


# In[56]:


# ndim: 確認陣列的行數，shape: 確認陣列的型態，包含欄與列。


# In[57]:


arr2.ndim


# In[58]:


arr2.shape


# In[61]:


# dtype: 確認陣列的資料型態。


# In[62]:


arr1.dtype


# In[63]:


arr2.dtype


# In[ ]:


# zeros(): 可以建立全部為0的陣列。


# In[65]:


np.zeros(10)


# In[84]:


# ones(): 可以建立全部為1的陣列。


# In[85]:


np.ones(10)


# In[ ]:


# 如果希望建立多維度的陣列，可以將tuple放入zeros()/ones()


# In[69]:


np.zeros((3,6))


# In[87]:


np.ones((2,2))


# In[88]:


# empty(): 可以產生亂數，（a,b,c)=(陣列數量,列數,欄數)


# In[89]:


np.empty((2,3,1))


# In[90]:


# arrange() 類似於range(): 可以產生連續的陣列。


# In[93]:


np.arange(15)


# In[99]:


# identity(), eye() 可以做出正方形的陣列，且對角線為0,1。


# In[100]:


np.identity(2)


# In[101]:


np.eye(2)


# In[102]:


# ndarray的資料型態


# In[105]:


arr1 = np.array([1,2,3], dtype=np.float64)


# In[117]:


arr2 = np.array([2,2,3], dtype=np.int32)


# In[118]:


arr1.dtype


# In[119]:


arr2.dtype


# In[120]:


# astype(): 可以轉換dtype。


# In[121]:


arr=np.array([1,2,3,4,5,6])


# In[122]:


arr.dtype


# In[123]:


float_arr=arr.astype(np.float64)


# In[124]:


float_arr.dtype


# In[125]:


# 將文字轉為數字，不過由於字串長度固定，可能會切掉部分的值，要小心。


# In[126]:


numeric_strings=np.array(['1.5','1.25','2.75','3.5','50'],dtype=np.string_)


# In[133]:


numeric_strings.astype(float)


# In[ ]:


# 可以使用另外一個陣列的屬性來轉換資料型態喔！


# In[134]:


int_array=np.arange(10)


# In[136]:


calibers=np.array([.22,.279,.45,.80,.50],dtype=np.float64)


# In[137]:


int_array.astype(calibers.dtype)


# In[ ]:


# 也可以使用代碼來轉換文字格式。例如：u4=unit32 ; f4=float32


# In[140]:


empty_unit32=np.empty(8,dtype='u4')


# In[141]:


empty_unit32


# In[143]:


#陣列的算數運算：好處是不用寫任何的迴圈，就會進行整批運算。-> 向量化（vectorization)


# In[151]:


arr=np.array([[1,2,3],[4,5,6]])
arr


# In[152]:


arr * arr


# In[153]:


arr - arr


# In[154]:


1 / arr


# In[155]:


arr **0.5


# In[156]:


arr2 = np.array([[0,4,1],[7,2,12]])


# In[157]:


arr2


# In[158]:


arr2 > arr


# In[159]:


# 基本的索引和切片


# In[160]:


arr = np.arange(10)


# In[161]:


arr


# In[162]:


arr[5]


# In[163]:


arr[5:8]


# In[171]:


# arr 透過索引進行修改後，會在原本的陣列上進行修改，並不會產生新的陣列。


# In[172]:


arr[5:8]=12
arr


# In[173]:


# 修改由原先陣列延伸出來的切片，若修改切片的值，原本的陣列數值也會更改。


# In[174]:


arr_slice=arr[5:8]
arr_slice


# In[175]:


arr_slice[1]=12345


# In[176]:


arr


# In[177]:


# [:] 表示要使用陣列所有值。


# In[178]:


arr_slice[:]=64
arr


# In[179]:


# numpy之所以直接修改原陣列的原因是為了效率，如果每做一個動作都要複製，會很消耗效能跟容量，所以原本設定是直接原地修改。


# In[180]:


# copy(): 想把資料複製出來，可以使用copy()


# In[181]:


a = arr[5:8].copy()


# In[182]:


a[:]=5 #複製出來的a，即便修改數值，也不會影響原本的arr。


# In[183]:


arr


# In[184]:


# 高維度陣列


# In[185]:


arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[186]:


arr2d[2]


# In[ ]:


# 二維陣列，如果要抓取特定的值，除了[a][b]外，也可以[a,b]


# In[187]:


arr2d[0][2]


# In[188]:


arr2d[0,2]


# In[191]:


arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3d


# In[200]:


arr3d[0]


# In[201]:


old_values=arr3d[0].copy


# In[202]:


arr3d[0]=42
arr3d


# In[207]:


# ???? arr3d[0]=old_values


# In[208]:


arr3d[1,0]


# In[209]:


x = arr3d[1]


# In[210]:


x


# In[211]:


x[0]


# In[212]:


# 用切片做索引


# In[213]:


arr


# In[214]:


arr[1:6]


# In[215]:


arr2d


# In[216]:


arr2d[:2]


# In[218]:


arr2d[:2,1:]


# In[219]:


arr2d[1,:2]


# In[220]:


arr2d[2,:2]


# In[221]:


arr2d[:,:1]


# In[222]:


arr2d[:2,1:]=0
arr2d


# In[223]:


# 布林索引


# In[259]:


interests = np.array(['Books','Movie','Swimming','Books','Bikes','Movie','Dance'])


# In[260]:


data = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24],[25,26,27,28]])


# In[261]:


interests


# In[262]:


data


# In[263]:


# 運用 == 可以進行布林值比較，可以透過比較運算子，產生布林索引。


# In[264]:


interests == 'Bikes'


# In[265]:


# 特別注意到使用布林陣列，兩個互相參照的行列數要一致。 


# In[266]:


# 由interests='Bike' 我們可以知道正確的值在index=4，放入到data，系統會找到index=4的那一列。(row)


# In[267]:


data[interests == 'Bikes']


# In[268]:


# 接下來再從[17,18,19,20]找到index=0,1的值，就是[17,18]囉！


# In[269]:


data[interests == 'Bikes',:2]


# In[270]:


data[interests == 'Bikes', 3]


# In[271]:


# 如果要排除Bike以外的資料，可以使用 '!=' 或是反向 '~'


# In[273]:


interests != 'Bikes'


# In[277]:


data[~(interests == 'Bikes')]


# In[281]:


# 在使用~時，可以先將資料存到另外一個陣列b_array，再套到data[]內，呈現會比較精美。


# In[282]:


b_array=interests=='Bikes'


# In[283]:


data[~b_array]


# In[284]:


# 如果想使用2個以上的條件，可以使用& , |(或)


# In[287]:


interests2=( (interests =='Bikes') | (interests =='Movie') )


# In[288]:


interests2


# In[290]:


data[interests2]


# In[291]:


# 注意在使用布林值陣列時，不能使用文字的and, or，必須使用符號 &, |。


# In[293]:


interests2=( (interests =='Bikes') & (interests =='Movie') )


# In[294]:


# 利用布林值陣列來調整原陣列的值。


# In[296]:


data


# In[297]:


data[data<20]=0
data


# In[299]:


data[interests=='Dance']=150


# In[300]:


data

