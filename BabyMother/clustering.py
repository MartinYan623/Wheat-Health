from sklearn.cluster import KMeans,DBSCAN
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.25(总表／入营平均分).csv')
X=[]
for i in range (len(data)):
    x=[]
    x.append(data.iloc[i]['平均得分'])
    x.append(data.iloc[i]['减重值'])
    #x.append(data.iloc[i]['总热量实际摄入平均量'])
    #x.append(data.iloc[i]['完整记录天数'])
    #x.append(data.iloc[i]['BMI'])
    #x.append(data.iloc[i]['年龄'])
    X.append(x)

#公式为：(X-mean)/std  计算时对每个属性/每列分别进行
#将数据按期属性（按列进行）减去其均值，并处以其标准差。得到的结果是，对于每个属性/每列来说所有数据都聚集在0附近，标准差为1
Y = np.array(X)
Y_scaled = preprocessing.scale(Y)

print(Y_scaled)
# Kmeans聚类
clf = KMeans(n_clusters=3)
# DBscan聚类 检测异常点
# 默认eps=0.5 min_samples=5
clf=DBSCAN(eps=0.6,metric='euclidean',algorithm='auto')

y_pred = clf.fit_predict(Y_scaled)
print(clf)
print(y_pred)

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
#data.to_excel('/Users/martin_yan/Desktop/clustering5.22-6.11(3).xlsx',index=False, encoding="utf_8_sig")
