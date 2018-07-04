import pandas as pd
import numpy as np
import datetime
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

score1=0
score2=0
countlight=0
countnormal=0
lightscore1=[]
lightscore2=[]
normalscore1=[]
normalscore2=[]
totalscore1=[]
totalscore2=[]
day1=[]
day2=[]
name=[]
id=[]
for i in range(len(data)):
    number = data.iloc[i]['对比值']
    if data.iloc[i]['是否为轻食日'] == 1:
        countlight = countlight + 1
        # [92-108]
        if number>91.99 and number<108.01:
            score1=score1+10
        # [83-92) or (108-117]
        if (number < 92 and number > 82.99) or (number>108 and number<117.01):
            score1 = score1 + 8
        # [76-83) or (117-124]
        if (number < 83 and number > 75.99) or (number>117 and number<124.01):
            score1 = score1 + 6
        # [66-76) or (124-134]
        if (number < 76 and number > 65.99) or (number > 124 and number < 134.01):
            score1 = score1 + 4
        # [60 - 66) or (134 - 140]
        if (number < 66 and number > 59.99) or (number > 134 and number < 140.01):
            score1 = score1 + 2
        # 其余 <60 or >140

    else:
        countnormal=countnormal+1
        # [82 - 109]
        if number>81.99 and number<109.01:
            score2=score2+10
        # [76-82)
        if number>75.99 and number<82:
            score2=score2+8
        # [65-76)
        if number > 64.99 and number < 76:
            score2=score2+5
        # [60-65)
        if number>59.99 and number<65:
            score2=score2+2
        # 其余 <60 or >109

    if last[i]==False:
        id.append(data.iloc[i]['uid'])
        name.append(data.iloc[i]['姓名'])
        if countlight==0:
            lightscore1.append(0)
        else:
            lightscore1.append(score1/countlight)
        lightscore2.append(score1 / 10)
        day1.append(countlight)
        if countnormal==0:
            normalscore1.append(0)
        else:
            normalscore1.append(score2/countnormal)
        normalscore2.append(score2/25)
        day2.append(countnormal)
        totalscore1.append((score1+score2)/(countnormal+countlight))
        totalscore2.append((score1+score2)/35)

        score1=0
        score2=0
        countlight=0
        countnormal=0

meanheat=pd.DataFrame({'用户编号':id,'姓名':name,'轻食日天数':day1,'普通日天数':day2,'轻食日热量平均分(实际记录天数)':lightscore1,'轻食日热量平均分(入营天数)':lightscore2,
                       '普通日热量平均分(实际记录天数)':normalscore1,'普通日热量平均分(入营天数)':normalscore2,
                       '总热量摄入平均分(实际记录天数)': totalscore1, '总热量摄入平均分(入营天数)': totalscore2
                       })
mean=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.25(体重跨度5周／实际记录平均分).csv',usecols=['姓名','减重值'])
data = pd.merge(meanheat,mean, on='姓名')
columns=['用户编号','姓名','减重值','轻食日天数','普通日天数','轻食日热量平均分(实际记录天数)','轻食日热量平均分(入营天数)',
                       '普通日热量平均分(实际记录天数)','普通日热量平均分(入营天数)',
                       '总热量摄入平均分(实际记录天数)', '总热量摄入平均分(入营天数)']
data.to_csv('/Users/martin_yan/Desktop/新热量区间换算热量分值2.csv', index=False, encoding="utf_8_sig",columns=columns)