import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.11.csv')
#target = np.log(data['减重值'])
#print ("Skew is:", target.skew())
#plt.hist(target, color='blue')
#plt.show()
balanced=[]
totalheat=[]
for i in range(len(data)):
    score=data.iloc[i]['平均得分']
    totalheat.append(data.iloc[i]['总热量摄入量平均分'])
    balanced.append((score-totalheat[i])/11)
#print(balanced)
best=0
parameter=0
for i in range(0,1000):
    a=i*0.001
    print(a)
    for j in range(len(data)):
        data.loc[j,'新得分']=float(balanced[j]*a+totalheat[j]*(1-a))
    now=data['减重值'].corr(data['新得分'])
    print(now)
    if now>best:
        best=now
        parameter=a
print('最好的相关性系数是:' + str(best)+', 饮食均衡分数权重是:'+ str(parameter))