import matplotlib
import matplotlib.pyplot as plt

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 显示饼图
def pie_chart(size,label,title):
    plt.figure() # 绘制画布
    plt.pie(size,labels=label,labeldistance=1.05,autopct='%1.2f%%',shadow=True,startangle=0,pctdistance=0.6)
    plt.axis('equal')
    plt.title(title,fontsize=12)
    plt.legend(bbox_to_anchor=(0.03,1))
    plt.show()


# 绘制折线图
def broken_line(y,y_pred,title):
    plt.figure()
    plt.plot(y,color='r',marker='o',label='真实房价')
    plt.plot(y_pred,color='b',marker='*',label="预测房价")
    plt.title(title)
    plt.xlabel('房子数量')
    plt.ylabel('房子总价')
    plt.grid()
    plt.show()


# 绘制条形图
def average_price_bar(x,y,title):
    plt.figure()
    plt.bar(x,y,alpha=0.8)
    plt.xlabel('区域')
    plt.ylabel('均价')
    plt.title(title)
    for x,y in enumerate(y):
        plt.text(x,y+100,y,ha='center')
    plt.show()

# 绘制全市二手房装修程度条形图
def renovation_bar(x,y,title):
    plt.figure()
    plt.bar(x,y,alpha=0.8)
    plt.xlabel('装修类型')
    plt.ylabel('数量')
    plt.title(title)
    for x,y in enumerate(y):
        plt.text(x,y+100,y,ha='center')
    plt.show()


# 绘制热门户型均价条形图
def bar(price,type,title):
    plt.figure()
    plt.barh(type, price, height=0.3, color='r', alpha=0.8)
    plt.xlim(0, 15000)
    plt.xlabel('均价')
    plt.title(title)
    for y, x in enumerate(price):
        plt.text(x + 10, y , str(x) + '元')
    plt.show()
