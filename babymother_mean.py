import pandas as pd
encoding='UTF-8'
data=pd.read_csv('/Users/martin_yan/Desktop/new_babymother_data.csv')
info=pd.read_csv('data/用户信息表2.csv')
data = pd.merge(data, info, on='姓名')
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
sum_f_totalheat = 0
sum_nutrients = 0
sum_f_nutrients = 0
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

    sum_f_totalheat = sum_f_totalheat+data.iloc[i][28]
    sum_totalheat =  sum_totalheat+data.iloc[i][29]

    sum_f_nutrients = sum_f_nutrients+data.iloc[i][30]
    sum_nutrients = sum_nutrients+data.iloc[i][31]

    sum_f_alcohol = sum_f_alcohol+data.iloc[i][32]
    sum_alcohol = sum_alcohol+data.iloc[i][33]

    sum_f_water = sum_f_water+data.iloc[i][34]
    sum_water =  sum_water+data.iloc[i][35]

    score = score+data.iloc[i][36]

    if username[i]==False:
        num=num+1
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
                                   '不饱和与饱和脂肪酸实际摄入平均量': [sum_f_fattyacids / count],
                                   '不饱和与饱和脂肪酸摄入比平均分': [sum_fattyacids / count],
                                   '固态脂肪实际摄入平均量': [sum_f_solidfat / count],
                                   '固态脂肪摄入量平均分': [sum_solidfat / count],
                                   '钠盐实际摄入平均量': [sum_f_salt / count], '钠盐摄入量平均分': [sum_salt / count],
                                   '添加糖实际摄入平均量': [sum_f_sugar /count], '添加糖摄入量平均分': [sum_sugar / count],
                                   '总热量实际摄入平均量': [sum_f_totalheat / count],
                                   '总热量摄入量平均分': [sum_totalheat / count],
                                   '三大营养素实际摄入平均量': [sum_f_nutrients / count],
                                   '三大营养素组成平均分': [sum_nutrients / count],
                                   '饮酒实际摄入平均量': [sum_f_alcohol / count],
                                   '饮酒（酒精量，全天标准）平均分': [sum_alcohol / count],
                                   '饮水平均量': [sum_f_water / count], '饮水量平均分': [sum_water / count],
                                   '平均得分': [score / count],'减重值':[data.iloc[i][37]],'BMI':[data.iloc[i][38]]})

        sec=True
        if num>1:
            sec=False
        columns2 = ['用户编号', '姓名', '记录天数','水果实际摄入平均量', '水果摄入量平均分', '蔬菜实际摄入平均量', '蔬菜摄入量平均分', '全谷类实际摄入平均量', '全谷类摄入量平均分',
                    '精制谷物摄入平均量', '精制谷物摄入量平均分', '膳食纤维实际摄入平均量', '膳食纤维摄入量平均分', '乳类实际摄入平均量', '乳类摄入量平均分', '总蛋白实际摄入平均量',
                    '总蛋白摄入量平均分', '鱼虾贝壳类及植物蛋白类实际摄入平均量', '鱼虾贝壳类及植物蛋白类摄入量平均分',
                    '不饱和与饱和脂肪酸实际摄入平均量', '不饱和与饱和脂肪酸摄入比平均分', '固态脂肪实际摄入平均量', '固态脂肪摄入量平均分', '钠盐实际摄入平均量', '钠盐摄入量平均分',
                    '添加糖实际摄入平均量', '添加糖摄入量平均分', '总热量实际摄入平均量', '总热量摄入量平均分', '三大营养素实际摄入平均量', '三大营养素组成平均分', '饮酒实际摄入平均量',
                    '饮酒（酒精量，全天标准）平均分', '饮水平均量', '饮水量平均分','平均得分','减重值','BMI']

        dataframe2.to_csv('/Users/martin_yan/Desktop/new_mean_babymother_data.csv', index=False, encoding="utf_8_sig",
                          columns=columns2,mode='a',header=sec)

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
        sum_f_totalheat = 0
        sum_nutrients = 0
        sum_f_nutrients = 0
        sum_alcohol = 0
        sum_f_alcohol = 0
        sum_water = 0
        sum_f_water = 0
        score = 0
        count = 0
