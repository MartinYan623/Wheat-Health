import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D
encoding='UTF-8'
plt.rcParams['font.sans-serif']=[u'SimHei']
plt.rcParams['axes.unicode_minus']=False
data = pd.read_csv('/Users/martin_yan/Desktop/completeday_score.csv')
#data=data[data['记录天数']>3]
data.drop(['用户编号'], inplace=True, axis=1)
print(data)
"""
#一元线性回归求相关性
for i in range(len(data)):
    data.loc[i,'水果摄入量平均分']=data.iloc[i]['水果摄入量平均分'] / 130
    data.loc[i, '蔬菜摄入量平均分'] = data.iloc[i]['蔬菜摄入量平均分'] / 130
    data.loc[i, '全谷类摄入量平均分'] = data.iloc[i]['全谷类摄入量平均分'] / 130
    data.loc[i, '精制谷物摄入量平均分'] = data.iloc[i]['精制谷物摄入量平均分'] / 130
    data.loc[i, '膳食纤维摄入量平均分'] = data.iloc[i]['膳食纤维摄入量平均分'] / 130
    data.loc[i, '乳类摄入量平均分'] = data.iloc[i]['乳类摄入量平均分'] / 130
    data.loc[i, '总蛋白摄入量平均分'] = data.iloc[i]['总蛋白摄入量平均分'] / 130
    data.loc[i, '鱼虾贝壳类及植物蛋白类摄入量平均分'] = data.iloc[i]['鱼虾贝壳类及植物蛋白类摄入量平均分'] / 130
    data.loc[i, '不饱和与饱和脂肪酸摄入比平均分'] = data.iloc[i]['不饱和与饱和脂肪酸摄入比平均分'] / 130
    data.loc[i, '固态脂肪摄入量平均分'] = data.iloc[i]['固态脂肪摄入量平均分'] / 130
    data.loc[i, '钠盐摄入量平均分'] = data.iloc[i]['钠盐摄入量平均分'] / 130
    data.loc[i, '添加糖摄入量平均分'] = data.iloc[i]['添加糖摄入量平均分'] / 130
    data.loc[i, '总热量摄入量平均分'] = data.iloc[i]['总热量摄入量平均分'] / 130
    data.loc[i, '三大营养素组成平均分'] = data.iloc[i]['三大营养素组成平均分'] / 130
    data.loc[i, '饮酒（酒精量，全天标准）平均分'] = data.iloc[i]['饮酒（酒精量，全天标准）平均分'] / 130
    data.loc[i, '饮水量平均分'] = data.iloc[i]['饮水量平均分'] / 130
"""
numeric_features = data.select_dtypes(include=[np.number])
# 默认为pearson相关系数,另外选择method=spearman表示spearman相关系数等级皮尔逊相关系数，而method=kendall表示另外一种秩相关系数
corr = numeric_features.corr()
print (corr['减重值'].sort_values(ascending=False), '\n')
#print (corr['减重百分比'].sort_values(ascending=False), '\n')
#print (corr['蔬菜摄入量平均分'].sort_values(ascending=False), '\n')
#print (corr['膳食纤维摄入量平均分'].sort_values(ascending=False), '\n')
#print (corr['平均得分'].sort_values(ascending=False), '\n')
#print (corr['初始体重值'].sort_values(ascending=False), '\n')
#print (corr['BMI'].sort_values(ascending=False), '\n')
#print (corr['固态脂肪摄入量平均分'].sort_values(ascending=False), '\n')
#print (corr['全谷类实际摄入平均量'].sort_values(ascending=False), '\n')
#print (corr['不饱和与饱和脂肪酸实际摄入平均量'].sort_values(ascending=False), '\n')
#设置热图大小
plt.figure(1,figsize=(12,8))
#设置热图标题
plt.title(u'各属性之间的相关性分析')
#coorelation相关性
corr = data.corr()
#绘制热图
sns.heatmap(corr)
#plt.show()


#多元线性回归分析及画图
list=['蔬菜摄入量平均分','全谷类摄入量平均分','减重值']
xx=[]
yy=[]
zz=[]
for i in range(len(data)):
    xx.append(data.iloc[i][list[0]])
    yy.append(data.iloc[i][list[1]])
    zz.append(data.iloc[i][list[-1]])
# 构建成特征、值的形式
X, Z = np.column_stack((xx,yy)), zz
# 建立线性回归模型
regr = linear_model.LinearRegression()
# 拟合
regr.fit(X, Z)
# 得到平面的系数、截距
a, b = regr.coef_, regr.intercept_
print('coefficients(b1,b2...):',a)
print('intercept(b0):',b)
# 画图
fig = plt.figure()
ax = fig.gca(projection='3d')
# 1.画出真实的点
ax.scatter(xx, yy, zz)
# 2.画出拟合的平面
ax.plot_wireframe(xx, yy, regr.predict(X).reshape(1,81))
ax.plot_surface(xx, yy, regr.predict(X).reshape(1,81), alpha=0.3)
plt.show()
