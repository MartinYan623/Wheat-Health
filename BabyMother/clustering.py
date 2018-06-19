from sklearn.cluster import Birch
from sklearn.cluster import KMeans
import pandas as pd

data=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.11.csv')
X=[]
for i in range (len(data)):
    x=[]
    x.append(data.iloc[i]['平均得分'])
    x.append(data.iloc[i]['减重值'])
    #x.append(data.iloc[i]['初始体重值'])
    #x.append(data.iloc[i]['BMI'])
    #x.append(data.iloc[i]['年龄'])
    X.append(x)

# Kmeans聚类
clf = KMeans(n_clusters=5)
y_pred = clf.fit_predict(X)
print(clf)
print(y_pred)

import numpy as np
import matplotlib.pyplot as plt

x = [n[0] for n in X]
y = [n[1] for n in X]
# 可视化操作
plt.scatter(x, y, c=y_pred, marker='o')
plt.title("Kmeans-Babymother Data")
plt.xlabel("score")
plt.ylabel("reduced weight")
plt.legend(["user"])
plt.show()
data['聚类标签']=y_pred
data.to_excel('/Users/martin_yan/Desktop/clustering5.22-6.11111.xlsx',index=False, encoding="utf_8_sig")