#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 花式索引


# In[3]:


import numpy as np


# In[4]:


arr= np.empty((8,4))


# In[5]:


for i in range(8):
    arr[i]= i


# In[6]:


arr


# In[7]:


# 特定索引，可以給予一個有順序的list或ndarray。


# In[8]:


arr [[4,5,7,0]]


# In[9]:


# 如果list內的元素為負值，可以讓array由後面數回前面。


# In[10]:


arr[[-3,-4,-1,-5]]


# In[11]:


# arange(): 可以產出有順序的array。 reshape((x,y))：可以將array變成多維矩陣。


# In[12]:


arr= np.arange(32).reshape((8,4))
arr


# In[13]:


arr[[1,5,7,2],[0,3,1,2]]


# In[14]:


# 先從arr取出4列 [1,5,7,2], 再維持取出來的值[:]，並將值做順序調整 [0,3,1,2]。


# In[15]:


arr[[1,5,7,2]][:,[0,3,1,2]]


# In[16]:


# 轉置陣列和軸交換


# In[17]:


# reshaping 重新塑形會改變view，不會把底層的資料重新安排。


# In[18]:


import numpy as np


# In[19]:


arr= np.arange(15).reshape((3,5))


# In[20]:


arr


# In[21]:


# T： 可以將行翻轉成列。


# In[22]:


arr.T


# In[23]:


# np.dot(arr1,arr2) 計算矩陣乘積。


# In[24]:


np.dot([2],[3])


# In[25]:


arr=np.arange(4).reshape((2,2))
arr


# In[26]:


arr.T


# In[27]:


np.dot(arr.T,arr)


# In[28]:


#reshape(x,y,z)：代表這個陣列有三個維度，最外面那層[],中間那層[],最裡面那些元素。


# In[29]:


arr =np.arange(16).reshape(2,2,4)
arr


# In[30]:


# transpose(x,y,z): 代表這裡有3個維度，包含0,1,2，0代表最外層，也就是(0,8)，1代表中間層，也就是(0,4)，2代表最內層，也就是（0,1,2,3)
# transpose(1,0,2): 代表最外層改為(0,4),中間層改為(0,8)，最內層維持不動為（0,1,2,3)。


# In[31]:


arr.transpose((1,0,2))


# In[32]:


np.transpose(arr)


# In[33]:


#swapaxes(x,y): x,y表示想要互相交換的維度。這裡總共有3個維度，包含0,1,2，0維度代表（0,8),1維度代表（0,4),2維度代表（0,1,2,3)。
#swapaxes(1,2): 1維度與2維度交換，表示0維持為（0,8), 1維度改為（0,1,2,3), 2維度改為(0,4)。
#swapaxes(): 不進行資料複製，只回傳view。


# In[34]:


arr=np.arange(16).reshape(2,2,4)
arr


# In[35]:


arr.swapaxes(1,2)


# In[36]:


# 全域函式：快速元素級別陣列函式，對陣列裡的資料，執行元素級別運算的函式，也稱ufunc。


# In[37]:


arr= np.arange(10)
arr


# In[38]:


# sqrt(): 開根號，屬於一元的全域函式。


# In[39]:


np.sqrt(arr)


# In[40]:


# exp()：指的是常數e的指數。ｅ=2.7182...無限無理數，屬於一元的全域函式。


# In[41]:


arr
np.exp(arr)


# In[42]:


# maximum():可以找出最大值，屬於二元的全域函式。


# In[43]:


x=np.random.randn(8)
x


# In[44]:


y=np.random.randn(8)
y


# In[45]:


np.maximum(x,y)


# In[46]:


# modf(): 返回x的整數部分與小數部份，為一元函式，會回傳多個陣列。


# In[47]:


arr=np.random.randn(7)*5
arr


# In[48]:


remaindar, whole_part=np.modf(arr)


# In[49]:


remaindar #小數部份


# In[50]:


whole_part #整數部份


# In[51]:


# 運用全域函式，增加一個out的參數，就可以讓原本的陣列更改為全域函式作用後的陣列。


# In[52]:


arr2=arr+10
arr2


# In[53]:


np.sqrt(arr2,arr2)


# In[54]:


arr2


# In[55]:


#一元全域函式


# In[56]:


#abs(), fabs()：計算絕對值。


# In[57]:


np.abs(-100)


# In[58]:


np.fabs(-200)


# In[59]:


#sqrt(): 計算平方根。


# In[60]:


np.sqrt(25)


# In[61]:


#square(): 計算平方。


# In[62]:


np.square(30)


# In[63]:


#exp(): 求出e的指數值，e=2.7182...


# In[64]:


np.exp(3)


# In[65]:


#log(),log10(),log2(),log1p: 做自然對數(以e為底), 以10為底，以2為底，以log(1+x)為底


# In[66]:


np.log(20.08333692)


# In[67]:


np.log10(1000)


# In[68]:


np.log2(32)


# In[69]:


np.log1p(5)


# In[70]:


#sign(): 計算每個元素的正負值：0,1,-1


# In[71]:


np.sign(-21)


# In[72]:


np.sign(56)


# In[73]:


np.sign(0)


# In[74]:


#ceil(): 向上取整數。


# In[75]:


np.ceil(-6.17)


# In[76]:


#floor(): 向下取整數。


# In[77]:


np.floor(-6.17)


# In[78]:


#rint(): 將元素取最靠近的整數，並保留dtype。


# In[79]:


np.rint(-3.9)


# In[80]:


np.rint(3.15)


# In[81]:


#modf(): 取出整數與小數的部分。


# In[82]:


np.modf(2.14)


# In[83]:


#isnan(): 回傳布林列，確認是否為NaN。


# In[84]:


np.isnan(np.sqrt(-100))


# In[85]:


#isfinite(),isinf(): 回傳是否為有限。


# In[86]:


np.isfinite(1/3)


# In[87]:


#sin(),cos(),tan(),sinh(),cosh(),tanh(): 三角函數或是雙曲三角函數。


# In[88]:


np.sin(2)


# In[89]:


#logical_not(): 相當於~arr，逐元素計算not x 的真值。


# In[90]:


arr=np.arange(6)
np.logical_not(arr<4)


# In[91]:


#二元全域函式


# In[92]:


#add(): 把陣列相對位置函式相加。


# In[93]:


x=np.random.randn(4).reshape(2,2)
y=np.random.randn(4).reshape(2,2)


# In[94]:


x


# In[95]:


y


# In[96]:


np.add(x,y)


# In[97]:


#subtract(): 第一個陣列減掉第二個陣列。


# In[98]:


np.subtract(x,y)


# In[99]:


#multiply(): 兩個陣列相乘。


# In[100]:


np.multiply(x,y)


# In[101]:


#divide(), floor_divide(): 除或整除（去除餘數）


# In[102]:


np.divide(1,3)


# In[103]:


np.floor_divide(1,3)


# In[104]:


#power(): 將第一個陣列作為第二個陣列的次方。


# In[105]:


np.power(3,4)


# In[106]:


#maximum(),fmax(): 找到最大值或忽視NAN找到最大值。


# In[107]:


np.maximum(np.sqrt(x),np.sqrt(y))


# In[108]:


np.fmax(np.sqrt(x),np.sqrt(y))


# In[109]:


#mod():取出餘數。


# In[110]:


np.mod(20,3)


# In[111]:


#copysign(): 複製第二個陣列的正負號給第一個陣列。


# In[112]:


np.copysign(-1,10)


# In[113]:


np.copysign(100,-30)


# In[114]:


#greater(), greater_equal, less(), less_equal(), equal(), not_equal(): 等同於>,>=,<,<=,=,!=


# In[115]:


np.greater(x,y)


# In[116]:


#logical_and(), logical_or, logical_xor: 等同於＆, |, ^


# In[117]:


x


# In[118]:


y


# In[119]:


np.logical_xor(x,y)


# In[120]:


# 用陣列寫陣式導向程式


# In[121]:


# 向量化：迴圈替換成陣列表達式。


# In[122]:


# meshgrid()：可以產生二維矩陣。


# In[123]:


points= np.arange(-5,5,0.01)


# In[124]:


xs,ys= np.meshgrid(points,points)


# In[125]:


ys


# In[126]:


xs


# In[127]:


z=np.sqrt(xs**2, ys**2)
z


# In[128]:


# matplotlib: 可將產出的二維陣列視覺化。


# In[129]:


import matplotlib.pyplot as plt


# In[130]:


plt.imshow(z, cmap=plt.cm.gray) ; plt.colorbar()


# In[131]:


plt.title('Image plot of $\sqrt{x^2 +y^2}$ for a grid of values')


# In[132]:


# 用陣列運算表達條件邏輯


# In[133]:


# numpy.where 是 x if condition else y 的向量版本。


# In[134]:


xarr = np.array([1.1,1.2,1.3,1.4,1.5])


# In[135]:


yarr = np.array([2.1,2.2,2.3,2.4,2.5])


# In[136]:


cond = np.array([True,False,True,False,True])


# In[137]:


# 假設我們只要在cond中看到True，就拿xarr，否則yarr


# In[138]:


result=[(x if c else y)
       for x,y,c in zip(xarr,yarr,cond)]
result


# In[139]:


# 不過上面的寫法遇到大陣列會很慢。


# In[140]:


# np.where 可以提升運算效率與精簡度。


# In[141]:


result= np.where(cond,xarr,yarr)
result


# In[142]:


# 假設有一個隨機的資料庫，要把正值改為2, 負值改為-2, 可以使用np.where


# In[143]:


arr = np.random.randn(4,4)
arr


# In[144]:


arr >0


# In[145]:


np.where(arr>0, 2, -2) #常數＋常數


# In[146]:


np.where(arr>0, 2, arr) #常數＋陣列


# In[147]:


# 數學和統計方法


# In[148]:


# 聚合函數（aggregation, reduction)：sum(),mean(),std()


# In[149]:


arr = np.arange(16).reshape(4,4)
arr


# In[150]:


arr.mean()


# In[151]:


arr.sum()


# In[152]:


# 第一個維度:(0,4,8,12), 第二個維度：(0,1,2,4)，如下表示僅計算第二維度的中位數與總和。


# In[153]:


arr.mean(axis=1)


# In[154]:


arr.sum(axis=1)


# In[155]:


# cumsum(): a, a+b, a+b+c, a+b+c+d,,,構成的數列。


# In[156]:


# cumprod(): a, a*b, a*b*c, a*b*c*d,,,構成的數列。 


# In[157]:


arr= np.array([1,2,3,4,5,6,7,8,9])
arr


# In[158]:


arr.cumsum()


# In[159]:


arr.cumprod()


# In[160]:


# 多維陣列的運算


# In[161]:


arr = np.array([[0,1,2],[3,4,5],[7,8,9]])
arr


# In[162]:


arr.cumsum(axis=0) #第一維度（0,3,7)


# In[163]:


arr.cumsum(axis=1) #第二維度（0,1,2)


# In[164]:


# 布林陣列的方法


# In[165]:


# sum()：可以用來計算Ture有幾個。


# In[166]:


arr= np.random.randn(20)
arr


# In[167]:


(arr>0).sum()


# In[168]:


# any(): 可以查找是否有至少一個True。 all(): 可以用來確認是不是全部都是True。


# In[169]:


bools= np.array([True, False, False, False])


# In[170]:


bools.any()


# In[171]:


bools.all()


# In[172]:


# 排序


# In[173]:


# sort(): 跟list一樣，可以讓array排序。


# In[174]:


arr= np.random.randn(5)
arr


# In[175]:


arr.sort()


# In[176]:


arr


# In[177]:


# 除了全部一起排序外，寫入axis，就可以根據特定維度做排序。


# In[178]:


arr = np.random.randn(3,4)
arr


# In[179]:


arr.sort(1) #針對第二維度做排序。
arr


# In[180]:


# np.sort(): 會回傳一個已經排好序的複製序列。


# In[181]:


large_arr = np.random.randn(5)
large_arr


# In[182]:


large_arr.sort()
large_arr


# In[183]:


# len(array): 可以計算array內元素的數量。


# In[184]:


len([1,2,3,4])


# In[185]:


len([[1,2],[3,4]])


# In[186]:


len([[1,2],3,4])


# In[187]:


# int(): 可以取出整數值。


# In[188]:


int(1.25)


# In[189]:


large_arr[int(0.05*len(large_arr))] #large_arr[0]


# In[190]:


# Unique 和其他集合操作


# In[191]:


# unique(): 回傳排好序的不重複的值。


# In[192]:


name= np.array(['Joe','Joe','Joe','Tom','Tom','Tom','Eric','Eric','Eric'])


# In[193]:


np.unique(name)


# In[194]:


ints= np.array([50,20,80,70,70,80,60,20,50,50])


# In[195]:


np.unique(ints)


# In[196]:


# 上面的動作，等同於set(), sorted()功能的加總


# In[197]:


name


# In[198]:


sorted(set(name))


# In[199]:


sorted(set(ints))


# In[200]:


# in1d(): 用來檢查一個陣列是否存在於另一個陣列。


# In[201]:


ints


# In[202]:


np.in1d(ints, [50,60,70])


# In[203]:


# 從檔案中輸入或輸出值到陣列


# In[204]:


arr = np.arange(10)


# In[205]:


# save(): 將一個陣列儲存起來。


# In[206]:


np.save('some_array',arr)


# In[207]:


# load(): 載入該陣列，檔名必須要加.npy


# In[208]:


np.load('some_array.npy')


# In[209]:


# savez(): 儲存多個未壓縮的陣列。


# In[210]:


np.savez('array_archive.npz',a=arr,b=arr)


# In[211]:


arch=np.load('array_archive.npz')


# In[212]:


arch['b']


# In[213]:


# savez.compressed()：可使用在壓縮資料。


# In[214]:


np.savez_compressed('arrays_compressed.npz',a=arr,b=arr,c=arr,d=arr)


# In[215]:


arch2=np.load('arrays_compressed.npz')


# In[216]:


arch2['d']


# In[217]:


# 線性代數


# In[218]:


# dot(): 用來計算矩陣的內積。


# In[219]:


x= np.array([[1,2,3],[4,5,6]])
x


# In[220]:


y= np.array([[7,8],[9,10],[11,12]])
y


# In[221]:


x.dot(y)


# In[222]:


np.dot(x,y)


# In[223]:


np.ones(3)


# In[224]:


np.dot(x,np.ones(3))


# In[225]:


# @的符號功能等同於dot()


# In[226]:


x @ y


# In[227]:


# 介紹linalg內的inv(), qr()


# In[228]:


from numpy.linalg import inv,qr


# In[229]:


x = np.array([[1,2],[3,4],[5,6]])
x


# In[230]:


# T: 可以用來將矩陣的行換成列。


# In[231]:


x.T


# In[232]:


mat=x.T.dot(x)
mat


# In[233]:


# inv(): 逆矩陣的一種。 如果一個矩陣為[[a,b],[c,d]]，使用inv()後，該矩陣的a,d會互換位置，並且變成負值，
# 此外，a,b,c,d都會除以-(ab-cd)。


# In[234]:


arr = np.array([[10,20],[30,40]])
arr


# In[235]:


inv(arr)


# In[236]:


mat


# In[237]:


inv(mat) #35,56互換位置，由於35*56-44*44=24，故每個值要除以24。


# In[238]:


mat.dot(inv(mat)) #因為互為反矩陣，故呈現結果為[1,0],[0,1]


# In[239]:


# qr(): 可將現有矩陣轉換為三角矩陣。


# In[240]:


q,r =qr(mat) 


# In[241]:


r


# In[242]:


# 生成偽隨機變數


# In[312]:


# 常態分布(Normal Distribution)，又稱高斯分佈，可以透過normail(size=(x,y))執行出來。


# In[313]:


samples = np.random.normal(size=(4,4))
samples


# In[314]:


# random.normalvariate(mu,sigma): 可以做出常態分佈，mu代表平均數，sigma代表標準差。


# In[ ]:


# %timeit: 可以用來計算該程式的執行速度。


# In[317]:


from random import normalvariate


# In[318]:


n =100


# In[319]:


get_ipython().run_line_magic('timeit', 'samples=[normalvariate(0,1) for _ in range(n)]')


# In[320]:


get_ipython().run_line_magic('timeit', 'np.random.normal(size=n)')


# In[321]:


# 由上述的時間比較可知，在進行常態分佈的運算時，random.mormal的運行效率比random.normalvariate好！


# In[331]:


# 之所以為偽隨機變數，是因為亂數器產生的種子可以透過np.random.seed()做改變。


# In[335]:


# 在 random.seed(0)的情況下，若要隨機產生１-1000中的整數，會出現固定值865。
# 在 random.seed(1)的情況下，會出現138。
# 由此可知，seed()的功用在於變換當下隨機產生的亂數，一次產生一個。
for i in range(5):
    random.seed(1)
    print(random.randint(1,1000))


# In[336]:


# 如果希望不要有重複的亂數，直接移除 random.seed()即可。
for i in range(5):
    print(random.randint(1,1000))


# In[338]:


np.random.seed(1)


# In[ ]:


# random.RandomState()：建立獨立的亂數產生器，一次可以產生多個值。


# In[350]:


rng= np.random.RandomState(1)


# In[351]:


rng.randn(1)


# In[354]:


for i in range(5):
    np.random.RandomState(1)
    print(random.randint(1,1000))


# In[263]:


# 隨機漫步(Random Walk Theory): 股票價格是隨機波動的，價格的去向並沒有規律的。

# 任何投資者都明白影響股價走向的因素很多。但若然從長時間的價格走勢來看，價格上下起伏的機會其實差不多均等的。

# 隨機漫步理論假設：股票市場每一個人都懂得分析，而資料都是公開的，人人皆知。


# In[ ]:


# 隨機漫步的起點為0, 接下來每一步可能是1, -1，且每一步機率相等。


# In[279]:


import random


# In[280]:


position=0


# In[281]:


walk=[position]


# In[282]:


steps=1000


# In[283]:


for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)


# In[284]:


plt.plot(walk[:100])


# In[355]:


# 將硬幣連續擲1000次，正面為１，反面為-1，計算累積加總數。


# In[356]:


nsteps=1000


# In[357]:


draws = np.random.randint(0,2,size=nsteps)


# In[358]:


steps=np.where(draws>0, 1, -1)


# In[359]:


walk = steps.cumsum()


# In[360]:


walk.min()


# In[361]:


walk.max()


# In[362]:


# 首次穿越時間 (first crossing time)：計算走了多少步以後才能夠首次到達10, -10。


# In[363]:


# argmax(): 可以找到最大值，並且回傳index。


# In[364]:


(np.abs(walk) >= 10).argmax()


# In[365]:


# 一次模擬許多隨機漫步


# In[295]:


nwalks=5000


# In[296]:


nsteps=1000


# In[297]:


draws=np.random.randint(0,2,size=(nwalks,nsteps)) 


# In[298]:


steps = np.where(draws >0, 1, -1)


# In[299]:


walks = steps.cumsum(1)


# In[300]:


walks


# In[301]:


walks.max()


# In[302]:


walks.min()


# In[303]:


# 第幾步穿越30, -30


# In[304]:


hits30= (np.abs(walks)>=30).any(1)


# In[305]:


hits30


# In[306]:


hits30.sum()


# In[307]:


# 把walks中累加步數絕對值30以上的列，利用布林陣列選出來。


# In[308]:


crossing_times = (np.abs(walks[hits30]) >=30).argmax(1)


# In[309]:


crossing_times.mean()


# In[310]:


# 常態分布的漫步值


# In[311]:


steps = np.random.normal(loc=0, scale=0.25, size=(nwalks, nsteps))

