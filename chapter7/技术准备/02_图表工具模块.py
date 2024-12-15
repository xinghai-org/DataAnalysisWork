import matplotlib
import matplotlib.pyplot as plt

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 显示饼图
def pie_chart(size,label,title):
    plt.figure() # 绘制画布
    plt.pie(size,labels=label,labeldistance=1.05,autopct='%1.2f%%')
    plt.title(title,fontsize=12)
    plt.show()

pie_chart([0.5,0.2,0.2,0.1],['a','b','c','d'],'haha') 