import pandas as pd
from sklearn.preprocessing import LabelEncoder  # 用于标签编码，将类别数据转化为数值型数据
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler  # 用于数据标准化
from sklearn.cluster import KMeans  # 用于KMeans聚类分析
from MyWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
# 读取CSV文件
frame = pd.read_csv('./data/Depression_Students.csv', encoding='gbk')

# 数据转换，将字符串标记转换成可以计算的数字
coder = LabelEncoder()  # 创建LabelEncoder实例，用于标签编码
# 将“是否有过自杀的念头”，“精神疾病家族史”，“是否抑郁”，“饮食习惯”这几列的字符串标记转换为数字
frame[['是否有过自杀的念头','精神疾病家族史','是否抑郁']] = frame[['是否有过自杀的念头','精神疾病家族史','是否抑郁']].apply(coder.fit_transform)

# 将时间转换成数字
def time_to_hours(time_str):
    """将睡眠时间的字符串转换为数值型的小时数"""
    if "hours" in time_str:
        if "More than" in time_str:
            return 8.5  # 如果时间描述为“More than”，则返回8.5小时
        elif "Less than" in time_str:
            return 4.5  # 如果时间描述为“Less than”，则返回4.5小时
        elif "-" in time_str:
            # 如果时间格式为“X-Y hours”，计算其平均值
            start, end = time_str.split("-")
            return (float(start) + float(end.split(' ')[0])) / 2
    return None  # 如果格式不正确，返回None

frame['睡眠时间'] = frame['睡眠时间'].apply(time_to_hours)  # 将“睡眠时间”列应用上述转换函数
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为“SimHei”，以支持中文显示


# 绘制学习压力与抑郁的关系
def xxyl():
    # 过滤掉“精神疾病家族史”列为0的行，并选择“学习压力”和“是否抑郁”这两列
    data = frame.loc[frame['精神疾病家族史'] == 0, ['学习压力', '是否抑郁']]
    result = data.groupby('学习压力').agg('sum')  # 按学习压力分组，计算“是否抑郁”的总和
    fig, ax = plt.subplots()  # 创建图形和坐标轴对象
    # 绘制学习压力与抑郁关系的折线图
    ax.plot(result.index, result['是否抑郁'], label='是否抑郁', linewidth=5, marker='o', alpha=0.5)
    plt.title('学习压力与抑郁的关系', fontsize=18, fontweight='bold', color='darkblue')  # 设置标题
    plt.xlabel('学习压力压力', fontsize=14)  # 设置x轴标签
    plt.ylabel('抑郁数量', fontsize=14)  # 设置y轴标签
    plt.legend()  # 显示图例
    plt.show()  # 显示图表



# 绘制抑郁与各项指标的关系
def yysx():
    # 过滤掉“精神疾病家族史”列为0的行，并选择“学习压力”，“是否抑郁”，“经济压力”，“学习满意度”这些列
    data = frame.loc[frame['精神疾病家族史'] == 0, ['学习压力', '是否抑郁', '经济压力', '学习满意度']]
    result = data.groupby('是否抑郁').agg('mean')  # 按是否抑郁分组，计算其他列的平均值
    # 绘制条形图，分别使用不同的颜色表示两种“是否抑郁”的情况
    ax = result.plot(kind='bar', color=['skyblue', 'lightgreen'], edgecolor='black')
    plt.title('抑郁与各项指标的关系', fontsize=18, fontweight='bold', color='darkblue')  # 设置标题
    plt.xlabel('是否抑郁', fontsize=14)  # 设置x轴标签
    plt.ylabel('平均值', fontsize=14)  # 设置y轴标签
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # 在y轴方向显示虚线网格
    plt.show()  # 显示图表

# 绘制抑郁与自杀念头的年龄关系
def nlfb():
    # 选择需要的列：“是否抑郁”，“是否有过自杀的念头”，“年龄”
    data = frame.loc[:, ['是否抑郁', '是否有过自杀的念头', '年龄']]
    result = data.groupby('年龄').agg('mean')  # 按年龄分组，计算“是否抑郁”和“是否有过自杀的念头”的平均值
    # 创建一个图形和坐标轴对象，设置图形的大小
    fig, ax = plt.subplots()
    # 绘制两条线，分别表示“是否抑郁”和“是否有过自杀的念头”
    ax.plot(result.index.astype(str) + '岁', result['是否抑郁'], label='是否抑郁', color='skyblue', linewidth=2)
    ax.plot(result.index.astype(str) + '岁', result['是否有过自杀的念头'], label='是否有过自杀的念头', color='orange', linewidth=2)
    # 填充颜色区域，突出显示数据趋势
    ax.fill_between(result.index.astype(str) + '岁', result['是否抑郁'], alpha=0.3, color='skyblue')
    ax.fill_between(result.index.astype(str) + '岁', result['是否有过自杀的念头'], alpha=0.3, color='orange')
    plt.title('抑郁与自杀念头的年龄关系', fontsize=18, fontweight='bold', color='darkblue')  # 设置标题
    plt.xlabel('年龄', fontsize=14)  # 设置x轴标签
    plt.ylabel('平均值', fontsize=14)  # 设置y轴标签
    plt.grid(True, linestyle='--', alpha=0.3)  # 显示网格，增加可读性
    plt.legend()  # 显示图例
    plt.show()  # 显示图表

# 绘制经济压力与抑郁的关系
def jjyl():
    # 过滤掉“精神疾病家族史”列为0的行，并选择“经济压力”和“是否抑郁”这两列
    data = frame.loc[frame['精神疾病家族史'] == 0, ['经济压力', '是否抑郁']]
    result = data.groupby('经济压力').agg('sum')  # 按经济压力分组，计算“是否抑郁”的总和
    fig, ax = plt.subplots()  # 创建图形和坐标轴对象
    # 绘制经济压力与抑郁关系的折线图
    ax.plot(result.index, result['是否抑郁'], label='是否抑郁', color='coral', linewidth=5, marker='o', alpha=0.5)
    plt.title('经济压力与抑郁的关系', fontsize=18, fontweight='bold', color='darkblue')  # 设置标题
    plt.xlabel('经济压力', fontsize=14)  # 设置x轴标签
    plt.ylabel('抑郁数量', fontsize=14)  # 设置y轴标签
    plt.legend()  # 显示图例
    plt.show()  # 显示图表


def ysxg():
    # 筛选数据
    data = frame.loc[frame['精神疾病家族史'] == 0, ['饮食习惯', '是否抑郁', '是否有过自杀的念头']]
    
    # 按饮食习惯分组并计算平均值
    result = data.groupby('饮食习惯').agg('mean')[::-1]
    
    # 创建图形
    fig, ax = plt.subplots()
    
    # 绘制折线图
    result.plot(kind='line', marker='o', linewidth=2, ax=ax, color=['skyblue', 'lightgreen', 'salmon'])
    
    # 添加标题和标签
    plt.title('不同饮食习惯与抑郁症和自杀念头的关系', fontsize=18, fontweight='bold', color='darkblue')
    plt.xlabel('饮食习惯', fontsize=14)
    plt.ylabel('平均值', fontsize=14)
    
    # 设置网格线
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 设置 y 轴标签的字体大小
    plt.yticks(fontsize=12)
    
    # 设置图例
    plt.legend(title='指标', title_fontsize='13', fontsize=12, loc='best')
    
    # 显示图表
    plt.tight_layout()
    plt.show()




# KMeans聚类分析
def jl():
    # 将数据转换为DataFrame，避免修改原始数据
    df = frame.copy()
    
    # 特征选择：选择需要聚类的特征
    features = ['年龄', '学习压力', '学习满意度', '睡眠时间', '学习时间', '经济压力']

    # 提取特征数据
    X = df[features]
    
    # 对数据进行标准化处理
    scaler = StandardScaler()  # 初始化标准化工具
    X_scaled = scaler.fit_transform(X)  # 标准化数据

    # 初始化KMeans聚类算法，将数据分为3个簇
    kmeans = KMeans(n_clusters=3, random_state=300)
    df['Cluster'] = kmeans.fit_predict(X_scaled)  # 根据聚类结果，将聚类标签添加到数据中

    # 绘制每个聚类的散点图
    for cluster_id in df['Cluster'].unique():  # 遍历每个聚类
        # 获取当前聚类的数据
        cluster_data = df[df['Cluster'] == cluster_id]
        
        # 创建图形
        plt.figure()
        
        # 绘制散点图，显示每个聚类的年龄与学习压力的关系
        plt.scatter(cluster_data['年龄'], cluster_data['学习压力'], label=f'Cluster {cluster_id}', s=100, alpha=0.4)
        
        # 设置标题与标签
        plt.title(f'聚类 {cluster_id} 的数据分布', fontsize=16)
        plt.xlabel('年龄', fontsize=12)
        plt.ylabel('学习压力', fontsize=12)
        
        # 显示图例和网格
        plt.legend()
        plt.grid(True)
        
        # 调整图形布局并显示图表
        plt.tight_layout()
        plt.show()


class MyWin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect()
    
    def closeEvent(self, event):
        sys.exit()
    
    def connect(self):
        self.toolButton.clicked.connect(xxyl)
        self.toolButton_2.clicked.connect(yysx)
        self.toolButton_3.clicked.connect(nlfb)
        self.toolButton_4.clicked.connect(jjyl)
        self.toolButton_5.clicked.connect(ysxg)
        self.toolButton_6.clicked.connect(jl)
app = QApplication([])
win = MyWin()
win.show()
app.exec()
