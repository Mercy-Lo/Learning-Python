#!/usr/bin/env python
# coding: utf-8

# In[51]:


## 檔案和作業系統


# In[52]:


# path: 輸入檔案的路徑。


# In[101]:


path='desktop/example1'


# In[102]:


# open(): 可以傳入路徑。


# In[103]:


f=open(path)


# In[104]:


for line in f:
    pass


# In[105]:


lines =[x.rstrip() for x in open(path)]
lines


# In[106]:


# close() 關閉很重要！關閉檔案會讓它佔用的資源還給系統。


# In[107]:


f.close()


# In[108]:


# with 的設定，可以讓自己不會忘記關閉檔案。


# In[109]:


with open(path) as f:
    lines =[x.rstrip() for x in f]


# In[62]:


# w代表建立新檔，會覆寫所有資料。


# In[63]:


path2='desktop/example0'
f=open(path,'w')


# In[47]:


# x代表建立新檔，如果檔案已存在，則失敗。


# In[65]:


path3='desktop/example1'
f2=open(path3,'x')


# In[32]:


# read(), seek(), tell()


# In[83]:


path2='desktop/example0'
f=open(path2)


# In[84]:


f.read()


# In[85]:


# rb代表2進位模式。


# In[86]:


f2= open(path2,'rb')


# In[87]:


f2.read()


# In[110]:


lines2 =[x.rstrip() for x in open(path2)]
lines2


# In[88]:


# tell(): 告訴你位置在何處。


# In[89]:


f.tell()


# In[90]:


f2.tell()


# In[91]:


# 使用sys模組看預設的編碼是什麼。


# In[92]:


import sys


# In[94]:


sys.getdefaultencoding()


# In[95]:


# seek(): 改變目前檔案以位元組為單位的檔案位置。


# In[96]:


f.seek(5)


# In[97]:


f.read(1)


# In[111]:


f.close()


# In[112]:


f2.close()


# In[113]:


# 若想要將文字寫入到檔案中，可以使用write或是writelines。


# In[114]:


with open('tmp.txt','w')as handle:
    handle.writelines(x for x in open(path) if len(x)>1)


# In[115]:


with open ('tmp.txt') as f:
    lines = f.readlines()


# In[116]:


lines


# In[117]:


# 檔案中的位元組與Unicode。


# In[119]:


with open(path) as f:
    chars=f.read(10)
chars


# In[ ]:


# 如果放入rb的格式，可以指定b到檔案中。(binary 二元制)


# In[120]:


with open(path,'rb') as f:
    data=f.read(10)


# In[121]:


data


# In[122]:


# 自行將位元組編碼為str物件。


# In[123]:


data.decode('utf8')


# In[124]:


data[:4].decode('utf8')


# In[125]:


# 可以指定endcoding。


# In[126]:


sink_path='sink.txt'


# In[127]:


with open(path) as source:
    with open(sink_path, 'xt', encoding='iso-8859-1') as sink:
        sink.write(source.read())


# In[129]:


with open(sink_path, encoding='iso=8859-1')as f:
    print(f.read(10))


# In[130]:


f=open(path)


# In[131]:


f.read(5)


# In[132]:


f.seek(4)


# In[133]:


f.read(1)

