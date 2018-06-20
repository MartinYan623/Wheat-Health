import pandas as pd
from sklearn import linear_model
from sklearn.decomposition import PCA

train=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.18.csv')
#选取部分属性作为预测标准
predictors=['精制谷物摄入量平均分','平均得分','蔬菜摄入量平均分','固态脂肪摄入量平均分','膳食纤维摄入量平均分','初始体重值','BMI','全谷类实际摄入平均量',
'完整记录天数','不饱和与饱和脂肪酸实际摄入平均量','水果实际摄入平均量','水果摄入量平均分','全谷类摄入量平均分','记录天数','添加糖摄入量平均分',
'不饱和与饱和脂肪酸摄入比平均分','鱼虾贝壳类及植物蛋白类摄入量平均分','饮水平均量','饮水量平均分','饮酒（酒精量，全天标准）平均分','总蛋白实际摄入平均量',
'鱼虾贝壳类及植物蛋白类实际摄入平均量','乳类实际摄入平均量','乳类摄入量平均分','总蛋白摄入量平均分','总热量摄入量平均分','膳食纤维实际摄入平均量',
'三大营养素实际摄入平均量','总热量实际摄入平均量','蔬菜实际摄入平均量','三大营养素组成平均分','钠盐实际摄入平均量','年龄','添加糖实际摄入平均量',
'饮酒实际摄入平均量','钠盐摄入量平均分','固态脂肪实际摄入平均量','精制谷物摄入平均量']

target=train['减重值']
pre_data=train[predictors]
#利用pca降低维度
pca = PCA('mle')
pca.fit(pre_data)
X_pca=pca.fit_transform(pre_data)
print(pca.explained_variance_ratio_)
lr=linear_model.LinearRegression()
lr=lr.fit(X_pca,target)
print ('利用PCA降维后的数据得到的准确率:%s' % lr.score(X_pca,target))
lr1 = linear_model.LinearRegression()
lr1=lr1.fit(pre_data,target)
print ('未做降维得到的准确率:%s' % lr1.score(pre_data,target))


