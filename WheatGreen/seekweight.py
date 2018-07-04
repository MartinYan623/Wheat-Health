import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('/Users/martin_yan/Desktop/HEI_mean_babymother_data5.22-6.25(总表／入营得分).csv')
data2=pd.read_csv('/Users/martin_yan/Desktop/新热量区间换算热量分值.csv',usecols=['姓名','轻食日热量平均分(入营天数)','普通日热量平均分(入营天数)'])
data = pd.merge(data, data2, on='姓名')

balanced=[]
totalheat=[]
light=[]
normal=[]
for i in range(len(data)):
    #score=data.iloc[i]['平均得分']
    #totalheat.append(data.iloc[i]['总热量摄入量平均分'])
    #balanced.append((score-totalheat[i])/11)
    light.append(data.iloc[i]['轻食日热量平均分(入营天数)'])
    normal.append(data.iloc[i]['普通日热量平均分(入营天数)'])
    balanced.append(data.iloc[i]['饮食均衡得分'] / 12)

best=0
parameter=0
for i in range(0,100):
    for j in range(0, 100):
        a=i*0.01
        b=j*0.01
        print(a)
        print(b)
        for num in range(len(data)):
            data.loc[num,'新得分']=float(light[num]*a+normal[num]*b+balanced[num]*(1-a-b))
        now=data['减重值'].corr(data['新得分'])
        print(now)
        if now>best:
            best=now
            parameter1=a
            parameter2 =b
print('最好的相关性系数是:' + str(best)+', 轻食日分数权重是:'+ str(parameter1)+', 轻食日分数权重是:'+ str(parameter2))