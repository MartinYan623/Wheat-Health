import pandas as pd
encoding='UTF-8'
data=pd.read_csv('/Users/martin_yan/Desktop/new_babymother_data5.22-6.25.csv')
#HEI删除了四项指标
#data.drop(['膳食纤维摄入实际量','膳食纤维摄入量得分','总热量摄入实际量','总热量摄入量得分','三大营养素摄入实际量','三大营养素组成得分','饮水量','饮水量得分'], inplace=True, axis=1)
info=pd.read_csv('../data/宝妈用户减重表5.22-6.25(全部).csv',usecols=[1,2])
original=pd.read_csv('../data/宝妈用户初始信息表.csv',usecols=['姓名','初始体重值','BMI'])
birthday=pd.read_csv('../data/宝妈营用户生日.csv',usecols=['uid','年龄'])
birthday.rename(columns={'uid':'用户编号'}, inplace = True)
data = pd.merge(data, info, on='姓名')
data = pd.merge(data, original, on='姓名')
data = pd.merge(data, birthday, on='用户编号')
print(len(data['姓名'].unique()))
print(data)

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


heiscore=0
balancescore=0
totalscore=0

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

    sum_f_diefiber = sum_f_diefiber + data.iloc[i][12]
    sum_diefiber = sum_diefiber + data.iloc[i][13]

    sum_f_milk = sum_f_milk + data.iloc[i][14]
    sum_milk = sum_milk + data.iloc[i][15]

    sum_f_totalprotein = sum_f_totalprotein + data.iloc[i][16]
    sum_totalprotein = sum_totalprotein + data.iloc[i][17]

    sum_f_fishshrimp = sum_f_fishshrimp + data.iloc[i][18]
    sum_fishshrimp = sum_fishshrimp + data.iloc[i][19]

    sum_f_fattyacids = sum_f_fattyacids + data.iloc[i][20]
    sum_fattyacids = sum_fattyacids + data.iloc[i][21]

    sum_f_solidfat = sum_f_solidfat + data.iloc[i][22]
    sum_solidfat = sum_solidfat + data.iloc[i][23]

    sum_f_salt = sum_f_salt + data.iloc[i][24]
    sum_salt = sum_salt + data.iloc[i][25]

    sum_f_sugar = sum_f_sugar + data.iloc[i][26]
    sum_sugar = sum_sugar + data.iloc[i][27]

    # sum_f_totalheat = sum_f_totalheat+data.iloc[i][28]
    sum_totalheat = sum_totalheat + data.iloc[i][30]

    sum_f_nutrients1 = sum_f_nutrients1 + data.iloc[i][31]
    sum_f_nutrients2 = sum_f_nutrients2 + data.iloc[i][32]
    sum_f_nutrients3 = sum_f_nutrients3 + data.iloc[i][33]
    sum_nutrients = sum_nutrients + data.iloc[i][34]

    sum_f_alcohol = sum_f_alcohol + data.iloc[i][35]
    sum_alcohol = sum_alcohol + data.iloc[i][36]

    sum_f_water = sum_f_water + data.iloc[i][37]
    sum_water = sum_water + data.iloc[i][38]

    heiscore = heiscore+data.iloc[i][5]+data.iloc[i][7]+data.iloc[i][9]+data.iloc[i][11]+data.iloc[i][15]+data.iloc[i][17]+data.iloc[i][19]+data.iloc[i][21]+data.iloc[i][23]+data.iloc[i][25]+data.iloc[i][27]+data.iloc[i][36]
    balancescore=balancescore+data.iloc[i][5]+data.iloc[i][7]+data.iloc[i][9]+data.iloc[i][11]+data.iloc[i][13]+data.iloc[i][15]+data.iloc[i][17]+data.iloc[i][19]+data.iloc[i][21]+data.iloc[i][23]+data.iloc[i][25]+data.iloc[i][27]+data.iloc[i][34]+data.iloc[i][36]+data.iloc[i][38]
    totalscore=totalscore+((data.iloc[i][5]+data.iloc[i][7]+data.iloc[i][9]+data.iloc[i][11]+data.iloc[i][13]+data.iloc[i][15]+data.iloc[i][17]+data.iloc[i][19]+data.iloc[i][21]+data.iloc[i][23]+data.iloc[i][25]+data.iloc[i][27]+data.iloc[i][34]+data.iloc[i][36]+data.iloc[i][38])/120)*90+(data.iloc[i][30]/10)*10

    if username[i]==False:
        num=num+1
        #除以实际记录天数
        """
        dataframe2 = pd.DataFrame({'用户编号': [data.iloc[i][0]], '姓名': [data.iloc[i][2]], '记录天数': [count],
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
                                   '饮酒实际摄入平均量': [sum_f_alcohol / count],'饮酒（酒精量，全天标准）平均分': [sum_alcohol / count],
                                   '饮水平均量': [sum_f_water / count], '饮水量平均分': [sum_water / count],
                                   'HEI平均得分': [heiscore / count],
                                   '饮食均衡得分':[balancescore/count],
                                   '新饮食得分':[totalscore/count],
                                   '减重值':[data.iloc[i][40]],'初始体重值':[data.iloc[i][41]],
                                   '减重百分比':[data.iloc[i][40]/data.iloc[i][41]],'BMI':[data.iloc[i][42]],'年龄':[data.iloc[i][43]]})
        """
        #除以入营以来的天数
        dataframe2 = pd.DataFrame({'用户编号': [data.iloc[i][0]], '姓名': [data.iloc[i][2]], '记录天数': [count],
                                   '水果实际摄入平均量': [sum_f_fruit / 35], '水果摄入量平均分': [sum_fruit / 35],
                                   '蔬菜实际摄入平均量': [sum_f_veg / 35], '蔬菜摄入量平均分': [sum_veg / 35],
                                   '全谷类实际摄入平均量': [sum_f_wholegrain / 35],
                                   '全谷类摄入量平均分': [sum_wholegrain / 35],
                                   '精制谷物摄入平均量': [sum_f_refinegrain / 35],
                                   '精制谷物摄入量平均分': [sum_refinegrain / 35],
                                   '膳食纤维实际摄入平均量': [sum_f_diefiber / 35],
                                   '膳食纤维摄入量平均分': [sum_diefiber / 35],
                                   '乳类实际摄入平均量': [sum_f_milk / 35], '乳类摄入量平均分': [sum_milk / 35],
                                   '总蛋白实际摄入平均量': [sum_f_totalprotein / 35],
                                   '总蛋白摄入量平均分': [sum_totalprotein / 35],
                                   '鱼虾贝壳类及植物蛋白类实际摄入平均量': [sum_f_fishshrimp / 35],
                                   '鱼虾贝壳类及植物蛋白类摄入量平均分': [sum_fishshrimp / 35],
                                   '不饱和与饱和脂肪酸摄入平均对比值': [sum_f_fattyacids / 35],
                                   '不饱和与饱和脂肪酸摄入比平均分': [sum_fattyacids / 35],
                                   '固态脂肪实际摄入平均量': [sum_f_solidfat / 35],
                                   '固态脂肪摄入量平均分': [sum_solidfat / 35],
                                   '钠盐实际摄入平均量': [sum_f_salt / 35], '钠盐摄入量平均分': [sum_salt / 35],
                                   '添加糖实际摄入平均量': [sum_f_sugar /35], '添加糖摄入量平均分': [sum_sugar / 35],
                                   '总热量摄入量平均分': [sum_totalheat / 35],
                                   '三大营养素碳水化合物平均对比值': [sum_f_nutrients1 / 35],
                                   '三大营养素脂肪平均对比值': [sum_f_nutrients2 / 35],
                                   '三大营养素蛋白质平均对比值': [sum_f_nutrients3 / 35],
                                   '三大营养素组成平均分': [sum_nutrients / 35],
                                   '饮酒实际摄入平均量': [sum_f_alcohol / 35], '饮酒（酒精量，全天标准）平均分': [sum_alcohol / 35],
                                   '饮水平均量': [sum_f_water / 35], '饮水量平均分': [sum_water / 35],
                                   'HEI平均得分': [heiscore / 35],
                                   '饮食均衡得分': [balancescore / 35],
                                   '新饮食得分': [totalscore / 35],
                                   '减重值': [data.iloc[i][40]], '初始体重值': [data.iloc[i][41]],
                                   '减重百分比': [data.iloc[i][40] / data.iloc[i][41]], 'BMI': [data.iloc[i][42]],
                                   '年龄': [data.iloc[i][43]]})

        sec=True
        if num>1:
            sec=False
        columns = ['用户编号', '姓名', '年龄', 'BMI', '记录天数', '水果实际摄入平均量', '水果摄入量平均分', '蔬菜实际摄入平均量', '蔬菜摄入量平均分', '全谷类实际摄入平均量',
                   '全谷类摄入量平均分','精制谷物摄入平均量', '精制谷物摄入量平均分', '膳食纤维实际摄入平均量', '膳食纤维摄入量平均分', '乳类实际摄入平均量', '乳类摄入量平均分', '总蛋白实际摄入平均量',
                   '总蛋白摄入量平均分', '鱼虾贝壳类及植物蛋白类实际摄入平均量', '鱼虾贝壳类及植物蛋白类摄入量平均分',
                   '不饱和与饱和脂肪酸摄入平均对比值', '不饱和与饱和脂肪酸摄入比平均分', '固态脂肪实际摄入平均量', '固态脂肪摄入量平均分', '钠盐实际摄入平均量',
                   '钠盐摄入量平均分', '添加糖实际摄入平均量', '添加糖摄入量平均分', '总热量摄入量平均分', '三大营养素碳水化合物平均对比值', '三大营养素脂肪平均对比值',
                   '三大营养素蛋白质平均对比值', '三大营养素组成平均分', '饮酒实际摄入平均量',
                   '饮酒（酒精量，全天标准）平均分', '饮水平均量', '饮水量平均分', 'HEI平均得分','饮食均衡得分','新饮食得分', '初始体重值', '减重值', '减重百分比']

        dataframe2.to_csv('/Users/martin_yan/Desktop/3.csv', index=False, encoding="utf_8_sig",columns=columns,mode='a',header=sec)

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

        heiscore=0
        balancescore=0
        totalscore = 0
        count = 0


"""
data=pd.read_csv('/Users/martin_yan/Desktop/记录餐数.csv',usecols=[0,2,3,4])
completedata=pd.read_csv('/Users/martin_yan/Desktop/3.csv')
#data=data[data['记录日期']<'2018/5/29 0:00']
data = data.drop_duplicates(['uid','记录日期'])
data = data.dropna(subset=['姓名'])
data=data.reset_index(drop=True)
username=data.duplicated('uid',keep='last')
print(username)
count=0
meal=[]
name=[]
for i in range(len(data)):
    if data.iloc[i]['记录餐数']==2:
        count=count+1
    if username[i]==False:
        name.append(data.iloc[i]['姓名'])
        meal.append(count)
        count=0
dataframe=pd.DataFrame({'姓名':name,'完整记录天数':meal})
data = pd.merge(dataframe,completedata, on='姓名')
print(data)
columns= ['用户编号', '姓名', '年龄','BMI','记录天数','完整记录天数','水果实际摄入平均量', '水果摄入量平均分', '蔬菜实际摄入平均量', '蔬菜摄入量平均分', '全谷类实际摄入平均量', '全谷类摄入量平均分',
                    '精制谷物摄入平均量', '精制谷物摄入量平均分', '乳类实际摄入平均量', '乳类摄入量平均分', '总蛋白实际摄入平均量','总蛋白摄入量平均分', '鱼虾贝壳类及植物蛋白类实际摄入平均量',
                    '鱼虾贝壳类及植物蛋白类摄入量平均分','不饱和与饱和脂肪酸实际摄入平均量', '不饱和与饱和脂肪酸摄入比平均分', '固态脂肪实际摄入平均量', '固态脂肪摄入量平均分', '钠盐实际摄入平均量',
                    '钠盐摄入量平均分','添加糖实际摄入平均量', '添加糖摄入量平均分', '饮酒实际摄入平均量','饮酒（酒精量，全天标准）平均分', '平均得分','初始体重值','减重值','减重百分比']
#data.to_csv('/Users/martin_yan/Desktop/3333333.csv',index=False, encoding="utf_8_sig",columns=columns)

"""