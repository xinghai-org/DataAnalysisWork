import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MaxNLocator

# 设置全局字体和负号显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
matplotlib.rcParams['axes.unicode_minus'] = False   # 解决负号显示问题

class DataAnalysis:
    def __init__(self):
        self.data = pd.read_excel('./data/员工离职分析.xlsx')

    # 工资和离职的关系
    def gongzi_lzl(self):
        frame = self.data.loc[self.data['离职'] == 1, ['工资', '离职']]
        result = frame.groupby('工资').size().to_dict()
        x = ['低', '中', '高']
        y = [result.get(i, 0) for i in x]
        
        # 绘制柱状图
        plt.figure(figsize=(8, 6))
        plt.bar(x, y, color=['#FF6F61', '#6B8E23', '#4682B4'], alpha=0.8)
        plt.xlabel('工资等级', fontsize=14)
        plt.ylabel('离职数量', fontsize=14)
        plt.title('工资与离职的关系', fontsize=16)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

    # 工资与其他指标的关系
    def yxgz(self):
        data = self.data
        a = data.groupby('工资')['考核得分'].mean().to_list()
        b = data.groupby('工资')['工龄'].mean().to_list()
        c = data.groupby('工资')['满意度'].mean().to_list()
        result = [[a[i], b[i], c[i]] for i in [1, 0, 2]]
        
        # 设置柱状图参数
        plt.figure(figsize=(10, 6))
        w = 0.25
        x_positions = [1, 2, 3]
        plt.bar([x - w for x in x_positions], result[0], width=w, color='#FF7F50', label='考核得分', alpha=0.8)
        plt.bar(x_positions, result[1], width=w, color='#87CEFA', label='工龄', alpha=0.8)
        plt.bar([x + w for x in x_positions], result[2], width=w, color='#9370DB', label='满意度', alpha=0.8)
        
        plt.xlabel('工资等级', fontsize=14)
        plt.ylabel('平均值', fontsize=14)
        plt.title('工资与各项指标关系', fontsize=16)
        plt.xticks(x_positions, ['低', '中', '高'], fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

    # 工资与工程数量及离职的关系
    def gcsl(self):
        data = self.data[['工资', '工程数量', '离职']]
        result = data.groupby('工资').mean()

        plt.figure(figsize=(10, 6))
        result.plot(kind='bar', ax=plt.gca(), color=['#FFA07A', '#20B2AA'], alpha=0.8)
        plt.title('按工资分组的工程数量和离职率', fontsize=16)
        plt.xlabel('工资等级', fontsize=14)
        plt.ylabel('平均值', fontsize=14)
        plt.xticks(rotation=0, fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

    # 工龄与离职的关系
    def gongl(self):
        data = self.data[['工龄', '离职']]
        result = data.sort_values('工龄', ascending=False).groupby('工龄').mean()

        plt.figure(figsize=(12, 6))
        plt.plot(result.index.astype('str'), result['离职'], marker='o', color='#1E90FF', label='离职率', alpha=0.9)
        plt.fill_between(result.index.astype('str'), result['离职'], color='#87CEEB', alpha=0.3)
        plt.title('离职率按工龄分布', fontsize=16)
        plt.xlabel('工龄（年）', fontsize=14)
        plt.ylabel('离职率', fontsize=14)
        plt.xticks(fontsize=12, rotation=45)
        plt.yticks(fontsize=12)
        plt.legend(fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

    # 数据集建模和结果展示
    def sjsl(self):
        from sklearn.metrics import accuracy_score
        from sklearn.preprocessing import LabelEncoder
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        import numpy as np

        data = self.data.copy()
        data['工资'] = LabelEncoder().fit_transform(data['工资'])
        X = data.drop(columns=['离职'])
        y = data['离职']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)

        train_accuracy = accuracy_score(y_train, y_pred_train)
        test_accuracy = accuracy_score(y_test, y_pred_test)

        plt.figure(figsize=(12, 6))
        plt.scatter(np.arange(len(y_train)), y_train, color='#FF7F50', label='训练集真实值', alpha=0.7)
        plt.scatter(np.arange(len(y_train)), y_pred_train, color='#DC143C', marker='x', label='训练集预测值', alpha=0.8)
        plt.scatter(np.arange(len(y_train), len(y_train) + len(y_test)), y_test, color='#87CEEB', label='测试集真实值', alpha=0.7)
        plt.scatter(np.arange(len(y_train), len(y_train) + len(y_test)), y_pred_test, color='#1E90FF', marker='x', label='测试集预测值', alpha=0.8)
        
        plt.title('预测值与真实值比较', fontsize=16)
        plt.xlabel('样本索引', fontsize=14)
        plt.ylabel('离职状态', fontsize=14)
        plt.legend(fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

        print(f"训练集准确率: {train_accuracy:.2f}")
        print(f"测试集准确率: {test_accuracy:.2f}")
