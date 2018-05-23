import pandas as pd
encoding='UTF-8'
weight=pd.read_csv('data/用户信息表.csv',usecols=[0,3,4,5,6,7])
for num in range(0,12):
    data = pd.read_csv('data/%d.csv' % num)
    data.drop(['营id','PB','实际值','对比值','推荐满分区间'], inplace=True, axis=1)
    data=data[(True-data['RF'].isin(['有氧运动','吸烟']))]
    data=data.drop_duplicates()
    userid=[]
    name=[]
    fruit=[]
    veg=[]
    wholegrain=[]
    refinegrain=[]
    diefiber=[]
    milk=[]
    totalprotein=[]
    fishshrimp=[]
    fattyacids=[]
    solidfat=[]
    salt=[]
    sugar=[]
    totalheat=[]
    nutrients=[]
    alcohol=[]
    water=[]
    for i in range(0, len(data)):
        if data.iloc[i]['RF']=='水果摄入量':
            fruit.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF']=='蔬菜摄入量':
            veg.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF']=='全谷类摄入量':
            wholegrain.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '精制谷物摄入量':
            refinegrain.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '膳食纤维摄入量':
            diefiber.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '乳类摄入量':
            milk.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '总蛋白摄入量':
            totalprotein.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '鱼虾贝壳类及植物蛋白类摄入量':
            fishshrimp.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '不饱和与饱和脂肪酸摄入比':
            fattyacids.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '固态脂肪摄入量':
            solidfat.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '钠盐摄入量':
            salt.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '添加糖摄入量':
            sugar.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '总热量摄入量':
            totalheat.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '三大营养素组成':
            nutrients.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '饮酒（酒精量，全天标准）':
            alcohol.append(data.iloc[i]['实际得分'])

        if data.iloc[i]['RF'] == '饮水量':
            water.append(data.iloc[i]['实际得分'])
    totalscore=[]
    time=data['记录日期'].unique()
    sum_fruit = 0
    #sum_f_fruit = 0
    sum_veg = 0
    #sum_f_veg = 0
    sum_wholegrain = 0
    #sum_f_wholegrain = 0
    sum_refinegrain = 0
    #sum_f_refinegrain = 0
    sum_diefiber = 0
    #sum_f_diefiber = 0
    sum_milk = 0
    #sum_f_milk = 0
    sum_totalprotein = 0
    #sum_f_totalprotein = 0
    sum_fishshrimp = 0
    #sum_f_fishshrimp = 0
    sum_fattyacids = 0
    #sum_f_fattyacids = 0
    sum_solidfat = 0
    #sum_f_solidfat = 0
    sum_salt = 0
    #sum_f_salt = 0
    sum_sugar = 0
    #sum_f_sugar = 0
    sum_totalheat = 0
    #sum_f_totalheat = 0
    sum_nutrients = 0
    #sum_f_nutrients = 0
    sum_alcohol = 0
    #sum_f_alcohol = 0
    sum_water = 0
    #sum_f_water = 0

    for i in range(0,len(time)):
        userid.append(data.iloc[1][0])
        name.append(data.iloc[1]['姓名'])
        totalscore.append(fruit[i]+veg[i]+wholegrain[i]+refinegrain[i]+diefiber[i]+milk[i]+totalprotein[i]+fishshrimp[i]+fattyacids[i]
                      +solidfat[i]+salt[i]+sugar[i]+totalheat[i]+nutrients[i]+alcohol[i]+water[i])
        sum_fruit = sum_fruit + fruit[i]
        sum_veg = sum_veg + veg[i]
        sum_wholegrain = sum_wholegrain + wholegrain[i]
        sum_refinegrain = sum_refinegrain + refinegrain[i]
        sum_diefiber = sum_diefiber + diefiber[i]
        sum_milk = sum_milk + milk[i]
        sum_totalprotein = sum_totalprotein + totalprotein[i]
        sum_fishshrimp = sum_fishshrimp + fishshrimp[i]
        sum_fattyacids = sum_fattyacids + fattyacids[i]
        sum_solidfat = sum_solidfat + solidfat[i]
        sum_salt = sum_salt + salt[i]
        sum_sugar = sum_sugar + sugar[i]
        sum_totalheat = sum_totalheat + totalheat[i]
        sum_nutrients = sum_nutrients + nutrients[i]
        sum_alcohol = sum_alcohol + alcohol[i]
        sum_water = sum_water + water[i]

    sec = True
    if num > 0:
        sec = False
    dataframe = pd.DataFrame({'用户编号': userid , '姓名':name, '记录日期':time, '水果摄入量得分': fruit,'蔬菜摄入量得分':veg,'全谷类摄入量得分':wholegrain,'精制谷物摄入量得分':refinegrain,
                          '膳食纤维摄入量得分':diefiber,'乳类摄入量得分':milk,'总蛋白摄入量得分':totalprotein,'鱼虾贝壳类及植物蛋白类摄入量得分':fishshrimp,'不饱和与饱和脂肪酸摄入比得分':fattyacids,
    '固态脂肪摄入量得分':solidfat,'钠盐摄入量得分':salt,'添加糖摄入量得分':sugar,'总热量摄入量得分':totalheat,'三大营养素组成得分':nutrients,'饮酒（酒精量，全天标准）得分':alcohol,'饮水量得分':water,'总得分':totalscore})

    columns = ['用户编号','姓名','记录日期','水果摄入量得分','蔬菜摄入量得分','全谷类摄入量得分','精制谷物摄入量得分','膳食纤维摄入量得分','乳类摄入量得分','总蛋白摄入量得分','鱼虾贝壳类及植物蛋白类摄入量得分'
    ,'不饱和与饱和脂肪酸摄入比得分','固态脂肪摄入量得分','钠盐摄入量得分','添加糖摄入量得分','总热量摄入量得分','三大营养素组成得分','饮酒（酒精量，全天标准）得分','饮水量得分','总得分']
    dataframe.to_csv('/Users/martin_yan/Desktop/data.csv', index=False, encoding="utf_8_sig", columns=columns, mode='a',
                     header=sec)
    wei = weight.iloc[num]['减重值']
    dataframe2 = pd.DataFrame({'用户编号': [data.iloc[1][0]], '姓名': [data.iloc[1]['姓名']], '记录天数': [len(time)],
                                '水果摄入量平均分': [sum_fruit / len(time)],
                                '蔬菜摄入量平均分': [sum_veg / len(time)],
                               '全谷类摄入量平均分': [sum_wholegrain / len(time)],
                               '精制谷物摄入量平均分': [sum_refinegrain / len(time)],
                               '膳食纤维摄入量平均分': [sum_diefiber / len(time)],
                               '乳类摄入量平均分': [sum_milk / len(time)],
                               '总蛋白摄入量平均分': [sum_totalprotein / len(time)],
                               '鱼虾贝壳类及植物蛋白类摄入量平均分': [sum_fishshrimp / len(time)],
                               '不饱和与饱和脂肪酸摄入比平均分': [sum_fattyacids / len(time)],
                               '固态脂肪摄入量平均分': [sum_solidfat / len(time)],
                                '钠盐摄入量平均分': [sum_salt / len(time)],
                                '添加糖摄入量平均分': [sum_sugar / len(time)],
                                '总热量摄入量平均分': [sum_totalheat / len(time)],
                                '三大营养素组成平均分': [sum_nutrients / len(time)],
                                '饮酒（酒精量，全天标准）平均分': [sum_alcohol / len(time)],
                                '饮水量平均分': [sum_water / len(time)],'减重值':[wei]
                               })

    columns2 = ['用户编号', '姓名', '记录天数', '水果摄入量平均分', '蔬菜摄入量平均分', '全谷类摄入量平均分',
                 '精制谷物摄入量平均分', '膳食纤维摄入量平均分','乳类摄入量平均分',
                '总蛋白摄入量平均分',  '鱼虾贝壳类及植物蛋白类摄入量平均分',
                 '不饱和与饱和脂肪酸摄入比平均分','固态脂肪摄入量平均分', '钠盐摄入量平均分',
                '添加糖摄入量平均分', '总热量摄入量平均分', '三大营养素组成平均分',
                '饮酒（酒精量，全天标准）平均分', '饮水量平均分','减重值']

    dataframe2.to_csv('/Users/martin_yan/Desktop/mean_data.csv', index=False, encoding="utf_8_sig", columns=columns2,
                      mode='a', header=sec)


