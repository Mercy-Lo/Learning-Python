#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Function Introduction


# In[2]:


# 函式使用時機點：你預期一些程式碼會被重複使用，就可以寫成一個函式。


# In[3]:


def my_function(x,y,z=1.5):
    if z > 1:
        return z*(x+y)
    else:
        return z/(x+y)


# In[4]:


# x, y為位置參數(positional parameter), z為關鍵字參數(keyword parameter)，關鍵字參數必須出現在位置參數後面。


# In[5]:


my_function(10,20,5)


# In[6]:


my_function(14,18,0.2)


# In[7]:


my_function(10,20) #系統會自動將數字按照順序給位置參數，而關鍵參數由於已經有定義值，運算就可以順利進行。


# In[12]:


my_function(z=0.2, y=100, x=100) #也可以直接寫出每個參數的名稱，就不需要在乎順序。


# In[13]:


# Global Scope v.s. Local Scope


# In[14]:


# 在函式內的變數屬於Local Scope，出了函式外就不可以使用，Global Scope為函式外的變數，可以被不同的公式所取用，不會消失。


# In[62]:


def func():

# 因為在函式裡面，這裡的a為local scope，函式結束即消失。

    a=[]
    for i in range(5):
        a.append(i)
    return a 


# In[63]:


func()


# In[66]:


# 因為在函式外面，這裡的a為global scope，並不會消失。

a=[]
def func():
    for i in range(5):
        a.append(i)
    return a 


# In[67]:


func()


# In[ ]:


# 函式的好處：可以回傳多個值。


# In[38]:


def f():
    a=5
    b=6
    c=7
    return a,b,c
a,b,c=f()


# In[40]:


print(a,b,c) 


# In[68]:


def f():
    a=6
    b=7
    c=8
    return {'a':a, 'b':b, 'c':c}

# 可以寫成dict的型態。


# In[69]:


f()


# In[48]:


# 函式即物件，透過re整理不規則的文字。


# In[53]:


country=['!Taiwan','JAPAN?','spain#','?new zeaLAND','  iceland ']


# In[54]:


import re


# In[55]:


# 透過clean_strings 定義出我們最後要呈現的list。

def clean_strings(country):
    result=[]

# strip()移除前後空格 ; sub()移除符號 ; title()開頭要大寫。

    for value in country:
        value=value.strip()
        value=re.sub('[!#?]', '', value)
        value=value.title()
        result.append(value)
    return result


# In[56]:


clean_strings(country)


# In[94]:


country=['!Taiwan','JAPAN?','spain#','?new zeaLAND','  iceland ']

# 定義一個可以移除標點符號的函式remove_punctuation
def remove_punctuation(value):
    return re.sub('[!#?]','',value)


clean_ops=[str.strip,remove_punctuation,str.title]

def clean_strings(strings, ops):
    result=[]
    for value in strings:
        for function in ops:
            value=function(value)
        result.append(value)
    return result


# In[95]:


clean_strings(country,clean_ops)


# In[96]:


# map(): 可以將一個函式變成另一個函式的參數。


# In[97]:


def remove_punctuation(value):
    return re.sub('[!#?]','',value)
    
for x in map(remove_punctuation, country):
    print(x)


# In[98]:


# 匿名Lambda函式


# In[99]:


def short_function(x):
    return x*2


# In[102]:


short_function(5)


# In[109]:


# equiv_anon 可以替換為其他的文字。
# lambda可以直接拿來定義函式，比def return精簡許多。

equiv_anon=lambda x: x*2


# In[110]:


equiv_anon(10)


# In[111]:


def apply_to_list(some_list,f):
    return [f(x) for x in some_list]
ints=[4,0,1,5,6]
apply_to_list(ints, lambda x:x*2)


# In[112]:


strings=['tv','lamp','sofa','kitchen']
strings.sort(key=lambda x: len(set(list(x))))


# In[113]:


strings


# In[114]:


# 柯里化（currying): 是一個計算機科學術語，代表只給現有函式加上部份變數，之後衍生出新函式的動作。


# In[115]:


def add_number(x,y):
    return x+y


# In[116]:


# 如果只提供一個value給add_number，會衍生出一個新的函式add_five。


# In[117]:


add_five=lambda y:add_number(5,y)


# In[118]:


# 這代表add_number的第二個參數ｙ被柯里化。


# In[119]:


# functools 內的partial 可以簡化柯里化的流程，也就是更快速定義一個新的函式。


# In[121]:


from functools import partial


# In[123]:


add_five=partial(add_number,5)


# In[129]:


add_five(100)


# In[183]:


# [補充說明] format()用法


# In[184]:


print('This article is written by {}.'.format('Python'))


# In[185]:


# format常與print做搭配，print的內容可以放置大括號{}，句末再加上.format()，就可以定義{}內要填入的內容囉！


# In[192]:


a='{},{},{} are the keys to success.'
print(a.format('Positivity',' persistence', ' and bravery'))


# In[189]:


# {0},{1} 代表forma的index()。


# In[193]:


print('{1},{0} are nice learning process.'.format(' Coursera','Udemy'))


# In[130]:


# 產生器(generator): 是產生一個新疊代物件的簡便方式，產生器可以回傳多個結果序列。


# In[131]:


# 疊代器協定 （itrtator protovol): 一種讓物件可以疊代的通運方法。


# In[ ]:


# 使用for迴圈，可以將dict帶入Python直譯器，傳出一個又一個的物件。


# In[133]:


some_dict={'a':1,'b':2,'c':3,'d':4,'e':5}

for key in some_dict:
    print(key)


# In[ ]:


# iter(): 定義待確認。


# In[138]:


dict_iterator=iter(some_dict)


# In[139]:


dict_iterator


# In[140]:


list(dict_iterator)


# In[181]:


# def 中的return每次只能回傳一個值，如果要一次回傳多值，則需改為yield。


# In[ ]:


# 觀察return()在squares()的回傳值個數。


# In[182]:


def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n**2))
    for i in range(1,n+1):
        return i**2

squares()


# In[ ]:


# yield()對於函式squares()為元素產生器()，故單純呼叫gen不會有值出現，需要搭配for迴圈，讓值顯示出來。


# In[201]:


def squares(n=10):
    print('Generating squares from 1 to {}'.format(n**2))
    for i in range(1,n+1):
        yield i**2


# In[202]:


gen=squares()
gen


# In[203]:


for x in gen:
    print(x, end=' ')


# In[205]:


# 產生器述句(Generator Expression): 最簡易的方式製作產生器，需寫在小括號（）內。


# In[209]:


# 原先透過def yield製作generator，需要比較長的語法。


# In[226]:


def _make_gen(): 
    for x in range(11):
        yield x **2
        
gen=_make_gen()
gen


# In[227]:


# 現在透過小括號，可以直接快速產出一個generator。


# In[228]:


gen=(x**2 for x in range(11))
gen


# In[225]:


for x in gen:
    print(x)


# In[ ]:


# 器述句（Generator Expression)的方便之處在於可以直接進行sum, dict, tuple等函式運算。


# In[229]:


sum(x**2 for x in range(11))


# In[230]:


dict((i,i**2) for i in range(6))


# In[232]:


# itertools Module 模組內的groupby(): 可以接受任一list, function當參數，依照函式回傳值將序列中連續元素進行分組。


# In[ ]:


# groupby()運作方式： group_by(iterable, func_key)


# In[233]:


import itertools


# In[238]:


# first_letter是一個function，裡面的值為元素的index=0。

first_letter=lambda x:x[0]

names=['Adam','Alan','Wes','Will','Albert','Steven']

for letter, names in itertools.groupby(names,first_letter):
    print(letter, list(names))


# In[240]:


# 錯誤與例外處理: try, except


# In[241]:


float('2.5678')


# In[246]:


float('a')


# In[247]:


# 為了在ValueError的發生時，有對應的說明視窗出現，可以使用try, except。


# In[275]:


def attempt_float(x):
    try:
        return float(x)
    except:
        return x


# In[276]:


attempt_float('a')


# In[277]:


# 不過，除了ValueError，可能也會有TypeError，可以多捕捉不同型態的Error，給予對應的說明。


# In[291]:


def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x


# In[294]:


attempt_float((1,2))


# In[298]:


# finally(): 如果try()執行失敗，就使用finally()


# In[299]:


# else(): 只要try()執行成功，else()後面也會被執行。

