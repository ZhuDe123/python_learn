import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('couplet.xlsx')
# 自定义画布
# plt.figure(figsize=(400,100),facecolor='r')
plt.grid(axis='y')
x=df['step']
y=df['loss']
plt.plot(x,y,color='r')
plt.show()
