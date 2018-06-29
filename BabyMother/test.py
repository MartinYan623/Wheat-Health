import pandas as pd
import numpy as np
import datetime
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



data=pd.read_csv('/Users/martin_yan/Desktop/HEI_mean_babymother_data5.22-6.11（21天平均分）.csv')
data2=pd.read_csv('../data/宝妈用户减重表5.22-6.11.csv',usecols=['姓名'])
data = pd.merge(data, data2, on='姓名')
print(data)
data.to_csv('/Users/martin_yan/Desktop/HEI_mean_babymother_data5.22-6.1111.csv',index=False, encoding="utf_8_sig")


data=pd.read_csv('/Users/martin_yan/Desktop/累积.csv')
data2=pd.read_csv('/Users/martin_yan/Desktop/单周减重值.csv',usecols=[1,3,5,7])
data = pd.merge(data, data2, on='姓名')
columns=['用户编号','姓名','第一周减重值','第一周累计减重值','第二周减重值','第二周累计减重值','第三周减重值','第三周累计减重值']
data.to_csv('/Users/martin_yan/Desktop/1111.csv',index=False, encoding="utf_8_sig",columns=columns)
print(data)



#体重减重值是从入营第一周到目前周
data=pd.read_csv('../data/宝妈用户每日体重变化5.22-6.25.csv')
data2=pd.read_csv('../data/宝妈用户初始信息表.csv',usecols=['姓名','初始体重值','日期'])
data=data[data['日期']>'2018/6/18 0:00']
data=data[data['日期']<'2018/6/26 0:00']
data=data[(True-data['日期'].isin(['2018/6/2 0:00']))]
data2=data2[data2['日期']<'2018/5/29 0:00']

data = pd.merge(data, data2, on='姓名')
data = data.drop_duplicates(['uid','日期'],keep='last')
data=data.reset_index(drop=True)
username=data.duplicated('uid',keep='last')
print(data)
id=[]
name=[]
reduce=[]
time=[]
for i in range(len(data)):
    if username[i] == False:
        id.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        reduce.append(data.iloc[i]['初始体重值']-data.iloc[i]['体重'])
        time.append(data.iloc[i]['日期_x'])
dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'减重值':reduce,'最后记录体重日期':time})
columns = ['用户编号','姓名','减重值','最后记录体重日期']
dataframe.to_csv('/Users/martin_yan/Desktop/宝妈用户减重表5.22-6.25.csv',index=False, encoding="utf_8_sig",columns=columns)



data=pd.read_csv('/Users/martin_yan/Desktop/11.csv')
data = data.drop_duplicates(['uid','记录日期', 'rf'])
data.to_csv('/Users/martin_yan/Desktop/22.csv',index=False, encoding="utf_8_sig")



data=pd.read_csv('/Users/martin_yan/Desktop/333.csv')
data2=pd.read_csv('../data/宝妈用户初始信息表.csv',usecols=['用户编号','初始体重值','日期','BMI'])
data = pd.merge(data, data2, on='用户编号')
print(data)
id=[]
name=[]
reduce=[]
time=[]
bmi=[]
for i in range(len(data)):
    id.append(data.iloc[i]['用户编号'])
    name.append(data.iloc[i]['姓名'])
    reduce.append(data.iloc[i]['初始体重值']-data.iloc[i]['最后体重'])
    time.append(data.iloc[i]['记录日期'])
    bmi.append(data.iloc[i]['BMI'])
dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'BMI':bmi,'减重值':reduce,'最后记录体重日期':time})
columns = ['用户编号','姓名','BMI','减重值','最后记录体重日期']
dataframe.to_csv('/Users/martin_yan/Desktop/宝妈用户减重表5.22-6.25(全部).csv',index=False, encoding="utf_8_sig",columns=columns)


data=pd.read_csv('/Users/martin_yan/Desktop/饮食完整记录未达到24天以上 5.22-6.25.csv')
username=data.duplicated('姓名',keep='last')
name=[]
group=[]
date=[]
reduce=[]
for i in range(len(data)):
    if username[i]==False:
        name.append(data.iloc[i]['姓名'])
        group.append(data.iloc[i]['组别'])
        date.append(data.iloc[i]['减肥时间段'])
        reduce.append(data.iloc[i]['减重值'])
dataframe=pd.DataFrame({'姓名':name,'组别':group,'减肥时间段':date,'减重值':reduce})
columns=['姓名','组别','减肥时间段','减重值']
dataframe.to_excel('/Users/martin_yan/Desktop/饮食完整记录未达到24天以上 5.22-6.25.xlsx',index=False, encoding="utf_8_sig",columns=columns)



data=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.25(体重跨度5周／实际记录平均分).csv',usecols=['用户编号','姓名','年龄','BMI','减重值'])
id=[]
name=[]
reduce=[]
group=[]
for i in range(len(data)):
    if data.iloc[i]['BMI']>24 and data.iloc[i]['年龄']>36:
        id.append(data.iloc[i]['用户编号'])
        name.append(data.iloc[i]['姓名'])
        reduce.append(data.iloc[i]['减重值'])
        group.append('A组 BMI>24 and 年龄>36岁')
    if data.iloc[i]['BMI']>24 and data.iloc[i]['年龄']<37:
        id.append(data.iloc[i]['用户编号'])
        name.append(data.iloc[i]['姓名'])
        reduce.append(data.iloc[i]['减重值'])
        group.append('B组 BMI>24 and 年龄<=36岁')
    if data.iloc[i]['BMI']<24.01 and data.iloc[i]['年龄']>36:
        id.append(data.iloc[i]['用户编号'])
        name.append(data.iloc[i]['姓名'])
        reduce.append(data.iloc[i]['减重值'])
        group.append('C组 BMI<=24 and 年龄>36岁')
    if data.iloc[i]['BMI']<24.01 and data.iloc[i]['年龄']<37:
        id.append(data.iloc[i]['用户编号'])
        name.append(data.iloc[i]['姓名'])
        reduce.append(data.iloc[i]['减重值'])
        group.append('D组 BMI<=24 and 年龄<=36岁')

dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'组别':group,'减重值':reduce})
columns=['用户编号','姓名','组别','减重值']
dataframe.to_excel('/Users/martin_yan/Desktop/用户BMI年龄分组.xlsx',index=False, encoding="utf_8_sig",columns=columns)


# 根据用户的减重值划分组，求每组的轻食日和普通日的热量平均对比值
data=pd.read_csv('/Users/martin_yan/Desktop/精选用户数据3.csv',usecols=['用户编号','姓名','轻食日热量平均对比值','普通日热量平均对比值','减重值'])
count1=0
count2=0
count3=0
count4=0
count5=0
lightnum1=0
normalnum1=0
lightnum2=0
normalnum2=0
lightnum3=0
normalnum3=0
lightnum4=0
normalnum4=0
lightnum5=0
normalnum5=0
for i in range (len(data)):
    if data.iloc[i]['减重值']<1:
        count1=count1+1
        lightnum1 = lightnum1+data.iloc[i]['轻食日热量平均对比值']
        normalnum1 = normalnum1 + data.iloc[i]['普通日热量平均对比值']
    if data.iloc[i]['减重值']>0.99 and data.iloc[i]['减重值']<2:
        count2=count2+1
        lightnum2 = lightnum2 + data.iloc[i]['轻食日热量平均对比值']
        normalnum2 = normalnum2 + data.iloc[i]['普通日热量平均对比值']
    if data.iloc[i]['减重值']>1.99 and data.iloc[i]['减重值']<3:
        count3=count3+1
        lightnum3 = lightnum3 + data.iloc[i]['轻食日热量平均对比值']
        normalnum3 = normalnum3 + data.iloc[i]['普通日热量平均对比值']
    if data.iloc[i]['减重值']>2.99 and data.iloc[i]['减重值']<4:
        count4=count4+1
        lightnum4 = lightnum4 + data.iloc[i]['轻食日热量平均对比值']
        normalnum4 = normalnum4 + data.iloc[i]['普通日热量平均对比值']
    if data.iloc[i]['减重值']>3.99:
        count5=count5+1
        lightnum5 = lightnum5 + data.iloc[i]['轻食日热量平均对比值']
        normalnum5 = normalnum5 + data.iloc[i]['普通日热量平均对比值']

lightnum1=lightnum1/count1
lightnum2=lightnum2/count2
lightnum3=lightnum3/count3
lightnum4=lightnum4/count4
lightnum5=lightnum5/count5
normalnum1=normalnum1/count1
normalnum2=normalnum2/count2
normalnum3=normalnum3/count3
normalnum4=normalnum4/count4
normalnum5=normalnum5/count5
print('人数:'+ str(count1)+',轻食日平均对比值:'+str(lightnum1)+',普通日平均对比值:'+str(normalnum1))
print('人数:'+ str(count2)+',轻食日平均对比值:'+str(lightnum2)+',普通日平均对比值:'+str(normalnum2))
print('人数:'+ str(count3)+',轻食日平均对比值:'+str(lightnum3)+',普通日平均对比值:'+str(normalnum3))
print('人数:'+ str(count4)+',轻食日平均对比值:'+str(lightnum4)+',普通日平均对比值:'+str(normalnum4))
print('人数:'+ str(count5)+',轻食日平均对比值:'+str(lightnum5)+',普通日平均对比值:'+str(normalnum5))
"""

data=pd.read_csv('/Users/martin_yan/Desktop/每日热量统计.csv',usecols=[0,1,3,5,6])
data = data.drop_duplicates(['uid','记录日期'])
light=pd.read_csv('../data/轻食日统计.csv')
data = pd.merge(data, light, on='姓名')
print(len(data['姓名'].unique()))
lightday=[]

# 判断某天是否为用户的轻食日
for i in range(len(data)):
    month=data.iloc[i]['记录日期'].split('/')[1]
    day=data.iloc[i]['记录日期'].split('/')[2].split(' ')[0]
    light1=data.iloc[i]['轻食日1']
    light2=data.iloc[i]['轻食日2']
    anyday=datetime.datetime(2018,int(month),int(day)).strftime("%w")
    if int(light1)==int(anyday) or int(light2)==int(anyday):
        lightday.append(1)
    else:
        lightday.append(0)

data['是否为轻食日']=lightday
first=data.duplicated('姓名',keep='first')
last=data.duplicated('姓名',keep='last')
print(data)

score=0
countlight=0
lightscore1=[]
lightscore2=[]
name=[]
id=[]
for i in range(len(data)):
    number = data.iloc[i]['对比值']
    if data.iloc[i]['是否为轻食日'] == 1:
        countlight = countlight + 1
        if number>74 and number<126:
            score=score+10
        if number < 74 and number > 65.99 and number>126 and number<134.01:
            score = score + 5
    if last[i]==False:
        id.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        if countlight==0:
            lightscore1.append(0)
        else:
            lightscore1.append(score/countlight)
        lightscore2.append(score / 10)
        score=0
        countlight=0

meanheat=pd.DataFrame({'用户编号':id,'姓名':name,'轻食日热量平均分(实际记录天数)':lightscore1,'轻食日热量平均分(入营天数)':lightscore2})
mean=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.25(总表／实际记录平均分).csv',usecols=['姓名','减重值'])
data = pd.merge(mean, meanheat, on='姓名')
data.to_csv('/Users/martin_yan/Desktop/21312321.csv', index=False, encoding="utf_8_sig")