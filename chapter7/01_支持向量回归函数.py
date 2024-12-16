from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.svm import LinearSVR
house = fetch_california_housing()
# print(dir(house))
# ['DESCR', 'data', 'feature_names', 'frame', 'target', 'target_names']

frame = pd.DataFrame(house.data,columns=house.feature_names)
# 数据集都是被标注过的，house.target就是他们对应的标签
frame.insert(0,'target',house.target)
# 数据标准化
data_mean = frame.mean()
data_std = frame.std()
data_train = (frame - data_mean) / data_std

x_train = data_train[house.feature_names].values # 特征数据
y_train = data_train['target'].values # 目标数据

# # 数据训练
linearsvr = LinearSVR(C=0.1)
# 通过值和被标注的标签训练模型
linearsvr.fit(x_train,y_train)
print(dir(linearsvr))

# 预测，并还原结果
# 数据标准化，这里不包含数据集里面的结果
x = ((frame[house.feature_names] - data_mean[house.feature_names]) / data_std[house.feature_names]).values
# 添加预测房价信息列
frame[u'y_pred'] =  linearsvr.predict(x) * data_std['target'] + data_mean['target']
print(frame[['target','y_pred']])