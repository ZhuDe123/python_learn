import pandas as pd
import numpy as np

"""
1.创建一个DataFrame(df)，用data做数据，labels做行索引
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
      'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
      'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
      'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
2.查看此df的前三行数据
3.选择df中列标签为animal和age的数据
4.选择行为[3, 4, 8]，且列为['animal', 'age']中的数据
5.选择visits大于3的行
6选择age为缺失值的行
7选择animal为cat，且age小于3的行
8选择age在2到4之间的数据(包含边界值)
9将f行的age改为1.5
10计算visits列的数据总和
11计算每种animal的平均age
12追加一行(k)，列的数据自定义，然后再删除新追加的k行
13计算每种animal的个数(cat有几个，dog几个...)
14先根据age降序排列，再根据visits升序排列
15将priority列的yes和no用True和False替换
16将animal列的snake用python替换
"""

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data=data, index=labels)

# 2.查看此df的前三行数据
print(df.head(3))

# 3.选择df中列标签为animal和age的数据
print(df.loc[:, ['animal', 'age']])

# 4.选择行为[3, 4, 8]，且列为['animal', 'age']中的数据
print(df.iloc[[3, 4, 8], [0, 1]])

# 5.选择visuts大于3的行
print(df[df['visits'] >= 3])

# 6选择age为缺失值的行
# 找出所有空行
print(df[df.isnull().T.any()])

# 7选择animal为cat，且age小于3的行
df[(df['animal'] == 'cat') & (df['age'] < 3)]

# 8选择age在2到4之间的数据(包含边界值)
df[(df['age'] >= 2) & (df['age'] <= 4)]

# 9将f行的age改为1.5
df.loc['f','age']=1.5

# 10计算visits列的数据总和
print(df['visits'].sum())

# 11计算每种animal的平均age
print(df.groupby('animal')['age'].mean())

# 12追加一行(k)，列的数据自定义，然后再删除新追加的k行
k = {'animal': 'cat',
      'age': 2.5,
      'visits': 1,
      'priority': 'yes'}
# 增加
df.loc['k',:] = k
# 删除
df.drop('k',inplace=True)

# 13计算每种animal的个数(cat有几个，dog几个...)
print(df.groupby('animal').count())

# 14先根据age降序排列，再根据visits升序排列
df.sort_values(['age','visits'],ascending=(False,True))

# 15将priority列的yes和no用True和False替换
for i in range(0, len(df)):
    if df.iloc[i,3] == 'yes':
        df.iloc[i,3]="True"
    if df.iloc[i,3] == 'no':
        df.iloc[i,3]="False"

# 16将animal列的snake用python替换
for i in range(0, len(df)):
    if df.iloc[i,0] == 'snake':
        df.iloc[i,0]="python"