import pandas as pd
import numpy as np
encoding='UTF-8'


"""
data=pd.read_csv('data/用户初始体重表.csv')
find=pd.read_csv('/Users/martin_yan/Desktop/heightandweight.csv')
#删除早于2018／5／22的体重数据
data=data[data['日期']> '2018/5/21 0:00']
#打印满足条件的用户初始体重表里的人数
print(len(data['uid'].unique()))
data.drop_duplicates('uid','first',inplace=True)
#对数据重新index编号
data=data.reset_index(drop=True)
data = pd.merge(find, data, how='left', on='姓名')
bmi=[]
reduce=[]
for i in range(len(data)):
    height=data.iloc[i]['身高']
    weight=data.iloc[i]['体重']
    bmi.append(weight/pow(height/100,2))
    reduce.append(data.iloc[i]['体重']-data.iloc[i]['当前体重'])

data['BMI']=bmi
data['减重值']=reduce
data.drop(['日期','uid'], inplace=True, axis=1)
print(data)
data.to_csv('/Users/martin_yan/Desktop/addBMI.csv', index=False, encoding="utf_8_sig")


#一元多项式拟合
#encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('/Users/martin_yan/Desktop/new_babymother_completedata.csv')
list=['蔬菜摄入量平均分','减重值']
x=[]
y=[]
for i in range(len(data)):
    x.append(data.iloc[i][list[0]])
    y.append(data.iloc[i][list[1]])


#用3次多项式拟合
f1 = np.polyfit(x, y, 10)
p1 = np.poly1d(f1)
print(p1)

#也可使用yvals=np.polyval(f1, x)
yvals = p1(x)  #拟合y值

#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('polyfitting')
plt.show()


from sklearn.preprocessing import PolynomialFeatures
X = np.arange(9).reshape(3, 3)
print(X)
poly = PolynomialFeatures(2)
X_ploly = poly.fit_transform(X)
#设置多项式阶数为２，其他的默认
X_ploly_df = pd.DataFrame(X_ploly, columns=poly.get_feature_names())
print(X_ploly_df.head())

poly = PolynomialFeatures(interaction_only=True)
#默认的阶数是２，同时设置交互关系为true
poly.fit_transform(X)

#增加年龄属性
find=pd.read_csv('/Users/martin_yan/Desktop/宝妈营用户生日.csv',usecols=['uid','年龄'])
#修改列名(任意个数)
find.rename(columns={'uid':'用户编号'}, inplace = True)
data=pd.read_csv('/Users/martin_yan/Desktop/babymother_completedata5.22-6.4.csv')
data = pd.merge(data, find, on='用户编号')
data.to_csv('/Users/martin_yan/Desktop/babymother_completedata5.22-6.41.csv',index=False, encoding="utf_8_sig")
"""