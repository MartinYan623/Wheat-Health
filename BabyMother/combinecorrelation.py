import pandas as pd
encoding='UTF-8'
import matplotlib.pyplot as plt
# 将多周多个表相关性按相同指标合并 并绘制折线图
data=pd.read_csv('/Users/martin_yan/Desktop/90人 记录得分 减重值.csv')
print(data)
reduce=[]
percent=[]
f_fruit = []
fruit = []
f_veg = []
veg = []
f_wholegrain = []
wholegrain = []
f_refinegrain = []
refinegrain = []
f_diefiber = []
diefiber = []
f_milk = []
milk = []
f_totalprotein = []
totalprotein = []
f_fishshrimp = []
fishshrimp = []
f_fattyacids = []
fattyacids = []
f_solidfat = []
solidfat = []
f_salt = []
salt = []
f_sugar = []
sugar = []
f_totalheat1 = []
f_totalheat2 = []
c_totalheat1=[]
c_totalheat2=[]
totalheat = []
f_nutrients1 = []
f_nutrients2 = []
f_nutrients3 = []
nutrients = []
f_alcohol = []
alcohol = []
f_water = []
water = []
bmi=[]
age=[]
weight=[]
day=[]
completeday=[]
banlanced120=[]
newscore100=[]
HEI100=[]

for i in range(len(data)):
    if data.iloc[i]['指标']=='减重值':
        reduce.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']=='减重百分比':
        percent.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '膳食纤维摄入量平均分':
        diefiber.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '饮食均衡得分(120分)':
        banlanced120.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '新饮食得分(100制)':
        newscore100.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '完整记录天数':
        completeday.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == 'HEI平均得分(100分)':
        HEI100.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '全谷类摄入量平均分':
        wholegrain.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '蔬菜摄入量平均分':
        veg.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '固态脂肪摄入量平均分':
        solidfat.append(data.iloc[i]['相关性'])

    if data.iloc[i]['指标'] == '普通日热量平均摄入值':
        f_totalheat2.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '普通日热量平均对比值':
        c_totalheat2.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '三大营养素碳水化合物平均对比值':
        f_nutrients1.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']== '精制谷物摄入量平均分':
        refinegrain.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '饮水量平均分':
        water.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '全谷类实际摄入平均量':
        f_wholegrain.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '乳类实际摄入平均量':
        f_milk.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '饮水平均量':
        f_water.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '膳食纤维实际摄入平均量':
        f_diefiber.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '水果实际摄入平均量':
        f_fruit.append(data.iloc[i]['相关性'])

    if data.iloc[i]['指标'] == '饮酒（酒精量，全天标准）平均分':
        alcohol.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '蔬菜实际摄入平均量':
        f_veg.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '鱼虾贝壳类及植物蛋白类摄入量平均分':
        fishshrimp.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']== '三大营养素组成平均分':
        nutrients.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '水果摄入量平均分':
        fruit.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '钠盐实际摄入平均量':
        f_salt.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']== '记录天数':
        day.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '乳类摄入量平均分':
        milk.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '添加糖摄入量平均分':
        sugar.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '总热量摄入量平均分':
        totalheat.append(data.iloc[i]['相关性'])

    if data.iloc[i]['指标']== '鱼虾贝壳类及植物蛋白类实际摄入平均量':
        f_fishshrimp.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']== '初始体重值':
        weight.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '总蛋白实际摄入平均量':
        f_totalprotein.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']== '轻食日热量平均摄入值':
        f_totalheat1.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '三大营养素蛋白质平均对比值':
        f_nutrients3.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']== 'BMI':
        bmi.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']== '轻食日热量平均对比值':
        c_totalheat1.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']== '精制谷物摄入平均量':
        f_refinegrain.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '不饱和与饱和脂肪酸摄入平均对比值':
        f_fattyacids.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']== '饮酒实际摄入平均量':
        f_alcohol.append(data.iloc[i]['相关性'])

    if data.iloc[i]['指标'] == '固态脂肪实际摄入平均量':
        f_solidfat.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标']== '添加糖实际摄入平均量':
        f_sugar.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '钠盐摄入量平均分':
        salt.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '年龄':
        age.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '不饱和与饱和脂肪酸摄入比平均分':
        fattyacids.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '总蛋白摄入量平均分':
        totalprotein.append(data.iloc[i]['相关性'])
    if data.iloc[i]['指标'] == '三大营养素脂肪平均对比值':
        f_nutrients2.append(data.iloc[i]['相关性'])

dataframe=pd.DataFrame({'减重值':reduce,'减重百分比':percent,'膳食纤维摄入量平均分':diefiber,'饮食均衡得分(120分)':banlanced120,
'新饮食得分(100制)':newscore100,'完整记录天数':completeday,'HEI平均得分(100分)':HEI100,'蔬菜摄入量平均分':veg,'固态脂肪摄入量平均分':solidfat,
'全谷类摄入量平均分':wholegrain,'普通日热量平均摄入值':f_totalheat2,'普通日热量平均对比值':c_totalheat1,'三大营养素碳水化合物平均对比值':f_nutrients1,
'精制谷物摄入量平均分':refinegrain,'饮水量平均分':water,'全谷类实际摄入平均量':f_wholegrain,'乳类实际摄入平均量':f_milk,'饮水平均量':f_water,
'膳食纤维实际摄入平均量':f_diefiber,'水果实际摄入平均量':f_fruit,'饮酒（酒精量，全天标准）平均分':alcohol,'蔬菜实际摄入平均量':f_veg,
'鱼虾贝壳类及植物蛋白类摄入量平均分':fishshrimp,'三大营养素组成平均分':nutrients,'水果摄入量平均分':fruit,'钠盐实际摄入平均量':f_salt,
'记录天数':day,'乳类摄入量平均分':milk,'添加糖摄入量平均分':sugar,'总热量摄入量平均分':totalheat,'鱼虾贝壳类及植物蛋白类实际摄入平均量':f_fishshrimp,
'初始体重值':weight,'总蛋白实际摄入平均量':f_totalprotein,'轻食日热量平均摄入值':f_totalheat1,'三大营养素蛋白质平均对比值':f_nutrients3,
'BMI':bmi,'轻食日热量平均对比值':c_totalheat1,'精制谷物摄入平均量':f_refinegrain,'不饱和与饱和脂肪酸摄入平均对比值':f_fattyacids,
'饮酒实际摄入平均量':f_alcohol,'固态脂肪实际摄入平均量':f_solidfat,'添加糖实际摄入平均量':f_sugar,'钠盐摄入量平均分':salt,'年龄':age,
'不饱和与饱和脂肪酸摄入比平均分':fattyacids,'总蛋白摄入量平均分':totalprotein,'三大营养素脂肪平均对比值':f_nutrients2})

#重新设置DataFrame的index名称
dataframe.index = pd.Series(['第一周','第二周','第三周','第四周','第五周'])
#数据行列转值
dataframe=dataframe.T

"""
week=[1,2,3,4,5]
plt.rcParams['font.sans-serif']=[u'SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.title('各指标随时间相关性变化')
plt.xlabel('周数')
plt.ylabel('MultipleR值')
plt.plot(week,newscore100, label='新饮食得分(100制)',marker='o')
plt.plot(week,banlanced120,  label='饮食均衡得分(120分)',marker='o')
plt.plot(week,HEI100,label='HEI平均得分(100分)',marker='o')
plt.legend()
# 设置数字标签
#for a, b in zip(week, newscore100):
#    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.savefig('/Users/martin_yan/Desktop/test.png', dpi=300)
plt.show()
"""


dataframe.to_excel('/Users/martin_yan/Desktop/33333.xlsx', index=True, encoding="utf_8_sig")

