import pandas as pd
import datetime
encoding='UTF-8'
data=pd.read_csv('/Users/martin_yan/Desktop/babymother_data5.22-6.25.csv')
info=pd.read_csv('../data/宝妈用户减重表5.22-6.25(全部).csv',usecols=[1,2])
original=pd.read_csv('../data/宝妈用户初始信息表.csv',usecols=['姓名','初始体重值','BMI'])
birthday=pd.read_csv('../data/宝妈营用户生日.csv',usecols=['uid','年龄'])
birthday.rename(columns={'uid':'用户编号'}, inplace = True)
data = pd.merge(data, info, on='姓名')
data = pd.merge(data, original, on='姓名')
data = pd.merge(data, birthday, on='用户编号')
print(len(data['姓名'].unique()))

username=data.duplicated('用户编号',keep='last')
sum_fruit = 0
sum_f_fruit = 0
sum_veg = 0
sum_f_veg = 0
sum_wholegrain = 0
sum_f_wholegrain = 0
sum_refinegrain = 0
sum_f_refinegrain = 0
sum_diefiber = 0
sum_f_diefiber = 0
sum_milk = 0
sum_f_milk = 0
sum_totalprotein = 0
sum_f_totalprotein = 0
sum_fishshrimp = 0
sum_f_fishshrimp = 0
sum_fattyacids = 0
sum_f_fattyacids = 0
sum_solidfat = 0
sum_f_solidfat = 0
sum_salt = 0
sum_f_salt = 0
sum_sugar = 0
sum_f_sugar = 0
sum_totalheat = 0
sum_nutrients = 0
sum_f_nutrients1 = 0
sum_f_nutrients2 = 0
sum_f_nutrients3 = 0
sum_alcohol = 0
sum_f_alcohol = 0
sum_water = 0
sum_f_water = 0
score=0

count=0
num=0
for i in range(len(data)):
    count=count+1

    sum_f_fruit=sum_f_fruit+data.iloc[i][4]
    sum_fruit = sum_fruit + data.iloc[i][5]

    sum_f_veg = sum_f_veg + data.iloc[i][6]
    sum_veg = sum_veg + data.iloc[i][7]

    sum_f_wholegrain = sum_f_wholegrain+data.iloc[i][8]
    sum_wholegrain = sum_wholegrain+data.iloc[i][9]

    sum_f_refinegrain = sum_f_refinegrain+data.iloc[i][10]
    sum_refinegrain = sum_refinegrain+data.iloc[i][11]

    sum_f_diefiber = sum_f_diefiber+data.iloc[i][12]
    sum_diefiber =  sum_diefiber+data.iloc[i][13]

    sum_f_milk = sum_f_milk+data.iloc[i][14]
    sum_milk = sum_milk+data.iloc[i][15]

    sum_f_totalprotein = sum_f_totalprotein+data.iloc[i][16]
    sum_totalprotein =   sum_totalprotein+data.iloc[i][17]

    sum_f_fishshrimp = sum_f_fishshrimp+data.iloc[i][18]
    sum_fishshrimp = sum_fishshrimp+data.iloc[i][19]

    sum_f_fattyacids = sum_f_fattyacids+data.iloc[i][20]
    sum_fattyacids = sum_fattyacids+data.iloc[i][21]

    sum_f_solidfat = sum_f_solidfat+data.iloc[i][22]
    sum_solidfat = sum_solidfat+data.iloc[i][23]

    sum_f_salt = sum_f_salt+data.iloc[i][24]
    sum_salt =  sum_salt+data.iloc[i][25]

    sum_f_sugar = sum_f_sugar+data.iloc[i][26]
    sum_sugar =  sum_sugar+data.iloc[i][27]

    #sum_f_totalheat = sum_f_totalheat+data.iloc[i][28]
    sum_totalheat =  sum_totalheat+data.iloc[i][30]

    sum_f_nutrients1 = sum_f_nutrients1+data.iloc[i][31]
    sum_f_nutrients2 = sum_f_nutrients2 + data.iloc[i][32]
    sum_f_nutrients3 = sum_f_nutrients3 + data.iloc[i][33]
    sum_nutrients = sum_nutrients+data.iloc[i][34]

    sum_f_alcohol = sum_f_alcohol+data.iloc[i][35]
    sum_alcohol = sum_alcohol+data.iloc[i][36]

    sum_f_water = sum_f_water+data.iloc[i][37]
    sum_water =  sum_water+data.iloc[i][38]

    score = score+data.iloc[i][39]

    if username[i]==False:
        num=num+1

        #除以实际记录天数
        dataframe = pd.DataFrame({'用户编号': [data.iloc[i][0]], '姓名': [data.iloc[i][2]], '记录天数': [count],
                                   '水果实际摄入平均量': [sum_f_fruit / count], '水果摄入量平均分': [sum_fruit / count],
                                   '蔬菜实际摄入平均量': [sum_f_veg / count], '蔬菜摄入量平均分': [sum_veg / count],
                                   '全谷类实际摄入平均量': [sum_f_wholegrain / count],
                                   '全谷类摄入量平均分': [sum_wholegrain / count],
                                   '精制谷物摄入平均量': [sum_f_refinegrain / count],
                                   '精制谷物摄入量平均分': [sum_refinegrain / count],
                                   '膳食纤维实际摄入平均量': [sum_f_diefiber / count],
                                   '膳食纤维摄入量平均分': [sum_diefiber / count],
                                   '乳类实际摄入平均量': [sum_f_milk / count], '乳类摄入量平均分': [sum_milk / count],
                                   '总蛋白实际摄入平均量': [sum_f_totalprotein / count],
                                   '总蛋白摄入量平均分': [sum_totalprotein / count],
                                   '鱼虾贝壳类及植物蛋白类实际摄入平均量': [sum_f_fishshrimp / count],
                                   '鱼虾贝壳类及植物蛋白类摄入量平均分': [sum_fishshrimp / count],
                                   '不饱和与饱和脂肪酸摄入平均对比值': [sum_f_fattyacids / count],
                                   '不饱和与饱和脂肪酸摄入比平均分': [sum_fattyacids / count],
                                   '固态脂肪实际摄入平均量': [sum_f_solidfat / count],
                                   '固态脂肪摄入量平均分': [sum_solidfat / count],
                                   '钠盐实际摄入平均量': [sum_f_salt / count], '钠盐摄入量平均分': [sum_salt / count],
                                   '添加糖实际摄入平均量': [sum_f_sugar /count], '添加糖摄入量平均分': [sum_sugar / count],
                                   '总热量摄入量平均分': [sum_totalheat / count],
                                  '三大营养素碳水化合物平均对比值': [sum_f_nutrients1 / count],
                                  '三大营养素脂肪平均对比值': [sum_f_nutrients2 / count],
                                  '三大营养素蛋白质平均对比值': [sum_f_nutrients3 / count],
                                   '三大营养素组成平均分': [sum_nutrients / count],
                                   '饮酒实际摄入平均量': [sum_f_alcohol / count],
                                   '饮酒（酒精量，全天标准）平均分': [sum_alcohol / count],
                                   '饮水平均量': [sum_f_water / count], '饮水量平均分': [sum_water / count],
                                   '平均得分': [score / count],'减重值':[data.iloc[i][40]],'初始体重值':[data.iloc[i][41]],
                                   '减重百分比':[data.iloc[i][40]/data.iloc[i][41]],'BMI':[data.iloc[i][42]],'年龄':[data.iloc[i][43]]})
        """
        #除以入营以来的天数
        dataframe = pd.DataFrame({'用户编号': [data.iloc[i][0]], '姓名': [data.iloc[i][2]], '记录天数': [count],
                                   '水果实际摄入平均量': [sum_f_fruit / 35], '水果摄入量平均分': [sum_fruit / 35],
                                   '蔬菜实际摄入平均量': [sum_f_veg / 35], '蔬菜摄入量平均分': [sum_veg /35],
                                   '全谷类实际摄入平均量': [sum_f_wholegrain / 35],
                                   '全谷类摄入量平均分': [sum_wholegrain / 35],
                                   '精制谷物摄入平均量': [sum_f_refinegrain / 35],
                                   '精制谷物摄入量平均分': [sum_refinegrain / 35],
                                   '膳食纤维实际摄入平均量': [sum_f_diefiber / 35],
                                   '膳食纤维摄入量平均分': [sum_diefiber / 35],
                                   '乳类实际摄入平均量': [sum_f_milk / count], '乳类摄入量平均分': [sum_milk / 35],
                                   '总蛋白实际摄入平均量': [sum_f_totalprotein / 35],
                                   '总蛋白摄入量平均分': [sum_totalprotein / 35],
                                   '鱼虾贝壳类及植物蛋白类实际摄入平均量': [sum_f_fishshrimp / 35],
                                   '鱼虾贝壳类及植物蛋白类摄入量平均分': [sum_fishshrimp / 35],
                                   '不饱和与饱和脂肪酸摄入平均对比值': [sum_f_fattyacids / 35],
                                   '不饱和与饱和脂肪酸摄入比平均分': [sum_fattyacids / 35],
                                   '固态脂肪实际摄入平均量': [sum_f_solidfat / 35],
                                   '固态脂肪摄入量平均分': [sum_solidfat / 35],
                                   '钠盐实际摄入平均量': [sum_f_salt / 35], '钠盐摄入量平均分': [sum_salt / 35],
                                   '添加糖实际摄入平均量': [sum_f_sugar / 35], '添加糖摄入量平均分': [sum_sugar /35],
                                   '总热量摄入量平均分': [sum_totalheat / 35],
                                   '三大营养素碳水化合物平均对比值': [sum_f_nutrients1 / 35],
                                  '三大营养素脂肪平均对比值': [sum_f_nutrients2 / 35],
                                  '三大营养素蛋白质平均对比值': [sum_f_nutrients3 / 35],
                                   '三大营养素组成平均分': [sum_nutrients / 35],
                                   '饮酒实际摄入平均量': [sum_f_alcohol / 35],
                                   '饮酒（酒精量，全天标准）平均分': [sum_alcohol / 35],
                                   '饮水平均量': [sum_f_water / 35], '饮水量平均分': [sum_water / 35],
                                   '平均得分': [score / 35], '减重值': [data.iloc[i][40]], '初始体重值': [data.iloc[i][41]],
                                   '减重百分比': [data.iloc[i][40] / data.iloc[i][41]], 'BMI': [data.iloc[i][42]],
                                   '年龄': [data.iloc[i][43]]})
        """
        sec=True
        if num>1:
            sec=False
        columns = ['用户编号', '姓名', '年龄','BMI','记录天数','水果实际摄入平均量', '水果摄入量平均分', '蔬菜实际摄入平均量', '蔬菜摄入量平均分', '全谷类实际摄入平均量', '全谷类摄入量平均分',
                    '精制谷物摄入平均量', '精制谷物摄入量平均分', '膳食纤维实际摄入平均量', '膳食纤维摄入量平均分', '乳类实际摄入平均量', '乳类摄入量平均分', '总蛋白实际摄入平均量',
                    '总蛋白摄入量平均分', '鱼虾贝壳类及植物蛋白类实际摄入平均量', '鱼虾贝壳类及植物蛋白类摄入量平均分',
                    '不饱和与饱和脂肪酸摄入平均对比值', '不饱和与饱和脂肪酸摄入比平均分', '固态脂肪实际摄入平均量', '固态脂肪摄入量平均分', '钠盐实际摄入平均量',
                   '钠盐摄入量平均分','添加糖实际摄入平均量', '添加糖摄入量平均分', '总热量摄入量平均分',   '三大营养素碳水化合物平均对比值','三大营养素脂肪平均对比值',
                    '三大营养素蛋白质平均对比值', '三大营养素组成平均分', '饮酒实际摄入平均量',
                    '饮酒（酒精量，全天标准）平均分', '饮水平均量', '饮水量平均分','平均得分','初始体重值','减重值','减重百分比']

        dataframe.to_csv('/Users/martin_yan/Desktop/21.csv', index=False, encoding="utf_8_sig",
                          columns=columns,mode='a',header=sec)

        sum_fruit = 0
        sum_f_fruit = 0
        sum_veg = 0
        sum_f_veg = 0
        sum_wholegrain = 0
        sum_f_wholegrain = 0
        sum_refinegrain = 0
        sum_f_refinegrain = 0
        sum_diefiber = 0
        sum_f_diefiber = 0
        sum_milk = 0
        sum_f_milk = 0
        sum_totalprotein = 0
        sum_f_totalprotein = 0
        sum_fishshrimp = 0
        sum_f_fishshrimp = 0
        sum_fattyacids = 0
        sum_f_fattyacids = 0
        sum_solidfat = 0
        sum_f_solidfat = 0
        sum_salt = 0
        sum_f_salt = 0
        sum_sugar = 0
        sum_f_sugar = 0
        sum_totalheat = 0
        sum_nutrients = 0
        sum_f_nutrients1 = 0
        sum_f_nutrients2 = 0
        sum_f_nutrients3 = 0
        sum_alcohol = 0
        sum_f_alcohol = 0
        sum_water = 0
        sum_f_water = 0
        score = 0
        count = 0


data=pd.read_csv('/Users/martin_yan/Desktop/每日热量统计.csv',usecols=[1,4,5,6])
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

sum_f_normal=0
sum_f_light=0
sum_normal=0
sum_light=0

countlight = 0
countnormal = 0

meanflight=[]
meanfnormal=[]
meanlight=[]
meannormal=[]

name=[]
print(data)
for i in range(len(data)):
    value = data.iloc[i]['摄入值']
    number = data.iloc[i]['对比值']

    if data.iloc[i]['是否为轻食日'] == 1:
        sum_f_light  = sum_f_light + value
        sum_light = sum_light + number
        countlight=countlight+1

    else:
        sum_f_normal = sum_f_normal + value
        sum_normal = sum_normal + number
        countnormal=countnormal+1

    if last[i] == False:
        name.append(data.iloc[i]['姓名'])


        #除以记录天数
        if countlight==0:
            meanlight.append(0)
            meanflight.append(0)
        else:
            meanlight.append(sum_light/countlight)
            meanflight.append(sum_f_light/countlight)
        if countnormal==0:
            meannormal.append(0)
            meanfnormal.append(0)
        else:
            meannormal.append(sum_normal/countnormal)
            meanfnormal.append(sum_f_normal/countnormal)

        """

        #除以实际入营天数
        meanflight.append(sum_f_light / 10)
        meanlight.append(sum_light / 10)
        meanfnormal.append(sum_f_normal / 25)
        meannormal.append(sum_normal / 25)
        """


        sum_light=0
        sum_normal=0
        sum_f_light = 0
        sum_f_normal = 0
        countlight=0
        countnormal=0

meanheat=pd.DataFrame({'姓名':name,'轻食日热量平均摄入值':meanflight,'普通日热量平均摄入值':meanfnormal,'轻食日热量平均对比值':meanlight,'普通日热量平均对比值':meannormal})
mean=pd.read_csv('/Users/martin_yan/Desktop/21.csv')
data = pd.merge(mean, meanheat, on='姓名')
data.to_csv('/Users/martin_yan/Desktop/31.csv', index=False, encoding="utf_8_sig")