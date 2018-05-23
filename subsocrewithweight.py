import pandas as pd
import numpy as np
encoding='UTF-8'
data = pd.read_csv('/Users/martin_yan/Desktop/mean_data.csv')
data.drop(['用户编号', '记录天数'], inplace=True, axis=1)
numeric_features = data.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print (corr['减重值'].sort_values(ascending=False), '\n')
