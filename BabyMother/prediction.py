import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier,GradientBoostingRegressor,AdaBoostClassifier
from sklearn.svm import SVR
from sklearn.kernel_ridge import KernelRidge
from xgboost import XGBRegressor


train=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.25(总表／实际记录平均分).csv')

#选取部分属性作为预测标准
predictors=['记录天数','平均得分','完整记录天数','膳食纤维摄入量平均分','蔬菜摄入量平均分','固态脂肪摄入量平均分','水果摄入量平均分',
'精制谷物摄入量平均分','全谷类摄入量平均分','总热量摄入量平均分','鱼虾贝壳类及植物蛋白类摄入量平均分','饮水量平均分','不饱和与饱和脂肪酸摄入平均对比值',
'不饱和与饱和脂肪酸摄入比平均分','初始体重值','BMI','三大营养素蛋白质平均对比值','总蛋白摄入量平均分','乳类摄入量平均分','三大营养素碳水化合物平均对比值',
'三大营养素组成平均分','轻食日热量平均对比值','轻食日热量平均摄入值','添加糖摄入量平均分','普通日热量平均对比值',
'年龄','钠盐摄入量平均分','三大营养素脂肪平均对比值','饮酒（酒精量，全天标准）平均分']

#找出存在nan的行号
#print(np.where(np.isnan(train['体重']))[0])
#根据行号去删除某些行
#train.drop([2,12] ,axis=0, inplace=True)

target=train['减重值']
x_train, x_test, y_train, y_test = train_test_split(train[predictors], target, test_size=.05)
lr=linear_model.LinearRegression()
model = lr.fit(x_train, y_train)
predictions=model.predict(x_test)
print(predictions)
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

