import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('/Users/martin_yan/Desktop/mean_data.csv')
#target = np.log(data['减重值'])
#print ("Skew is:", target.skew())
#plt.hist(target, color='blue')
#plt.show()
balanced=[]
totalheat=[]
for i in range(len(data)):
    score=data.iloc[i]['平均得分']
    totalheat.append(data.iloc[i]['总热量摄入量平均分'])
    balanced.append((score-totalheat[i])/12)
#print(balanced)
for i in range(0,10000):
    a=i*0.0001
    print(a)
    for j in range(len(data)):
        data.loc[j,'新得分']=float(balanced[j]*a+totalheat[j]*(1-a))
    print(data['减重值'].corr(data['新得分']))
