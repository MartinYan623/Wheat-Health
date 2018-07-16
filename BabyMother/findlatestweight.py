import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
encoding='UTF-8'

"""
data=pd.read_csv('../data/宝妈用户每日体重变化5.22-6.25.csv')
data2=pd.read_csv('../data/宝妈用户初始信息表.csv',usecols=['姓名','BMI'])
data = pd.merge(data, data2, on='姓名')
data = data.drop_duplicates(['uid','日期'],keep='last')
data=data.reset_index(drop=True)
#data=data[data['日期']>'2018/5/28 0:00']
#data=data[data['日期']< '2018/6/5 0:00']
#data=data[(True-data['日期'].isin(['2018/6/10 0:00','2018/6/11 0:00','2018/6/12 0:00','2018/6/13 0:00','2018/6/14 0:00','2018/6/15 0:00','2018/6/16 0:00','2018/6/17 0:00','2018/6/18 0:00']))]
#data=data[(True-data['日期'].isin(['2018/6/12 0:00','2018/6/13 0:00','2018/6/14 0:00','2018/6/15 0:00','2018/6/16 0:00','2018/6/17 0:00','2018/6/18 0:00']))]
fre=data.groupby('uid').count()['姓名'].to_dict()
a,b = list(fre.keys()) , list(fre.values())
fre = pd.DataFrame({'uid':a,'实际记录天数':b})
#fre_series=data['用户编号'].value_counts()
#fre = fre_series.to_frame('实际记录天数')
data = pd.merge(fre, data, how='left', on='uid')
data=data[data['实际记录天数']>27]
print(len(data['uid'].unique()))
data=data.reset_index(drop=True)
first=data.duplicated(['姓名'],keep='first')
last=data.duplicated(['姓名'],keep='last')
reduce=[]
id=[]
name=[]
day=[]
BMI=[]
for i in range(len(data)):
    if first[i]==False:
        original=data.iloc[i]['体重']
    if last[i]==False:
        id.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        day.append(data.iloc[i]['实际记录天数'])
        reduce.append(original-data.iloc[i]['体重'])
        if data.iloc[i]['BMI']>24:
            BMI.append('A组(BMI>24)')
        else:
            BMI.append('B组(BMI<=24)')
dataframe=pd.DataFrame({'用户编号':id,'姓名':name,'实际记录天数':day,'减重值':reduce,'BMI':BMI})
columns=['用户编号','姓名','实际记录天数','减重值','BMI']
print(dataframe)
dataframe.to_csv('/Users/martin_yan/Desktop/累积第五周减重值情况.csv', index=False, encoding="utf_8_sig",columns=columns)
"""
weight=0
meanweight=[]
best=0
parameter=0
bmi=0
meanbmi=[]
count=[]
oneweight=[]
onebmi=[]
data=pd.read_csv('/Users/martin_yan/Desktop/bmi减重百分比去异常点数据.csv')
data=data.sort_values(['减重值'])
print(data)
for i in range (len(data)):
    weight=weight+data.iloc[i]['减重值']
    bmi=bmi+data.iloc[i]['BMI']
    oneweight.append(data.iloc[i]['减重值'])
    onebmi.append(data.iloc[i]['BMI'])
    meanweight.append(weight/(i+1))
    meanbmi.append(round(bmi/(i+1), 2))

    count.append(i+1)

dataframe=pd.DataFrame({'平均减重值':meanweight,'平均BMI':meanbmi,'人数':count})
print(dataframe)
plt.rcParams['font.sans-serif']=[u'SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.title('BMI随减重值的变化图')
plt.xlabel('减重值(KG)')
plt.ylabel('BMI')


# 平均BMI随减重值的变化图
plt.plot(meanweight, meanbmi, 'r', label='broadcast')
count=0
for a, b in zip(meanweight, meanbmi):
    if count%3==0:
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    count=count+1
plt.show()

"""
# 非平均BMI随减重值的变化图
plt.plot(oneweight, onebmi, 'r', label='broadcast')
count=0
for a, b in zip(oneweight, onebmi):
    if count%10==0:
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    count=count+1
plt.show()


data=pd.read_csv('/Users/martin_yan/Desktop/bmi减重百分比去异常点数据.csv')
meanweight=[]
bmi=[]
number=[]
for a in range(210,240,4):
    a=a*0.1
    weight=0
    count=0
    for i in range(len(data)):
        if data.iloc[i]['BMI']>a:
            count=count+1
            weight=weight+data.iloc[i]['减重值']
    bmi.append(a)
    meanweight.append(weight/count)
    number.append(count)

dataframe=pd.DataFrame({'平均减重值':meanweight,'平均BMI':bmi,'计算人数':number})
print(dataframe)
"""