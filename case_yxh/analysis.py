import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
matplotlib.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题


class DataAnalysis:
    def __init__(self):
        self.data =  pd.read_excel('./data/员工离职分析.xlsx')

    # 工资和离职的关系
    def gongzi_lzl(self):
        frame = self.data.loc[self.data['离职']==1,['工资','离职']]
        result = frame.groupby('工资').size().to_dict()
        x = ['低','中','高']
        y = [result[i] for i in x]
        plt.xlabel('工资等级')
        plt.ylabel('离职数量')
        plt.title('工资与离职的关系')
        plt.bar(x,y)
        plt.show()

    def yxgz(self):
        data = self.data
        # 按工资等级查看考核得分的分布
        a = data.groupby('工资')['考核得分'].mean().to_list()
        # 工资与工龄的关系
        b = data.groupby('工资')['工龄'].mean().to_list()
        # 工资与满意度的关系
        c = data.groupby('工资')['满意度'].mean().to_list()
        # 按工资等级顺序（如 [1, 0, 2]）重新排序结果
        result = [[a[i], b[i], c[i]] for i in [1, 0, 2]]
        # 设置柱状图的宽度
        plt.figure()
        w = 0.2
        # X 轴的位置，分别为三组数据
        x_positions = [1, 2, 3]
        # 绘制三个数据组的柱状图
        plt.bar([x + w for x in x_positions], result[0], width=w, label='考核得分')
        plt.bar([x + 2 * w for x in x_positions], result[1], width=w, label='工龄')
        plt.bar([x + 3 * w for x in x_positions], result[2], width=w, label='满意度')
        # 添加标签和标题
        plt.xlabel('工资等级')
        plt.ylabel('值')
        plt.title('工资与各项指标关系')
        # 设置 X 轴刻度标签
        plt.xticks([x + w for x in x_positions], ['低', '中', '高'])
        # 添加图例
        plt.legend()
        # 显示图形
        plt.show()

    def gcsl(self):
        # 选择需要的列
        data = self.data[['工资', '工程数量', '离职']]

        # 按工资分组并计算工程数量和离职的总和
        result = data.groupby('工资').agg('mean')

        # 绘制并排柱状图
        result.plot(kind='bar', figsize=(8, 6))

        # 设置标题和标签
        plt.title('按工资分组的工程数量和离职总和')
        plt.xlabel('工资等级')
        plt.ylabel('总和')

        # 显示图形
        plt.show()

    def gongl(self):
        # 选择需要的列
        data = self.data[['工龄', '离职']]
        # 按工龄降序排序并进行分组计算均值
        result = data.sort_values('工龄', ascending=False).groupby('工龄').agg('mean')
        # 创建图形
        plt.figure(figsize=(10, 6))
        # 绘制线图
        plt.plot(result.index.astype('str') + '年', result['离职'], marker='o', color='tab:blue', label='离职均值')
        # 填充线下方的区域
        plt.fill_between(result.index.astype('str') + '年', result['离职'], color='skyblue', alpha=0.3)
        # 添加标题和标签
        plt.title('离职人数按工龄分布', fontsize=16)
        plt.xlabel('工龄', fontsize=14)
        plt.ylabel('离职率', fontsize=14)
        # 添加网格
        plt.grid(True)
        # 显示图例
        plt.legend()
        # 展示图形
        plt.tight_layout()  # 自动调整布局
        plt.show()


    def sjsl(self):
        import matplotlib.pyplot as plt
        from sklearn.metrics import accuracy_score
        import numpy as np

        data = self.data
        df = data.copy()

        # 数据预处理: 将非数值型数据转换为数值型
        from sklearn.preprocessing import LabelEncoder
        label_encoder = LabelEncoder()
        df['工资'] = label_encoder.fit_transform(df['工资'])

        # 特征和标签分离
        X = df.drop(columns=['离职'])  # 特征列
        y = df['离职']  # 标签列

        # 数据集划分，80%用于训练，20%用于测试
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # 创建随机森林模型
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        # 预测测试集和训练集
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)

        # 计算训练集和测试集准确率
        train_accuracy = accuracy_score(y_train, y_pred_train)
        test_accuracy = accuracy_score(y_test, y_pred_test)

        print(f"训练集准确率: {train_accuracy}")
        print(f"测试集准确率: {test_accuracy}")

        # 绘制结果
        plt.figure(figsize=(10, 6))

        # 绘制训练集的散点图（标记为红色）
        plt.scatter(np.arange(len(y_train)), y_train, color='red', label='训练集真实值')
        plt.scatter(np.arange(len(y_train)), y_pred_train, color='darkred', marker='x', label='训练集预测值')

        # 绘制测试集的散点图（标记为蓝色）
        plt.scatter(np.arange(len(y_train), len(y_train) + len(y_test)), y_test, color='blue', label='测试集真实值')
        plt.scatter(np.arange(len(y_train), len(y_train) + len(y_test)), y_pred_test, color='darkblue', marker='x', label='测试集预测值')

        # 添加图例
        plt.title('预测值')
        plt.xlabel('样本索引')
        plt.ylabel('离职 (源数据 vs 预测值)')
        plt.legend()
        
        # 显示准确率文本
        plt.text(len(y_train) // 2, 1.05, f"准确率: {train_accuracy:.2f}", color='red', fontsize=12, ha='center')
        plt.text(len(y_train) + len(y_test) // 2, 1.05, f"新的数据准确率: {test_accuracy:.2f}", color='blue', fontsize=12, ha='center')

        # 显示图形
        plt.tight_layout()
        plt.show()

        
