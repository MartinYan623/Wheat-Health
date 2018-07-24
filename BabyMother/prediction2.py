import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
encoding='UTF-8'
data0=pd.read_csv('/Users/martin_yan/Desktop/宝妈营用户单周减重及BMI变化.csv')
data1=pd.read_csv('/Users/martin_yan/Desktop/第一周饮食得分.csv')
data2=pd.read_csv('/Users/martin_yan/Desktop/第二周饮食得分.csv')
data3=pd.read_csv('/Users/martin_yan/Desktop/第三周饮食得分.csv')
data4=pd.read_csv('/Users/martin_yan/Desktop/第四周饮食得分.csv')
data5=pd.read_csv('/Users/martin_yan/Desktop/第五周饮食得分.csv')


#获取一个list的中位数
def get_median(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2

#获取一个list的平均值
def get_average(data):
    avg = 0.0
    n = len(data)
    for num in data:
        avg+= 1.0*num/n
    return avg

weight=[]
bmi=[]
# 获取用户的初始信息
weight.append(float(input("请输入您的初始体重(KG)")))
print(weight[0])
height=float(input("请输入您的身高(CM)"))
print(height)
bmi.append(int(weight[0])/pow(int(height)/100,2))
print(bmi[0])

#第一周
id=[]
weight2=[]
if bmi[0]<24:
    for i in range(len(data0)):
        if data0.iloc[i]['初始BMI']<24:
            id.append(data0.iloc[i]['uid'])
            weight2.append(data0.iloc[i]['第一周减重值'])
else:
    if bmi[0]>28:
        for i in range(len(data0)):
            if data0.iloc[i]['初始BMI']>28:
                id.append(data0.iloc[i]['uid'])
                weight2.append(data0.iloc[i]['第一周减重值'])

    else:
        for i in range(len(data0)):
            if data0.iloc[i]['初始BMI']>24 and data0.iloc[i]['初始BMI']<28:
                id.append(data0.iloc[i]['uid'])
                weight2.append(data0.iloc[i]['第一周减重值'])

dataframe=pd.DataFrame({'用户编号':id,'减重值':weight2})
data = pd.merge(data1, dataframe, on='用户编号')
data=data[data['新饮食得分(100制)']>70]
reduced_weight= np.array(data['减重值']) #np.ndarray()
reduced_weight_list=reduced_weight.tolist() #list
medianreduced=round(get_median(reduced_weight_list),2)
meanreduced=round(get_average(reduced_weight_list),2)
print(reduced_weight_list)
weight.append(round(weight[0]-meanreduced,2))
bmi.append(float(weight[1]/pow(height/100,2)))
print(weight)
print(bmi)


#第二周
id=[]
weight2=[]
if bmi[1]<24:
    for i in range(len(data0)):
        if data0.iloc[i]['初始BMI']<24:
            id.append(data0.iloc[i]['uid'])
            weight2.append(data0.iloc[i]['第二周减重值'])
else:
    if bmi[1]>28:
        for i in range(len(data0)):
            if data0.iloc[i]['初始BMI']>28:
                id.append(data0.iloc[i]['uid'])
                weight2.append(data0.iloc[i]['第二周减重值'])

    else:
        for i in range(len(data0)):
            if data0.iloc[i]['初始BMI']>24 and data0.iloc[i]['初始BMI']<28:
                id.append(data0.iloc[i]['uid'])
                weight2.append(data0.iloc[i]['第二周减重值'])

dataframe=pd.DataFrame({'用户编号':id,'减重值':weight2})
data = pd.merge(data2, dataframe, on='用户编号')
data=data[data['新饮食得分(100制)']>70]
reduced_weight= np.array(data['减重值']) #np.ndarray()
reduced_weight_list=reduced_weight.tolist() #list
print(reduced_weight_list)
medianreduced=round(get_median(reduced_weight_list),2)
meanreduced=round(get_average(reduced_weight_list),2)
weight.append(round(weight[1]-meanreduced,2))
print(weight[2])
bmi.append(float(weight[2]/pow(height/100,2)))
print(weight)
print(bmi)


#第三周
id=[]
weight2=[]
if bmi[2]<24:
    for i in range(len(data0)):
        if data0.iloc[i]['初始BMI']<24:
            id.append(data0.iloc[i]['uid'])
            weight2.append(data0.iloc[i]['第三周减重值'])
else:
    if bmi[2]>28:
        for i in range(len(data0)):
            if data0.iloc[i]['初始BMI']>28:
                id.append(data0.iloc[i]['uid'])
                weight2.append(data0.iloc[i]['第三周减重值'])

    else:
        for i in range(len(data0)):
            if data0.iloc[i]['初始BMI']>24 and data0.iloc[i]['初始BMI']<28:
                id.append(data0.iloc[i]['uid'])
                weight2.append(data0.iloc[i]['第三周减重值'])

dataframe=pd.DataFrame({'用户编号':id,'减重值':weight2})
data = pd.merge(data3, dataframe, on='用户编号')
data=data[data['新饮食得分(100制)']>70]
reduced_weight= np.array(data['减重值']) #np.ndarray()
reduced_weight_list=reduced_weight.tolist() #list
print(reduced_weight_list)
medianreduced=round(get_median(reduced_weight_list),2)
meanreduced=round(get_average(reduced_weight_list),2)
weight.append(round(weight[2]-meanreduced,2))
print(weight[3])
bmi.append(float(weight[3]/pow(height/100,2)))
print(weight)
print(bmi)

#第四周
id=[]
weight2=[]
if bmi[3]<24:
    for i in range(len(data0)):
        if data0.iloc[i]['初始BMI']<24:
            id.append(data0.iloc[i]['uid'])
            weight2.append(data0.iloc[i]['第三周减重值'])
else:
    if bmi[3]>28:
        for i in range(len(data0)):
            if data0.iloc[i]['初始BMI']>28:
                id.append(data0.iloc[i]['uid'])
                weight2.append(data0.iloc[i]['第三周减重值'])

    else:
        for i in range(len(data0)):
            if data0.iloc[i]['初始BMI']>24 and data0.iloc[i]['初始BMI']<28:
                id.append(data0.iloc[i]['uid'])
                weight2.append(data0.iloc[i]['第三周减重值'])

dataframe=pd.DataFrame({'用户编号':id,'减重值':weight2})
data = pd.merge(data4, dataframe, on='用户编号')
data=data[data['新饮食得分(100制)']>70]
reduced_weight= np.array(data['减重值']) #np.ndarray()
reduced_weight_list=reduced_weight.tolist() #list
print(reduced_weight_list)
medianreduced=round(get_median(reduced_weight_list),2)
meanreduced=round(get_average(reduced_weight_list),2)
weight.append(round(weight[3]-meanreduced,2))
print(weight[4])
bmi.append(float(weight[4]/pow(height/100,2)))
print(weight)
print(bmi)


#第五周
id=[]
weight2=[]
if bmi[4]<24:
    for i in range(len(data0)):
        if data0.iloc[i]['初始BMI']<24:
            id.append(data0.iloc[i]['uid'])
            weight2.append(data0.iloc[i]['第四周减重值'])
else:
    if bmi[4]>28:
        for i in range(len(data0)):
            if data0.iloc[i]['初始BMI']>28:
                id.append(data0.iloc[i]['uid'])
                weight2.append(data0.iloc[i]['第四周减重值'])

    else:
        for i in range(len(data0)):
            if data0.iloc[i]['初始BMI']>24 and data0.iloc[i]['初始BMI']<28:
                id.append(data0.iloc[i]['uid'])
                weight2.append(data0.iloc[i]['第四周减重值'])

dataframe=pd.DataFrame({'用户编号':id,'减重值':weight2})
data = pd.merge(data4, dataframe, on='用户编号')
data=data[data['新饮食得分(100制)']>70]
reduced_weight= np.array(data['减重值']) #np.ndarray()
reduced_weight_list=reduced_weight.tolist() #list
print(reduced_weight_list)
medianreduced=round(get_median(reduced_weight_list),2)
meanreduced=round(get_average(reduced_weight_list),2)
weight.append(round(weight[4]-meanreduced,2))
print(weight[5])
bmi.append(float(weight[5]/pow(height/100,2)))
print(weight)
print(bmi)

#绘制折线图
plt.rcParams['font.sans-serif']=[u'SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.title('某用户体重值预期变化图')
plt.xlabel('时间(周)')
plt.ylabel('体重值(KG)')
plt.grid(True)
week=[0,1,2,3,4,5]
plt.plot(week, weight, 'r', label='broadcast',marker='o')
for a, b in zip(week, weight):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.show()
