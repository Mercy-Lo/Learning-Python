#!/usr/bin/env python
# coding: utf-8

# In[33]:


# 資料載入、儲存和檔案格式


# In[34]:


# !cat：mac電腦用來開啟檔案的unix shell命令。


# In[35]:


# !type: 如果是windows的電腦，可使用itype的開啟檔案。


# In[36]:


get_ipython().system('cat desktop/python_practice/example_1.csv')


# In[37]:


f = open(path)


# In[38]:


import pandas as pd


# In[39]:


import numpy as np


# In[40]:


# pd.read_csv: 可以把資料寫入dataframe


# In[41]:


df= pd.read_csv('desktop/python_practice/example_1.csv')


# In[42]:


df


# In[43]:


# pd.read_table: 可以指定分隔資料的為哪個符號。


# In[44]:


df2=pd.read_table('desktop/python_practice/example_1.csv', sep=',')


# In[45]:


df2


# In[46]:


# 對沒有標題的檔案，可以透過read_csv自定義標題。


# In[47]:


get_ipython().system('cat desktop/python_practice/example_2.csv')


# In[52]:


# header=None: 寫出來，系統就不會擷取第一行作為標題。


# In[53]:


pd.read_csv('desktop/python_practice/example_2.csv', header=None)


# In[54]:


# names=[]，自己定義標題為何。


# In[55]:


pd.read_csv('desktop/python_practice/example_2.csv', names=['a','b','c','d','message'])


# In[50]:


names=['a','b','c','d','message']


# In[56]:


# index_col: 可以指定某一欄位為index。


# In[57]:


pd.read_csv('desktop/python_practice/example_2.csv', names=names, index_col='message')


# In[59]:


get_ipython().system("cat 'desktop/python_practice/example_3.csv'")


# In[62]:


# 如果希望多個欄位可以成為index，可以使用[x,y]


# In[63]:


parsed= pd.read_csv('desktop/python_practice/example_3.csv',index_col=['key1','key2'])


# In[64]:


parsed


# In[95]:


# 用list(open(path))開啟txt資料。


# In[96]:


list(open('desktop/python_practice/example_4.csv'))


# In[99]:


get_ipython().system('cat desktop/python_practice/example_5.csv')


# In[ ]:


# skiprows: 可以用來跳過特定行。


# In[101]:


pd.read_csv('desktop/python_practice/example_5.csv', skiprows=[0,2,4])


# In[105]:


# 處理遺失值


# In[106]:


# 遇到NA,空格，python會自動補上NAN。 


# In[107]:


get_ipython().system('cat desktop/python_practice/example_6.csv')


# In[108]:


result= pd.read_csv('desktop/python_practice/example_6.csv')


# In[109]:


result


# In[110]:


pd.isnull(result)


# In[117]:


# na_values=[] 可以自定義遺失值。


# In[118]:


result= pd.read_csv('desktop/python_practice/example_6.csv',na_values=['two',5,10,15])


# In[119]:


result


# In[122]:


# na_values 除了放入list外，也可以放入dict。


# In[123]:


sentinels={'message':['Tuesday','NA'], 'one':['two']}


# In[124]:


pd.read_csv('desktop/python_practice/example_6.csv', na_values=sentinels)


# In[125]:


# 分段讀取文字檔


# In[ ]:


# 在閱讀較大的檔案時，可以先縮小閱讀範圍。


# In[137]:


pd.options.display.max_rows=8


# In[138]:


result=pd.read_csv('desktop/python_practice/example_7.csv')


# In[139]:


result


# In[ ]:


# 如果一開始只決定閱讀前幾行，可以使用nrows。


# In[136]:


pd.read_csv('desktop/python_practice/example_7.csv', nrows=7)


# In[155]:


# chunksize: 設定一次讀幾行。


# In[156]:


chunker= pd.read_csv('desktop/python_practice/example_7.csv', chunksize=20)


# In[157]:


chunker


# In[158]:


tot= pd.Series([])

for piece in chunker:
    tot= tot.add(piece['key'].value_counts(), fill_value=0)

tot= tot.sort_values(ascending=False)


# In[160]:


tot[:8]


# In[161]:


# 寫出文字資料


# In[ ]:


# to_csv: 可以將資料寫成逗號分隔的檔案。


# In[169]:


data=pd.read_csv('desktop/python_practice/example_6.csv')


# In[170]:


data


# In[171]:


data.to_csv('desktop/python_practice/example_out.csv') #給予新的檔案名稱，會出現新檔案在檔案夾內。


# In[172]:


get_ipython().system('cat desktop/python_practice/example_out.csv')


# In[175]:


# 也可以改用其他的分隔符號。


# In[ ]:


# sys.stdout 會把文字顯示在終端機上。


# In[173]:


import sys


# In[174]:


data.to_csv(sys.stdout, sep='|')


# In[176]:


# na_rep='' 遺失值可以用其他符號取代。


# In[177]:


data.to_csv(sys.stdout, na_rep='Null')


# In[178]:


# 不要顯示欄標籤與列標籤


# In[179]:


data.to_csv(sys.stdout, index=False, header=False)


# In[180]:


# 也可以只顯示部份欄，欄的順序由你決定


# In[181]:


data.to_csv(sys.stdout, index=False, columns=['a','b','c'])


# In[194]:


# Series也可以儲存為csv。


# In[195]:


dates= pd.date_range('10/1/2022', periods=7)


# In[196]:


ts= pd.Series(np.arange(7), index=dates)


# In[197]:


ts.to_csv('desktop/python_practice/example_series.csv')


# In[198]:


get_ipython().system('cat desktop/python_practice/example_series.csv')


# In[231]:


# 分隔符號的使用


# In[232]:


get_ipython().system('cat desktop/python_practice/example_8.csv')


# In[233]:


# open(): 用來打開文件，reader():用來讀取文件


# In[234]:


import csv


# In[235]:


f=open('desktop/python_practice/example_8.csv')


# In[236]:


reader=csv.reader(f)


# In[237]:


# print(line): 可以顯示每一行的資料。


# In[238]:


for line in reader:
    print(line)


# In[239]:


# 將資料轉換爲想要的格式list


# In[240]:


with open ('desktop/python_practice/example_8.csv') as f:
    lines=list(csv.reader(f))


# In[241]:


# 第0列的資料為header，第1列之後的資料為列。


# In[242]:


header, values= lines[0], lines[1:]


# In[243]:


data_dict={h:v for h, v in zip(header, zip(*values))}


# In[244]:


data_dict


# In[246]:


f=open('desktop/python_practice/example_8.csv')


# In[247]:


reader=csv.reader(f)


# In[249]:


for line in reader:
    print(line)


# In[254]:


class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
    
reader=csv.reader(f, dialect=my_dialect)


# In[255]:


reader=csv.reader(f,delimiter='|')


# In[256]:


for line in reader:
    print(line)


# In[257]:


with open('mydata.csv', 'w') as f:
    writer= csv.writer(f, dialect=my_dialect)
    writer.writerow(('one','two','three'))
    writer.writerow(('1','2','3'))
    writer.writerow(('4','5','6'))
    writer.writerow(('7','8','9'))


# In[258]:


for line in reader:
    print(line)


# In[259]:


get_ipython().system('cat desktop/python_practice/example_8.csv')

