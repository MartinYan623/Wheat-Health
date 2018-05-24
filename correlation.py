import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D
encoding='UTF-8'
plt.rcParams['font.sans-serif']=[u'SimHei']
plt.rcParams['axes.unicode_minus']=False
data = pd.read_csv('/Users/martin_yan/Desktop/mean_data.csv')
data.drop(['用户编号', '记录天数'], inplace=True, axis=1)
#一元线性回归求相关性

numeric_features = data.select_dtypes(include=[np.number])
# 默认为pearson相关系数,另外选择method=spearman表示spearman相关系数等级皮尔逊相关系数，而method=kendall表示另外一种秩相关系数
corr = numeric_features.corr()
print (corr['减重值'].sort_values(ascending=False), '\n')
print (corr['减重百分比'].sort_values(ascending=False), '\n')
print (corr['BMI'].sort_values(ascending=False), '\n')
print (corr['年龄'].sort_values(ascending=False), '\n')
#设置热图大小
plt.figure(1,figsize=(12,8))
#设置热图标题
plt.title(u'各属性之间的相关性分析')
#coorelation相关性
corr = data.corr()
#绘制热图
sns.heatmap(corr)
#绘制一元回归线图
sns.pairplot(data, x_vars=['钠盐实际摄入平均量','蔬菜实际摄入平均量','水果实际摄入平均量'], y_vars='减重值', size=7, aspect=0.8,kind='reg')
plt.show()


#多元线性回归分析及画图
list=['钠盐实际摄入平均量','蔬菜实际摄入平均量','减重值']
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
# 不难得到平面的系数、截距
a, b = regr.coef_, regr.intercept_
print('coefficients(b1,b2...):',a)
print('intercept(b0):',b)
# 画图
fig = plt.figure()
ax = fig.gca(projection='3d')
# 1.画出真实的点
ax.scatter(xx, yy, zz)
# 2.画出拟合的平面
ax.plot_wireframe(xx, yy, regr.predict(X).reshape(1,12))
ax.plot_surface(xx, yy, regr.predict(X).reshape(1,12), alpha=0.3)
plt.show()