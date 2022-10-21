#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 資料整理和前處理


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


# 處理遺失資料


# In[4]:


# NAN: 在pandas內，遺失的資料表示為NAN，也就是not a number。


# In[5]:


string_data=pd.Series(['a','b','c','d',np.nan,'e'])


# In[6]:


string_data


# In[7]:


string_data.isnull()


# In[8]:


# Python內建中的None值，也是NA。


# In[9]:


string_data[0]=None


# In[10]:


string_data.isnull()


# In[11]:


# 過濾遺失值。


# In[12]:


# dropna(): 可以過濾遺失值。


# In[13]:


from numpy import nan as NA


# In[14]:


data=pd.Series([1,NA,3.5,NA,7])


# In[15]:


data.dropna()


# In[16]:


# notnull(): 就是isnull()的相反，可以顯示布林值。


# In[17]:


data[data.notnull()]


# In[18]:


data=pd.DataFrame([[1,5,7],[NA,6,NA],[NA,NA,NA],[NA,8,9]])


# In[19]:


data


# In[20]:


# 遇到dataframe時，使用dropna()會把有NA的列移除。


# In[21]:


cleaned=data.dropna()


# In[22]:


cleaned


# In[23]:


# dropna(how='all'): 會移除該列每一個數值都是NA的列。


# In[24]:


cleaned2=data.dropna(how='all')


# In[25]:


cleaned2


# In[26]:


data[4]=NA


# In[27]:


data


# In[28]:


data.dropna(axis=1,how='all')


# In[29]:


df=pd.DataFrame(np.random.randn(7,3))


# In[30]:


df


# In[31]:


df.iloc[:4,1]=NA


# In[32]:


df.iloc[:2,0]=NA


# In[33]:


df


# In[34]:


df.dropna()


# In[35]:


# thresh＝2 表示該列至少要有2筆數字非遺失值，才會保留該行。


# In[36]:


df.dropna(thresh=2)


# In[37]:


# 爲遺失值填值。


# In[38]:


# fillna(數字)： 放入常數，就可以在NAN的位置補上一個常數。


# In[39]:


df


# In[40]:


df.fillna(0)


# In[41]:


# fillna(dict): 可以指定欄位，在遺失值的位置填入常數。


# In[42]:


df.fillna({0:20, 1:30})


# In[43]:


# fillna(0): 本身可以存取為獨立的物件。


# In[44]:


a=df.fillna({0:30,1:100})


# In[45]:


a


# In[46]:


# inplace=True 可以直接修改原本的資料。


# In[47]:


df.fillna(0,inplace=True)


# In[48]:


df


# In[49]:


df=pd.DataFrame(np.random.randn(6,3))


# In[50]:


df


# In[51]:


df.iloc[4:,1]=NA


# In[52]:


df.iloc[2:,2]=NA


# In[53]:


df


# In[54]:


# method='ffill' 重複前一個值。


# In[55]:


df.fillna(method='ffill')


# In[56]:


# limit=2，遇到連續的遺失值，限定最多一次可以連續補上2個值。


# In[57]:


df


# In[58]:


df.fillna(method='ffill',limit=2)


# In[59]:


# fillna(data.mean()): 還可以在遺失值的位置補上該數列的平均值、最大值、最小值、中位數等。


# In[60]:


data=pd.Series([1,3,5,NA,6,NA])


# In[61]:


data


# In[62]:


data.fillna(data.mean())


# In[63]:


data.fillna(data.max())


# In[64]:


# 資料的轉換


# In[65]:


# 移除重複值


# In[66]:


data=pd.DataFrame({'k1':['one','two']*3+['one'], 'k2':[1,2,1,2,3,4,3]})


# In[67]:


data


# In[68]:


# duplicated(): 用來判斷該列前面有沒有出現過，有的話，會顯示Ture。


# In[69]:


data.duplicated()


# In[70]:


# drop_duplicates(): 移除重複的值，也就是會保留下duplicated() 顯示為False的地方。


# In[71]:


data.drop_duplicates()


# In[72]:


data['v1']=range(7)


# In[73]:


data


# In[74]:


# 可以針對特定的欄位進行drop_duplicates(), duplicated()


# In[75]:


data.drop_duplicates(['k1'])


# In[76]:


data.duplicated(['k1'])


# In[77]:


# 一般來說，drop_duplicates(), duplicated()會保留看到的第一個值。
# 如果是keep='last'，就會保留看到的最後一個值。


# In[78]:


data.duplicated(['k1','k2'],keep='last')


# In[79]:


data.drop_duplicates(['k1','k2'], keep='last')


# In[80]:


# 使用函式或對應關係轉換值


# In[81]:


data=pd.DataFrame({'food':['Bacon','pork','bacon','Chicken','Beef','chicken','Ham','bacon','ham','beef'],
                   'ounces':[4,6,8,8,10,12,4,3,9,10]})


# In[82]:


data


# In[83]:


origin_of_meat={'bacon':'Taiwan','pork':'Japan','chicken':'France',
                'beef':'Australia','ham':'Spain'}
type(origin_of_meat)


# In[84]:


# 由於data有些大寫、有些小寫，透過str.lower()全面改成小寫。


# In[85]:


lowercased=data['food'].str.lower()


# In[86]:


print(lowercased, type(lowercased))


# In[87]:


# 透過series.map(dict)，可以對應出每一個肉品的產地。


# In[88]:


lowercased.map(origin_of_meat)


# In[89]:


data['origin']=lowercased.map(origin_of_meat)


# In[90]:


data


# In[91]:


# 也可以僅透過一個式子就完成配對。


# In[92]:


data['food'].map(lambda x: origin_of_meat[x.lower()])


# In[93]:


# 取代值


# In[94]:


data=pd.Series([10,-999,20,-999,30,-999,100])


# In[95]:


data


# In[96]:


# -999可能是遺失值，需要改寫為NAN，可以使用replace()


# In[97]:


a=data.replace(-999,np.nan)
a


# In[98]:


# inplace=Ture 可以直接修改原始資料


# In[99]:


# 如果一口氣要取代許多值，可以用[]呈現。


# In[100]:


data.replace([-999,100], np.nan, inplace=True)


# In[101]:


data


# In[102]:


data=pd.Series([10,-999,20,-999,30,-999,100])


# In[103]:


# 如果想要置換不同的值，也可以使用雙括號。


# In[104]:


data.replace([-999,100],[np.nan,0])


# In[105]:


# 也可以在replace()內放入dict。


# In[106]:


data.replace({-999:np.nan, 100: 0})


# In[107]:


# 更名軸index


# In[108]:


data=pd.DataFrame(np.arange(12).reshape(3,4),index=['France','Spain','Netherland'], 
                  columns=['first','second','third','fourth'])


# In[109]:


data


# In[110]:


# index 透過map也可以做格式化的調整。


# In[111]:


transform=lambda x:x[:3].upper()


# In[112]:


data.index.map(transform)


# In[113]:


# 直接對index給值，就可以原地進行資料調整。


# In[114]:


data.index=data.index.map(transform)


# In[115]:


data


# In[116]:


# 如果不想動到原本的東西，可以使用rename。


# In[117]:


data.rename(index=str.title, columns=str.upper)


# In[118]:


# rename(index={}, columns={})：可以放入dict，修改標籤名稱。


# In[119]:


data.rename(index={'NET':'ENL'}, columns={'fourth':'third'})


# In[120]:


# rename() 如果加上inplace=True，就可以很節省時間的直接修改原始資料。


# In[121]:


data.rename(index={'NET':'ENL'}, inplace=True)


# In[122]:


data


# In[123]:


# 離散化和分組


# In[124]:


ages=[18,19,20,22,25,27,30,32,40,45,50,56,60,61,70,79]


# In[125]:


# 將年齡分為18-25, 25-35, 35-45, 55-65, 65以上。


# In[126]:


bins=[18,25,35,55,65,100]


# In[127]:


cats=pd.cut(ages,bins)


# In[128]:


# 小括號代表open，中括號代表close。


# In[129]:


cats


# In[130]:


# 使用cuts可以將資料做分群，會產生特殊的categorical物件，可以透過codes看到categorical陣列。


# In[131]:


cats.codes


# In[132]:


# categories 可以看出有哪些分群。


# In[133]:


cats.categories


# In[134]:


# value_counts() 可以計算每個分群有幾筆數值。


# In[135]:


pd.value_counts(cats)


# In[136]:


# right=flase 表示右邊的值為closed。


# In[137]:


cats=pd.cut(ages,bins, right=False)


# In[138]:


cats


# In[139]:


# 指定名稱給lables，就可以幫不同的分群取名。


# In[140]:


group_name=['Youth','Young_Adult','Middle_Age','Seniors','Elders']


# In[141]:


pd.cut(ages,bins,labels=group_name)


# In[142]:


data=np.random.randn(20)


# In[143]:


# 除了給bins，也可以指定分成4群。


# In[144]:


# precision=2,表示小數點後兩位。


# In[145]:


pd.cut(data,4,precision=2)


# In[146]:


# cut依據資料的分佈，分組時有時後會每組樣本數不同，使用qcut就可以平均分配樣本數囉！


# In[147]:


data=np.random.randn(1000) #常態分佈


# In[148]:


cats=pd.qcut(data,4)


# In[149]:


pd.value_counts(cats) #平均分配


# In[150]:


cats2=pd.cut(data,4)


# In[151]:


pd.value_counts(cats2) #依照數值區間分配


# In[152]:


# 偵測和濾除離群值


# In[153]:


data=pd.DataFrame(np.random.randn(100,4))


# In[154]:


data


# In[155]:


data.describe()


# In[156]:


col=data[2]


# In[157]:


col[np.abs(col)>2]


# In[158]:


data[(np.abs(data)>3).any(1)]


# In[159]:


data[np.abs(data)>3]=np.sign(data)*3


# In[160]:


data.describe()


# In[161]:


# sign(): 如果正值，給1，如果負值，給-1。


# In[162]:


np.sign(data).head()


# In[163]:


# 排列與隨機取樣


# In[164]:


# np.random.permutation(n): 會將0~n-1的數列隨機排序。


# In[165]:


np.random.permutation(7)


# In[166]:


df=pd.DataFrame(np.arange(5*4).reshape(5,4))


# In[167]:


sampler=np.random.permutation(5)


# In[168]:


sampler


# In[169]:


df


# In[170]:


# take(array): 可以將index換成array內的數值。


# In[171]:


df.take(sampler)


# In[172]:


# sample(n=4) 表示可以隨機從原數據挑選兩行。


# In[173]:


df.sample(n=4)


# In[174]:


df.sample(n=3)


# In[175]:


choices=pd.Series([5,7,-1,6,4])


# In[176]:


choices


# In[177]:


# 如果想抽取的資料行數大於原本的資料，就必須填入replace=True，才可以重複抽取。


# In[178]:


draws=choices.sample(n=10,replace=True)


# In[179]:


a=choices.sample(n=3)
a


# In[180]:


draws


# In[181]:


# 指標、虛擬變數


# In[182]:


# pd.get_dummies(): 可以告訴你變數的所在位置，該位置會顯示為1。


# In[183]:


df=pd.DataFrame({'key':['a','a','b','b','c','c'], 'data1':range(6)})


# In[184]:


df


# In[185]:


pd.get_dummies(df['key'])


# In[186]:


# prefix='key' 可以在欄位名稱上做註記，表示是key欄位的a的所在位置。


# In[187]:


dummies=pd.get_dummies(df['key'], prefix='key')


# In[188]:


dummies


# In[189]:


# join(): 以index為key值，使用join可以合併兩個表格。


# In[190]:


df_with_dummy=df[['data1']].join(dummies)


# In[191]:


df_with_dummy


# In[192]:


pd.get_dummies(df)


# In[193]:


movies=pd.DataFrame({'movie_id':range(10),
                     'title': ['Toy Story(1995)','Jumanji(1995)','Grumpier Old Man(1995)',
                              'Waiting to Exhale(1995)','Father of the Bride Part II(1995)',
                              'Heart(1995)','Sabrina(1995)','Tom and Huck(1995)','Sudden Death(1995)',
                              'Goldeneye(1995)'],
                    'genres': ['Animation|Children\'s|Comedy','Adventure|Children\'s|Fantasy',
                               'Comedy|Romance','Comedy|Drama','Comedy','Action|Crime|Thriller',
                               'Comedy|Romance','Adventure|Children\'s','Action','Action|Adventure|Thriller']})


# In[194]:


movies


# In[195]:


all_genres=[]


# In[196]:


# x.split('|'): 移除文字與文字之間的符號。


# In[197]:


for x in movies.genres:
    all_genres.extend(x.split('|'))


# In[198]:


# pd.unique: 移除重複值。


# In[199]:


genres=pd.unique(all_genres)


# In[200]:


genres


# In[201]:


# np.zeros（x,y): 可以製作x*y的矩陣，並以0為值。


# In[202]:


# len(movies): 表示movies的列數有10列。 len(genres): 表示genres有10個品項。


# In[203]:


zero_matrix=np.zeros((len(movies),len(genres)))


# In[204]:


zero_matrix


# In[205]:


dummies=pd.DataFrame(zero_matrix, columns=genres)


# In[206]:


dummies


# In[207]:


movies


# In[208]:


gen=movies.genres[0]
gen


# In[209]:


gen.split('|')


# In[210]:


dummies


# In[211]:


dummies.columns.get_indexer(gen.split('|'))


# In[212]:


for i, gen in enumerate(movies.genres):
    indices= dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i,indices]=1


# In[213]:


movies_windic=movies.join(dummies.add_prefix('Genre_'))


# In[214]:


movies_windic


# In[215]:


movies_windic.iloc[6]


# In[216]:


np.random.seed(12345)


# In[217]:


# np.random.rand() 會出現n個介於0-1的數值。


# In[218]:


values=np.random.rand(10)
values


# In[219]:


bins=[0,0.2,0.4,0.6,0.8,1]


# In[220]:


#pd.cut(values,bins)：先對資料進行分組。 pd.get_dummies(): 可以找出每個數值在群組中的位置。


# In[221]:


pd.get_dummies(pd.cut(values,bins))


# In[222]:


# 字串操作


# In[223]:


# split('標點符號')：依據標點符號的位置，可以切分文字。


# In[224]:


string='a,b, hello'


# In[225]:


string.split(',')


# In[226]:


# strip(): 可以移除前後空白（包括換行）


# In[227]:


pieces= [x.strip() for x in string.split(',')]


# In[228]:


pieces


# In[229]:


# ＋：字串可以用加號連結起來。


# In[230]:


first, second, third= pieces


# In[231]:


first+'::'+second+'::'+third


# In[232]:


#‘文字’.join(物件): 可以將點點前面的文字串連到每一個join內的物件。


# In[233]:


'::'.join(pieces)


# In[234]:


# in : 可以確認該物件是否有在tuple, list, dict內。


# In[235]:


'hello' in pieces


# In[236]:


# index():可以尋找文字所在位置。


# In[237]:


string


# In[238]:


string.index('hello')


# In[239]:


string.index(' ')


# In[240]:


string.index(',')


# In[241]:


string.index(':') #如果找不到該物件，會顯示ValueError。


# In[242]:


# find(): 可以尋找文字。


# In[243]:


string.find('hello')


# In[244]:


string.find(' ')


# In[245]:


string.find(':') #如果找不到該物件，會顯示-1。


# In[246]:


# count(): 計算文字出現次數。


# In[247]:


string.count(',')


# In[248]:


# replace(a,b): 可以用來替換字串，a表示原本的字串，b表示修改後的字串。


# In[249]:


string.replace('a', 'd')


# In[250]:


string


# In[251]:


# 正規表達式(regular expression): re模組。


# In[252]:


import re


# In[253]:


# \t代表3個空白。


# In[254]:


print(f'apple   bread')


# In[255]:


print(f'apple\tbread')


# In[256]:


text="apple \tbread  \tberry   \ttriangle"


# In[257]:


text


# In[258]:


#'\s+': 表示tab, 空白或換行。 split('\s+'): 表示文字遇到tab,空白或換行，就用逗號區隔開來。


# In[259]:


re.split('\s+', text)


# In[260]:


re.compile(text)


# In[261]:


# re.compile('功能')：可以將一直會寫到的功能放進來，就可以出現一個功能函式物件。


# In[262]:


# regex= regular expression 正規表達式


# In[263]:


regex=re.compile('\s+')


# In[264]:


regex


# In[265]:


regex.split(text)


# In[266]:


# findall()： 可以找到所有對應regex功能的物件，並顯示出來。


# In[267]:


regex.findall(text)


# In[268]:


# match(): 對比字串的開頭是否匹配。


# In[269]:


text="""Dave dave@google.com
Steve steve@gmail.com
Rob rob@gamil.com
Ryan ryan@yahoo.com"""


# In[270]:


# r: 表示字串不會被轉譯，例如\n就會換行。
# [a-zA-Z0-9]: 表示大寫小寫字母與數字都可以。
# . :表示點點之後的文字與符號都可以（但是不包括換行）。
# +: 表示加號之後的文字至少要出現一次。
# \ : 跳脫字元，使後面的文字不要產生功能。
# {m,n}: 表示大括號前的文字僅能重複m~n次。


# In[271]:


pattern=r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'


# In[272]:


# flags=re.IGNORECASE 忽略字母大小寫。


# In[273]:


regex=re.compile(pattern,flags=re.IGNORECASE)


# In[274]:


# 找出所有符合regex格式的信箱。


# In[275]:


regex.findall(text)


# In[276]:


# search()：會找到第一個符合regex的字串。


# In[277]:


m=regex.search(text)


# In[278]:


m


# In[279]:


# start(): 顯示字串的開頭。 end(): 顯示字串的結束。


# In[280]:


text[m.start():m.end()]


# In[281]:


#match:只會檢查字串的開頭是否匹配，如果不匹配，回傳None。


# In[282]:


text


# In[283]:


#由於text第一個字為Dave，並非regex定義的信箱格式，故回傳None，如果符合regex的格式，回傳第一個符合的物件。


# In[284]:


print(regex.match(text))


# In[285]:


text2="""dave@google.com
steve@gmail.com
rob@gmail.com"""


# In[286]:


print(regex.match(text2))


# In[287]:


# sub('取代後的文字', 原本的字串)：sub可以找到符合regex的字串，並取代成新的文字。


# In[288]:


print(regex.sub('REDACTED', text))


# In[289]:


# 在pattern內把想要切斷的文字放上小括號。（）


# In[290]:


pattern=r'([A-Z0-0._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'


# In[291]:


# flags=re.IGNORECASE 忽略字母的大小寫。


# In[292]:


regex=re.compile(pattern,flags=re.IGNORECASE)


# In[293]:


m=regex.match('wesm@bright.net')


# In[294]:


# groups(): 將小括號內的文字提出來，成為一個tuple。


# In[295]:


m.groups()


# In[296]:


# findall(text): 由於regex已經先分成三個物件，故在取出物件時，也會分成三份。


# In[297]:


regex.findall(text)


# In[298]:


# r: 表示保留原始文字，不做轉譯。
# sub(\1,\2,\3): 透過\1, \2, \3 可用來代表取出來按照排序的文字的物件。


# In[299]:


print(regex.sub(r'Username: \1, Domain: \2,  Suffix:\3', text))


# In[300]:


#pandas中的向量字串函式。


# In[301]:


data={'Dave':'dave@google.com', 'Steve': 'steve@gmail.com', 'Rob':'rob@gmail.com', 'Wes':np.nan}


# In[302]:


data=pd.Series(data)


# In[303]:


data


# In[304]:


data.isnull()


# In[305]:


# str.contains(): 找到是否包含此字串的物件。


# In[307]:


data


# In[306]:


data.str.contains('gmail')


# In[ ]:


# 如果要對表格每一行執行findall(), match()，記得要在前方加上str.


# In[308]:


pattern


# In[309]:


data.str.findall(pattern,flags=re.IGNORECASE)


# In[312]:


matches=data.str.match(pattern,flags=re.IGNORECASE)


# In[313]:


matches


# In[323]:


matches.dropna(inplace=True)


# In[324]:


matches.str.get(1)


# In[325]:


matches.str[0]


# In[327]:


# str[]: 可以對字串做切片。


# In[328]:


data.str[:5]

