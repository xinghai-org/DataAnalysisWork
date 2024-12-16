import pandas
from sklearn.svm import LinearSVR

# 读取csv文件
data = pandas.read_csv('data/data.csv')

# 删除默认的索引列
data.drop('Unnamed: 0',inplace=True,axis=1)

# 数据清洗,删除data数据中所有带有空值的行
data.dropna(axis=0,how='any',inplace=True)

# 数据转换，将需要计算的列转换成数值类型
data['单价'] = data['单价'].map(lambda d:d.replace('元/平米','')).astype(float)
# data['单价'] = data['单价'].str.replace('元/平米','').astype(float)
data['总价'] = data['总价'].map(lambda d:d.replace('万','')).astype(float)
# data['总价'] = data['总价'].str.replace('万','').astype(float)
data['建筑面积'] = data['建筑面积'].map(lambda p:p.replace('平米','')).astype(float)
# data['建筑面积'] = data['建筑面积'].str.replace('平米','').astype(float)

# 各区二手房价分析
def get_average_price():
    # 按照区域分组
    group = data.groupby('区域')
    # 获取各组内的均价
    average_price_group = group['单价'].mean()
    # 获取区域
    region = average_price_group.index
    # 获取区域对应的值
    average_price = average_price_group.values.astype(int)
    # 返回
    return region,average_price

# 获取各区房子数量比例
def get_house_number():
    group_number = data.groupby('区域').size() # 获取每个区的数量
    region = group_number.index # 获取区域
    numbers = group_number.values # 获取区域对应的数量
    percentage = numbers /numbers.sum() * 100 # 计算区域数量占总数的百分比数
    return region, percentage 

# 全市二手房装修程度对比
def get_renovation():
    group_renovation = data.groupby('装修').size()
    atype = group_renovation.index # 装修程度
    number = group_renovation.values # 装修程度对应的数量
    return atype,number

# 热门户型均价分析
def get_house_type():
    house_type_number = data.groupby('户型').agg(均价=('单价','mean'),总数=('单价','size'))# 按照户型分组,然后计算单价的品均值和数量
    sort_values = house_type_number.sort_values('总数',ascending=False)[:5] # 排序，降序,然后获取前五组数据，也就是热门数据
    return sort_values.index,sort_values.loc[:,'均价'].values.astype(int)

# 二手房价预测
def get_price_forecast():
    # 复制一份数据
    data_copy = data.copy()
    # 用正则表达式，将户型拆分成（室，厅，卫），并去除文字，转成数字类型
    data_copy[['室','厅','卫']] = data_copy['户型'].str.extract('(\d+)室(\d+)厅(\d+)卫').astype(float) # 正则表达式为'(\d+)室(\d+)厅(\d+)卫'，所以返回结果只有括号里的三个数字
    # 将数据中没有意义的数据删除，只保留有用的字段，这个过程叫做数据规约
    data_copy = data_copy[['总价','建筑面积','室','厅','卫']]
    # 数据清洗，去除所有空值,去除面积大于300的房子
    data_copy.dropna(axis=0,how='any',inplace=True)
    new_data = data_copy[data_copy['建筑面积'] < 300].reset_index(drop=True)
    

    # 添加自定义数据
    new_data.loc[2505] = [None,88.0,2.0,1.0,1.0]
    new_data.loc[2506] = [None,136.0,3.0,2.0,2.0]
    data_train=new_data.loc[0:2504]
    x_list = ['建筑面积','室','厅','卫'] # 自变量，就是最终结果是受这些数值影响的
    # 标准化
    data_mean = data_train.mean() #计算品均值
    data_std = data_train.std() # 计算标准差
    data_train = (data_train - data_mean) / data_std # 数据标准化 （数据-数据品均值）/ 数据标准差
    # 将特征数据和目标数据分开,训练模型
    x_train = data_train[x_list]
    y_train = data_train['总价'].values
    linearsvr = LinearSVR(C=0.1)
    linearsvr.fit(x_train,y_train)
    # 标准化特征数据，这个特征数据包含自定义的特征，所以需要重新标准化
    x = (new_data[x_list] - new_data[x_list].mean()) / new_data[x_list].std()
    # 添加预测房价信息列
    new_data['y_pred'] = linearsvr.predict(x) * data_std['总价'] + data_mean['总价'] # 根据原来的数据通过模型预测结果，相当于将训练集用作预测了
    y = new_data.loc[2490:,'总价'] # 获取真实的结果
    y_pred = new_data.loc[2490:,'y_pred'] # 获取预测的结果
    return y,y_pred
    
