# Wheat-Health

环境配置

本代码需要运行在python3.6环境下，运行前需要安装以下常用的python第三方库 pandas,numpy,matplotlib,seaborn和sklearn。

代码结果如下:

Wheat-Health---WheatGreen|---correlation.py
            |            |---modifycriterion.py
            |            |---preprocessing.py
            |            |---seekweight.py
            |
            |
            ---BabyMother|---babymother.py
            |            |---babymother_mean.py
            |            |---correlation2.py
            |            |---findlatestweight.py
            |            |---groupwithweight.py
            |            |---numbermeal.py
            |            |---prediction.py
            |            |---test.py
            |
            |
            ---data|---all data for this project


----> preprocessing.py : 读取多个csv文件中的数据进行预处理操作，

将RF属性中的16项子属性如：'水果摄入量'，'蔬菜摄入量'等展开作为新属性列.

运行后将生成两个新的csv文件:1.data.csv包括用户每日实际摄入量及每一项得分及总分。2.mean_data.csv包括每个用户的平均各项得分。


----> correlation.py : 读取mean_data.csv对数据做相关性分析，主要包括一元相关性分析和多元相关性分析。

分析各项营养指标的实际摄入量和平均得分及用户平均总得分对减重、减重百分比及BMI和年龄的相关性，利用的是pearson相关系数。

代码如下:

#corr = data.corr()

利用matplotlib和seaborn绘制热力图heatmap及一元线图和多元剖面图。

注意：如果matplotlib作图出现中文乱码问题，请参照以下链接解决问题：

https://blog.csdn.net/sinat_33027857/article/details/78072292


-----> modifycriterion.py : 更改为新的评分标准。

水果摄入量，蔬菜摄入量，膳食纤维摄入量，固态脂肪摄入量，钠盐摄入量（共五项）分别从5分->10分。提升。

而三大营养素，饮酒和添加糖（共三项）分别从10分->5分。下降。

总分从120分变为130分。更改后的data命名为:new_num。

-----> seekweight.py : 寻找热量评分和其余各营养素评分的合理权重。

对除热量得分外的其余分数记为balanced。然后将balanced除以12，归为总分10分和热量总分一样。

设置权重因子，grid search 搜索最大相关性的值。

-----> prediction.py : 预测用户的平均得分，减重值等数据。利用线性回归函数做预测。

使用RMSE值评估模型误差。PCA降低数据维度。核心代码如下：

#pca = PCA(n_components='mle')

#pca.fit(pre_data)

#X_pca=pca.fit_transform(pre_data)

#print(pca.explained_variance_ratio_)

-----> babymother.py : 将读取的宝妈营数据文件csv中rf列的16项子属性展开，并计算出每人每日的总得分。

这里的评分标准目前还是老标准（110+10分）。

-----> babymother_mean.py : 计算出每人的各营养素的平均量及各营养素的平均得分，以及目前的平均总得分。

和用户信息表2做关于姓名的连接，合并表。生成文件mean_babymother_data。

-----> correlation2.py : 读取mean_babymother_data, 做减重值、BMI对分数的相关性分析。


-----> groupwithweight.py : 增加user的初始体重和减重百分比列。

将用户根据BMI分为AB组(大于24或小于等于24),计算每个用户每天和初始体重的差值、每天与上一日差值。

将用户的得分分为AB组(大于84分或小与等于84分),计算每个用户每天和初始体重差值、每天与上一日差值。

用BMI和减重大小分为4组，看数据的分布。

-----> findlatestweight.py : 找到用户目前最新的体重值。并记录下用户的身高数据为计算BMI做准备。


-----> numbermeal.py : 统计出用户到目前为止记录完整三餐情况的天数。并将结果写入到babymother_completedata中。


LOG:

5.22 读取一个用户的数据，对数据扩展变形处理，输出为data_num.csv。

5.23 读取全部的用户数据，将用户数据整理到一个data.csv（包括用户每日的饮食摄入量及得分等数据）。

做各营养指标对减重等指标一元线性分析。

利用matplotlib绘制热力图。增加考虑饮食摄入的实际值，去重复数据遇到bug，已解决。

5.24 增加一元线性回归部分回归线图，做二元及多元线性回归分析及绘制剖面图。

对营养指标的平均得分做归一化处理，在mean_data中增加平均总得分。

更改打分标准，对原数据的打分进行更改。观察分析。

改变前：平均总分对减重的相关性为0.3907。改变后变为：0.42，有所改善。

但是评分标准的改变和归一化处理对各营养小分和减重，减重百分比，BMI指标的相关性不产生影响。

原因是这两种改变并不改变数据内部的差异，等比例变化，不影响相关性。

5.25 寻找目前新标准评分下热量得分（1项）和均衡得分（15项）的合理权重值。

但是，搜索找不到凸点收敛值。

分析：1.数据量太小，就目前的数据下无法搜索到。2.划分不合理，改变均衡和热量的划分方法。

5.29 预测减重值，减重百分比，平均得分等属性。但是因为数据量小，误差大。

5.30 对宝妈营用户数据进行清洗，生成mother_data及mean_babymother_data。

对清洗后的数据做相关性分析。

5.31 增加原始体重和减重百分比列。

Tableau可视化数据分析AB组用户不同时间段的减重绝对值情况。

更改数据为新的标准评分标准，找各指标与减重值、减重百分比的相关性。

6.1 用BMI分组，计算每个用户每日与上一日的体重差值，并用Tableau绘制图。

增加用户筛选条件，筛选出用户记录7天及以上的有效记录数据。

用分数分组，计算每个用户每日与初始体重差值以及与上一日体重差值。

以BMI和减重绝对值分为四组，看数据的分布情况。

6.4 PCA降低数据维度，和原始维度准确性比较下降。

#调用estimator的score缺省函数，对分类器对应于准确率为sklearn.metrics.accuracy_score

对回归器对应于R2得分sklearn.metrics.r2_score

6.5 对一周的数据5.30-6.4做预处理和清洗。

增加年龄新属性到babymother_completedata5.22-6.4.csv。

6.6 分析各项和减重绝对值、减重百分比之间的相关性。

增加记录次数，统计出用户完整记录三餐的天数。

统计出用户第一周减重值和第二周减重值及累积减重值。

以BMI和年龄分四组，探究不同组别的平均得分和减重值的情况。

