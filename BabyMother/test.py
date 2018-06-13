import pandas as pd
import numpy as np
encoding='UTF-8'


"""
data=pd.read_csv('data/宝妈用户初始体重表.csv')
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

#将以前的用户初始体重表中提取出每个用户5.22以后第一天的体重值，重复输入取最后一次记录为准
data=pd.read_csv('../data/宝妈用户初始体重表.csv')
data = data.drop_duplicates(['uid','日期'],keep='last')
data=data[data['日期']> '2018/5/21 0:00']
data=data.reset_index(drop=True)
date=data.duplicated(['uid'],keep='first')
print(data)
uid=[]
name=[]
weight=[]
time=[]
for i in range(len(data)):
    if date[i] == False:
        uid.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        weight.append(data.iloc[i]['体重'])
        time.append(data.iloc[i]['日期'])
dataframe=pd.DataFrame({'用户编号':uid,'姓名':name,'初始体重值':weight,'日期':time})
columns = ['用户编号', '姓名', '初始体重值','日期']
#dataframe.to_csv('/Users/martin_yan/Desktop/宝妈用户初始体重表.csv',index=False, encoding="utf_8_sig",columns=columns)

#将目前宝妈营用户初始体重全部输出
data=pd.read_csv('../data/宝妈用户每日体重变化5.22-6.4.csv')
data = data.drop_duplicates(['uid','日期'],keep='first')
data=data.reset_index(drop=True)
date=data.duplicated(['uid'],keep='first')
uid=[]
name=[]
weight=[]
time=[]
for i in range(len(data)):
    if date[i] == False:
        uid.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        weight.append(data.iloc[i]['体重'])
        time.append(data.iloc[i]['日期'])
dataframe=pd.DataFrame({'用户编号':uid,'姓名':name,'初始体重值':weight,'日期':time})
columns = ['用户编号', '姓名', '初始体重值','日期']

data2=pd.read_csv('/Users/martin_yan/Desktop/宝妈用户初始体重表.csv')
data=dataframe.append(data2)
print(data)
data=data.drop_duplicates(['用户编号'],keep='first')
data=data.sort_values('用户编号')
data=data.reset_index(drop=True)
print(data)
data.to_csv('/Users/martin_yan/Desktop/用户初始体重表222.csv',index=False, encoding="utf_8_sig",columns=columns)


data=pd.read_csv('../data/heightandweight.csv',usecols=['用户编号','身高'])
data2=pd.read_csv('../data/宝妈用户初始体重表.csv')
data = pd.merge(data2, data, how='left', on='用户编号')
bmi=[]
for i in range(len(data)):
    height = data.iloc[i]['身高']
    weight = data.iloc[i]['初始体重值']
    bmi.append(weight / pow(height / 100, 2))
data['BMI']=bmi
print(data)
columns = ['用户编号', '姓名', '初始体重值','日期','身高','BMI']
data.to_csv('/Users/martin_yan/Desktop/宝妈用户初始信息表.csv',index=False, encoding="utf_8_sig",columns=columns)




data=pd.read_csv('../data/new_宝妈营数据5.22-5.29.csv')
data2=pd.read_csv('../data/new_宝妈营数据5.30-6.4.csv')
data=data[data['记录日期']=='2018/5/29 0:00']
data=data.append(data2)
columns = ['uid','营id','真实姓名','手机号','pb','pb得分','rf','rf得分','rf满分参考','摄入值','对比值','满分参考区间','记录日期']
data.to_csv('/Users/martin_yan/Desktop/new_宝妈营数据5.29-6.4.csv',index=False, encoding="utf_8_sig",columns=columns)

data=pd.read_csv('../data/宝妈用户每日体重变化5.22-6.4.csv')
data2=pd.read_csv('/Users/martin_yan/Desktop/1.csv')
#修改列名(任意个数)
data2.rename(columns={'记录日期':'日期'}, inplace = True)
data=data.append(data2)
data = data.drop_duplicates(['uid','日期'],keep='last')
print(data)
data.to_csv('/Users/martin_yan/Desktop/宝妈用户每日体重变化5.22-6.11.csv',index=False, encoding="utf_8_sig")


data=pd.read_csv('../data/宝妈用户每日体重变化5.22-6.11.csv')
#data2=pd.read_csv('../data/宝妈用户初始信息表.csv',usecols=['姓名','初始体重值'])
#data3=pd.read_csv('/Users/martin_yan/Desktop/babymother_data5.22-5.28.csv')
#data=data[data['日期']>'2018/5/28 0:00']
#data = pd.merge(data, data2, on='姓名')
username1=data.duplicated('uid',keep='first')
username2=data.duplicated('uid',keep='last')
print(data)
id=[]
name=[]
reduce=[]
for i in range(len(data)):
    if username1[i]==False:
        original=data.iloc[i]['体重']
    if username2[i]==False:
        id.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        #reduce.append(data.iloc[i]['初始体重值']-data.iloc[i]['体重'])
        reduce.append(original - data.iloc[i]['体重'])
        original=0
dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'减重值':reduce})
columns = ['用户编号','姓名','减重值']
dataframe.to_csv('/Users/martin_yan/Desktop/宝妈用户减重表5.22-6.11(全部).csv',index=False, encoding="utf_8_sig",columns=columns)


#体重减重值是从入营第一周到目前周
data=pd.read_csv('../data/宝妈用户每日体重变化5.22-6.11.csv')
data2=pd.read_csv('../data/宝妈用户初始信息表.csv',usecols=['姓名','初始体重值','日期'])
data=data[data['日期']>'2018/6/4 0:00']
data2=data2[data2['日期']<'2018/5/29 0:00']

data = pd.merge(data, data2, on='姓名')
data = data.drop_duplicates(['uid','日期'],keep='last')
data=data.reset_index(drop=True)
username=data.duplicated('uid',keep='last')
print(data)
id=[]
name=[]
reduce=[]
for i in range(len(data)):
    if username[i] == False:
        id.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        reduce.append(data.iloc[i]['初始体重值']-data.iloc[i]['体重'])
dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'减重值':reduce})
columns = ['用户编号','姓名','减重值']
dataframe.to_csv('/Users/martin_yan/Desktop/宝妈用户减重表5.22-6.11(全部).csv',index=False, encoding="utf_8_sig",columns=columns)
"""

data=pd.read_csv('/Users/martin_yan/Desktop/HEI_mean_babymother_data5.22-6.11（21天平均分）.csv')
data2=pd.read_csv('../data/宝妈用户减重表5.22-6.11.csv',usecols=['姓名'])
data = pd.merge(data, data2, on='姓名')
print(data)
data.to_csv('/Users/martin_yan/Desktop/HEI_mean_babymother_data5.22-6.1111.csv',index=False, encoding="utf_8_sig")