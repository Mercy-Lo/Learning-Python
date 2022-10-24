# Python for Data Analysis, 2nd Edition
by Wes McKinney, published by O'Reilly Media

# Outline
-  Chapter 1: 寫在前面 Advanced NumPy
-  Chapter 2: Python基礎、IPython和Jupyter Notebook
-  Chapter 3: 內建資料結構、函式和檔案 Bulit-in Data Structure, Functions and Structures
-  Chapter 4: Numpy基礎：陣列和向量化計算 Numpy Basics: Arrays and Vectorized Computation
-  Chapter 5: 使用Pandas Getting Started with pandas
-  Chapter 6: 資料載入、儲存和檔案格式 Data Loading, Storage, and File Formats
-  Chapter 7: 資料整理和前處理 Data Cleaning and Preparation 
-  Chapter 8: 資料處理：連接、合併和重塑 Data Wrangling: Join, Combine and Reshape
-  Chapter 9: 繪圖與視覺化 Plotting and Vitualizaiton 
-  Chapter 10: 資料聚合與分組 Data Aggregation and Group Operations 
-  Chapter 11: 時間序列 Time Series
-  Chapter 12: Pandas 進階 Advanced Pandas 
-  Chapter 13: Python 中的建模函式庫 Introdction to Modeling Libraries in Python 
-  Chapter 14: 資料分析範例 Data Analysis Examples 
-  附錄A: 深入Numpy Advanced Numpy

# Chapter 1
- Python 3.6
- Anaconda-Navigator: Jupyter Notebook

# Chapter 2
- mutable v.s. immutable 
- scalar: None, str, bytes, float, bool, int
- 控制流程: if, elif, else/ for 迴圈 / continue v.s. break/ while 迴圈/ pass
- [[Python0]_Basic_Concept.ipynb ](https://github.com/Mercy-Lo/Learning-Python/blob/main/%5BPython0%5D_Basic_Concept.ipynb)

# Chapter 3
- [[Python1] Tuple Introduction.ipynb](https://github.com/Mercy-Lo/Learning-Python/blob/4a7fd7c9c062eef564c1aca692b72c46ac968dff/%5BPython1%5D%20Tuple%20Introduction.ipynb)
- [[Python2] List Introduction.ipynb](https://github.com/Mercy-Lo/Learning-Python/blob/4a7fd7c9c062eef564c1aca692b72c4[6ac968dff/%5BPython2%5D%20List%20Introduction.ipynb)
- [[Python3] Slices Introduction.ipynb](https://github.com/Mercy-Lo/Learning-Python/blob/main/%5BPython3%5D%20Slices%20Introduction.ipynb)
- [[Python4] enumerate( ), sorted( ), zip( ), reverse( ).ipynb](https://github.com/Mercy-Lo/Learning-Python/blob/main/%5BPython4%5D%20enumerate(%20)%2C%20sorted(%20)%2C%20zip(%20)%2C%20reverse(%20).ipynb)
- [[Python5] Dict Introduction.ipynb](https://github.com/Mercy-Lo/Learning-Python/blob/main/%5BPython5%5D%20Dict%20Introduction.ipynb)
- [[Python6] Set Introduction.ipynb](https://github.com/Mercy-Lo/Learning-Python/blob/main/%5BPython6%5D%20Set%20Introduction.ipynb)
- [[Python7] List, Set, Dict Comprehension.ipynb](https://github.com/Mercy-Lo/Learning-Python/blob/main/%5BPython7%5D%20List%2C%20Set%2C%20Dict%20Comprehension.ipynb)
- [[Python8] Function Introduction.ipynb](https://github.com/Mercy-Lo/Learning-Python/blob/main/%5BPython8%5D%20Function%20Introduction.ipynb)
- [[Python9] File, system and unicode.ipynb](https://github.com/Mercy-Lo/Learning-Python/blob/main/%5BPython9%5D%20File%2C%20system%20and%20unicode.ipynb)

# Chapter 4 
- import numpy as np
- shape / dtype /nidm / astype
- np.array/np.zeros/np.arange/ np.in1d
- array slices 
- data[boolean] / arr[[[],[]] 
- np.arrange(15).reshape((3,5)) / np.random.randn(6,3)/ np.dot/ arr.T
- arr.transpose / arr.swapaxes / arr.sort 
- numpy.where=x if condition else y
- np.save v.s. np.load

# Chapter 5
- import pandas as pd
- Series / DataFrame
- isnull v.s. notnull
- Pandas Index v.s. Python Set 
- reindex / method='ffill'
- drop/ inplace=True
- loc v.s. iloc
- frame.apply(f)/ frame.applymap(format)
- sort_index()/ sort_values() 
- rank/ method: average/ min/ max/ first/ dense
- is_unique
- mean/ skipna=False
- idxmax/cumsum/describe
- isin/ apply/ fillna(0)

# Chapter 6
- !cat desktop/practice_python/example01
- pd.read_csv('desktop/practice/python/example01')
- pd.options.display.max_rows
- json.loads v.s. json.dumps 
- pd.read_html
- xml: root/ root.get('href')/ root.text
- to_pickle/ pd.HDFStore/ frame.to_hdf
- pd.ExcelFile / pd.read_excel/ frame.to_excel
- web API: requests/ url/ requests.get(url)
- pd.read_sql

# Chapter 7
- np.nan: dropna/ fillna/ isnull/ notnull
- dropna / how='all'/ thresh=2
- fillna / method='ffill'/ limit=2/ data.mean()
- duplicated/ drop_duplicates / keep='last'
- str.lower()
- lowercased.map(meat_to_animal)
- repalce(x,y) / rename
- pd.cut(ages, bins, lables=group_names) /cats.codes/cats.categories / precision=2
- pd.value_counts(cats) / pd.qcut(data,4)
- np.random.permutation
- df.take(sampler)
- pd.get_dummies / dummies.columns
- get_indexer 
- split v.s. strip
- val.index() v.s. val.find() v.s. val.count() v.s. val.replace()
- regular expression
- regex=re.compile('\s+')
- regex.findall()/ regex.search()/ regex.match()/ regex.sub()
- str.contains()/ str.match()/ str.get()/ srt[0]

# Chapter 8
- MultiIndex
- unstack() v.s. stack()
- index.names() v.s. columns.names()
- pd.MulitiIndex.from.arrays
- swaplevel() / sort_index() 
- set_index() / reset_index()
- pd.merge v.s. pd.concat
- np.concatenate
- b.combime_first(a)
- pivoted=ldata.pivot(index, columns, value)
- reshaped=melted.pivot('index', 'columns', value)
- reset_index()
- pd.melt(df, value_vars=['key','A','B']

# Chapter 9
- %matplotlib notebook
- import matplotlib.pyplot as plt
- plt.plot(data)
- fig=plt.figure()
- ax1=fig.add_subplot(x,y,n)

-- to be updated...--

<!---
Mercy-Lo/Mercy-Lo is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
