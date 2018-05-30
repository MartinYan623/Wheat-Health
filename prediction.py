import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier,GradientBoostingRegressor,AdaBoostClassifier
from sklearn.svm import SVR
from sklearn.kernel_ridge import KernelRidge
from xgboost import XGBRegressor

train=pd.read_csv('/Users/martin_yan/Desktop/mean_data.csv')
#train_data, test_data = cv.train_test_split(df, test_size=0.2)
#选取部分属性作为预测标准
predictors=['BMI','水果实际摄入平均量','水果摄入量平均分','蔬菜实际摄入平均量','蔬菜摄入量平均分','全谷类实际摄入平均量','全谷类摄入量平均分'
,'添加糖摄入量平均分','钠盐实际摄入平均量','精制谷物摄入量平均分','乳类实际摄入平均量','不饱和与饱和脂肪酸实际摄入平均量','总蛋白实际摄入平均量',
'膳食纤维实际摄入平均量','固态脂肪摄入量平均分','总热量实际摄入平均量','饮酒实际摄入平均量','不饱和与饱和脂肪酸摄入比平均分','全谷类实际摄入平均量','全谷类摄入量平均分']
target=train['减重值']
x_train, x_test, y_train, y_test = train_test_split(train[predictors], target, random_state=42, test_size=.1)
lr = linear_model.LinearRegression()
model = lr.fit(x_train, y_train)
predictions=model.predict(x_test)
print(predictions)
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

