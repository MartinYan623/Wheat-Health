import pandas as pd
encoding='UTF-8'
import numpy as np
data=pd.read_csv('/Users/martin_yan/Desktop/babymother_completedata5.22-6.4.csv')
#对年龄进行分段
def numerical_to_categorical(data, attr, val_map):
    result = data.copy(deep=True)
    for the_map in val_map:
        lower = the_map['lower']
        upper = the_map['upper']
        val = the_map['val']
        result.loc[np.logical_and(
            data[attr] >= lower, data[attr] < upper), attr] = val
    return result

# discretize age
age_map = [
    {'lower': 20, 'upper': 30, 'val': 1},
    {'lower': 30, 'upper': 40, 'val': 2},
    {'lower': 40, 'upper': 50, 'val': 3},
]
data = numerical_to_categorical(data, '年龄', age_map)
print(data)
data.to_csv('/Users/martin_yan/Desktop/1.csv', index=False, encoding="utf_8_sig")