#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 資料載入、儲存和檔案格式


# In[3]:


# JSON資料 （Javascript Object Notation)


# In[7]:


# json.dumps(): 將python物件轉成json。 在python中，所有儲存成json的程式碼都是str。


# In[8]:


import json
import numpy as np
import pandas as pd


# In[9]:


a_tuple=(1,2,3,4,5)
b_list=['a','b','c','d','e']
c_dict={'a':[True,False,True],'b':[True,True,True],'c':[False,False,False]}


# In[11]:


a_json_array=json.dumps(a_tuple)
b_json_array=json.dumps(b_list)
c_json_object=json.dumps(c_dict)


# In[12]:


print(a_json_array, type(a_json_array))


# In[13]:


print(b_json_array, type(b_json_array))


# In[15]:


print(c_json_object, type(c_json_object))


# In[47]:


#json.loads(): 將json轉成python。


# In[48]:


json_array='[10,20,30,40,50]'
json_object='{"a":"orange","b":"blue","c": "purple"}'


# In[49]:


python_list=json.loads(json_array)
python_dict=json.loads(json_object)


# In[50]:


print(python_list,type(python_list))


# In[51]:


print(python_dict,type(python_dict))


# In[52]:


# 儲存json檔案


# In[ ]:


# with open(path,'w') as 變數


# In[44]:


a_python_dict={'age':[30,40,50],'name':['Alice','Bruce','Charlie'], 'gender':['Female','Male','Male']}


# In[45]:


path='Desktop/python_practice/test1.json'


# In[83]:


with open(path,'w') as json_obj:
    json.dump(a_python_dict, json_obj)
print('儲存成功')


# In[84]:


# 如果要儲存中文名稱的json檔案，需要輸入encoding='utf-8', ensure_ascii=False


# In[85]:


c_python_dict={'年紀':['50歲','40歲','30歲'], '姓名':
              ['大寶','二寶','小寶'], '性別':['男','女','男']}


# In[86]:


path='Desktop/python_practice/test2.json'


# In[87]:


with open(path,'w', encoding='utf-8') as json_obj2:
    json.dump(c_python_dict, json_obj2, ensure_ascii=False)
print('儲存成功')


# In[88]:


# 讀取json的資料


# In[ ]:


# !cat ___資料位置＿＿＿ 即可直接讀取json檔案


# In[89]:


get_ipython().system('cat desktop/python_practice/test1.json')


# In[90]:


get_ipython().system('cat desktop/python_practice/test2.json')


# In[ ]:


# pd.read_json('資料位置')：可以將資料轉換為一個表格。


# In[91]:


data=pd.read_json('desktop/python_practice/test1.json')


# In[92]:


data


# In[93]:


# to_json：可將pandas的資料匯出成json格式。 orient='records'->列位輸出。


# In[94]:


print(data.to_json())


# In[95]:


print(data.to_json(orient='records'))


# In[96]:


# with open(path) as 變數： 可以直接開啟json檔案


# In[97]:


path='Desktop/python_practice/test1.json'


# In[98]:


with open(path) as json_obj:
    data=json.load(json_obj)


# In[99]:


print(data)


# In[100]:


print(type(data))


# In[101]:


# XML和HTML: 從網站抓資料


# In[ ]:


# 範例的網站：https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/


# In[108]:


# pd.read_html('網址')：嘗試讀取網站的資料，出來的結果會是list。


# In[103]:


tables=pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')


# In[104]:


len(tables)


# In[113]:


failures=tables[0]


# In[112]:


failures.head()


# In[ ]:


# 計算每年的銀行出錯次數close_timestamps


# In[117]:


close_timestamps=pd.to_datetime(failures['Closing DateClosing'])


# In[119]:


close_timestamps.dt.year.value_counts()


# In[124]:


#XML(eXtensible Markup Language): 常用來支援階層式、巢式以及帶metadata的資料結構。


# In[125]:


from lxml import objectify


# In[128]:


path = "Desktop/python_practice/PurchaseOrder.xml"
with open(path) as f:
    parsed = objectify.parse(f)
root = parsed.getroot()


# In[129]:


data=[]


# In[137]:


# 讀取html的標籤


# In[131]:


from io import StringIO


# In[132]:


tag='<a href="http://www.google.com">Google</a>'


# In[133]:


root=objectify.parse(StringIO(tag)).getroot()


# In[134]:


root


# In[135]:


root.get('href')


# In[136]:


root.text


# In[138]:


pip install xmltodict


# In[1]:


# xmltodict: 可以用來將xml的資料轉成python檔案。


# In[2]:


import requests


# In[3]:


import xmltodict


# In[7]:


url="https://ibus.tbkc.gov.tw/xmlbus/GetEstimateTime.xml?routeIds=1421"


# In[8]:


html=requests.get(url).text


# In[9]:


data=xmltodict.parse(html)


# In[11]:


stops=data["BusDynInfo"]["BusInfo"]["Route"]["EstimateTime"]
for stop in stops:
    print(stop["@StopName"], stop["@comeTime"])


# In[1]:


# 二進位資料格式


# In[2]:


# pickle: 儲存二進位資料格式，也稱為序列化。(serialization)


# In[4]:


import pandas as pd
import numpy as np


# In[5]:


frame=pd.read_csv('Desktop/python_practice/example_1.csv')


# In[6]:


frame


# In[7]:


frame.to_pickle('Desktop/python_practice/frame_pickle')


# In[9]:


pd.read_pickle('Desktop/python_practice/frame_pickle')


# In[11]:


# HDF5格式：階層式資料格式（hierarchical data format)，可以有效率儲存資料，可用來處理大體積的資料集。


# In[35]:


frame=pd.DataFrame({'a':np.random.randn(100)})


# In[36]:


store=pd.HDFStore('mydata.h5') #設定一個hdf文件(mydata.h5)


# In[37]:


store['obj1']=frame #將obj1儲存入hdf文件。


# In[38]:


store['obj1_col']=frame['a'] #將obj1_col儲存入hdf文件。


# In[39]:


store


# In[40]:


store['obj1']


# In[41]:


store['obj1_col']


# In[ ]:


# store.put('obj2',frame, format='table') == store('obj2')=frame


# In[18]:


store.put('obj2',frame,format='table')


# In[42]:


# store.select('obj', where=[]) 可以使用SQL查詢語句。


# In[43]:


store.select('obj2',where=['index>=10 and index <=15'])


# In[44]:


store.close() #關閉HDF檔案。


# In[ ]:


# to_hdf（'路徑', 儲存的名稱, format='table'):更直覺的開起hdf檔案。


# In[21]:


frame.to_hdf('mydata.h5','obj3',format='table')


# In[ ]:


# pd.read_hdf('路徑',儲存的名稱,where=[])：更直覺的讀取hdf檔案。


# In[22]:


pd.read_hdf('mydata.h5','obj3',where=['index<5'])


# In[45]:


# 讀取Microsoft Excel檔案


# In[47]:


pip install xlrd


# In[48]:


pip install openpyxl


# In[49]:


xlsx=pd.ExcelFile('Desktop/python_practice/Global Superstore Orders 2016.xlsx')


# In[51]:


orders=pd.read_excel(xlsx,'Orders')


# In[52]:


people=pd.read_excel(xlsx,'People')


# In[53]:


orders.head()


# In[54]:


people.head()


# In[55]:


orders.describe()


# In[58]:


# 將Pandas的資料另存新檔到excel格式。


# In[68]:


a_dataframe=pd.DataFrame(np.arange(12).reshape(3,4), index=['a','b','c'], columns=['one','two','three','four'])


# In[69]:


a_dataframe


# In[ ]:


# pd.ExcelWriter('儲存的新檔案路徑')


# In[70]:


writer=pd.ExcelWriter('Desktop/python_practice/frame1.xlsx') 


# In[ ]:


# to_excel('路徑', '工作表名稱')


# In[71]:


a_dataframe.to_excel(writer,'a_dataframe') 


# In[72]:


writer.save()


# In[ ]:


# 如果不想要這麼麻煩，可以直接使用to_excel('路徑','工作表名稱')


# In[74]:


a_dataframe.to_excel('Desktop/python_practice/frame2.xlsx','a_dataframe')


# In[75]:


# 使用Web API


# In[76]:


# requests: 最容易使用Web API的套件。


# In[77]:


import requests


# In[78]:


url='https://api.github.com/repos/pandas-dev/pandas/issues'


# In[79]:


resp=requests.get(url)


# In[80]:


resp


# In[81]:


data=resp.json()


# In[82]:


data[0]['title']


# In[83]:


issues=pd.DataFrame(data,columns=['number','title','labels','state'])


# In[84]:


issues


# In[85]:


# 使用資料庫


# In[ ]:


# sqlite3: Python內建的資料庫。


# In[86]:


import sqlite3


# In[ ]:


# 創立一個表格叫做test


# In[88]:


query="""
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20), c REAL, d INTERGER
); """


# In[ ]:


# 連接到資料庫con


# In[89]:


con=sqlite3.connect('mydata.sqlite')


# In[ ]:


# 對資料庫con執行query


# In[90]:


con.execute(query)


# In[ ]:


# 完成資料庫更新


# In[91]:


con.commit


# In[ ]:


# 對資料庫con插入資料。


# In[92]:


data=[('Atlanta','Gerogia', 1.25,6),
      ('Tallahassee','Florida',2.6,3),
       ('Scaramento','California',1.7,5)]


# In[93]:


stmt="INSERT INTO test VALUES(?,?,?,?)"


# In[94]:


con.executemany(stmt,data)


# In[ ]:


# 完成資料更新


# In[95]:


con.commit


# In[ ]:


# 取出表格test內所有資料。


# In[96]:


cursor=con.execute('select * from test')


# In[97]:


rows=cursor.fetchall()


# In[98]:


rows


# In[100]:


cursor.description


# In[110]:


pd.DataFrame(rows,columns=[x[0] for x in cursor.description])


# In[111]:


# SQLAlchemy


# In[112]:


import sqlalchemy as sqla


# In[113]:


db=sqla.create_engine('sqlite:///mydata.sqlite')


# In[122]:


pd.read_sql('select * from test' , db)

