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


train=pd.read_csv('/Users/martin_yan/Desktop/mean_babymother_data5.22-6.18.csv')

#选取部分属性作为预测标准
predictors=['精制谷物摄入量平均分','平均得分','蔬菜摄入量平均分','固态脂肪摄入量平均分','膳食纤维摄入量平均分','初始体重值','BMI','全谷类实际摄入平均量',
'完整记录天数','不饱和与饱和脂肪酸实际摄入平均量','水果实际摄入平均量','水果摄入量平均分','全谷类摄入量平均分','记录天数','添加糖摄入量平均分',
'不饱和与饱和脂肪酸摄入比平均分','鱼虾贝壳类及植物蛋白类摄入量平均分','饮水平均量','饮水量平均分','饮酒（酒精量，全天标准）平均分','总蛋白实际摄入平均量',
'鱼虾贝壳类及植物蛋白类实际摄入平均量','乳类实际摄入平均量','乳类摄入量平均分','总蛋白摄入量平均分','总热量摄入量平均分','膳食纤维实际摄入平均量',
'三大营养素实际摄入平均量','总热量实际摄入平均量','蔬菜实际摄入平均量','三大营养素组成平均分','钠盐实际摄入平均量','年龄','添加糖实际摄入平均量',
'饮酒实际摄入平均量','钠盐摄入量平均分','固态脂肪实际摄入平均量','精制谷物摄入平均量']

#找出存在nan的行号
#print(np.where(np.isnan(train['体重']))[0])
#根据行号去删除某些行
#train.drop([2,12] ,axis=0, inplace=True)

target=train['减重值']
x_train, x_test, y_train, y_test = train_test_split(train[predictors], target, test_size=.1)
lr=linear_model.LinearRegression()
model = lr.fit(x_train, y_train)
predictions=model.predict(x_test)
print(predictions)
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

