import sys # 导入sys模块
import pygame # 导入pygame模块
from util import btn
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter # 绘图模块格式化类
from util.TimeUtil import *   

# 读取文件内容
pi_table = pd.read_excel('.\data\停车场信息表.xlsx')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 停车时间分布
def sjfb():
    # 图表标题
    plt.title('停车时间分布图')
    # 设置x轴信息
    labels_x = ['1小时','2小时','3-5小时','6-10小时','11-12小时','12小时以上']
    # 获取表中数据判断车辆停车时间
    df1 = pi_table.loc[(pi_table['price']==3)] # 停车1小时
    df2 = pi_table.loc[(pi_table['price']==6)] # 停车2小时
    df3 = pi_table.loc[(pi_table['price']>6)&(pi_table['price']<=15)] # 停车3~5小时
    df4 = pi_table.loc[(pi_table['price']>15)&(pi_table['price']<=30)] # 停车6~10小时
    df5 = pi_table.loc[(pi_table['price']>30)&(pi_table['price']<=36)] # 停车11~12小时
    df6 = pi_table.loc[(pi_table['price']>36)] # 停车12小时以上
    # 停车各阶段数量
    y = [len(i) for i in [df1,df2,df3,df4,df5,df6]]
    plt.bar(labels_x,y)
    # 为每一个图形添加数值标签
    for x,y in enumerate(y):
        plt.text(x,y+30,str(y) + '台',ha='center')
    plt.show()

# 停车高峰所占比例
def tcgf():
    plt.title('停车高峰所占比例')
    labels_x = ['0-3点','3-6点','6-9点','9-12点','12-15点','15-18点','18-21点','21-00点']
    # 根据时间获取y轴数据
    kks = {}
    for i in range(0,24):
        index = str(i) if len(str(i)) > 1 else '0' + str(i)
        kks[f'kk{i}'] = pi_table[pi_table["timein"].str.contains(f"{index}:")]
    
    # 设置数据信息
    x = [(len(kks[f'kk{i*3}'])+len(kks[f'kk{i*3+1}'])+len(kks[f'kk{i*3+2}'])) for i in range(8)]
    # 设置饼图
    plt.pie(x,labels=labels_x,autopct='%1.1f%%')
    # 设置图例
    plt.legend(loc='upper right',fontsize=10,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)
    plt.show() # 显示图表


# 每周繁忙统计
def fmtj():
    # 获取列表中rps(车位剩余)列为0的所有数据
    fmdfs = pi_table.loc[pi_table['state']==1]
    # 转换数据为列表
    fmdfs = fmdfs.values
    # x轴数据
    WEEK = ['周一','周二','周三','周四','周五','周六','周日',]
    weeks = {
    'WEEK1':0,
    'WEEK2':0,
    'WEEK3':0,
    'WEEK4':0,
    'WEEK5':0,
    'WEEK6':0,
    'WEEK7':0,
    }

    # 循环列表，判断数据是星期几
    for fmdf in fmdfs:
        week_numbeer = get_week_numbeer(fmdf[1])
        if week_numbeer in [0,1,2,3,4,5,6,7]:
            weeks[f'WEEK{week_numbeer+1}'] += 1 
    # 数据信息
    WEEK_VALUE = list(weeks.values())
    plt.title('周繁忙统计')
    plt.pie(WEEK_VALUE,labels=WEEK,autopct='%1.1f%%') # 绘制饼图
    plt.axis('equal')
    # 显示图例
    plt.legend(loc='upper right',fontsize=10,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)
    plt.show()


# 月收入分析
def ysrfx():
    srdf = pi_table.loc[pi_table['state']==1]
    # 筛选每月数据
    kk1 = srdf[srdf['timeout'].str.contains('2018-01')]
    kk2 = srdf[srdf['timeout'].str.contains('2018-02')]
    kk3 = srdf[srdf['timeout'].str.contains('2018-03')]
    # 计算价格和
    price1 = kk1['price'].sum()
    price2 = kk2['price'].sum()
    price3 = kk3['price'].sum()
    # 设置x和y
    labels_x = ['1月','2月','3月']
    y = [price1,price2,price3]

    plt.bar(labels_x,y)
    # 为每一个图形加数值标签
    for x,y in enumerate(y):
        plt.text(x,y+300,str(y) + '元',ha='center')
    plt.xlabel('月份')
    plt.ylabel('元')
    # 设置标题
    plt.title('2018年1-3月收入分析-总收入:'+str(price1+price2+price3)+'元')
    plt.show()

# 每日接待车辆统计
def cljd():
    # 获取列表中车状态为1的数据
    tcdf = pi_table.loc[pi_table['state']==1]
    # 循环的开始和结束时间
    start = '2018-1-1'
    end = '2018-03-31'
    # 开始转换开始于结束时间
    datestart = datetime.datetime.strptime(start,r'%Y-%m-%d')
    dateend = datetime.datetime.strptime(end,r'%Y-%m-%d')
    VALUE = [] # 数据列表
    DATE = [] # 日期列表
    # 循环日期
    while datestart <= dateend:
        # 判断当前日期出车库的车辆多少
        kk = tcdf[tcdf['timeout'].str.contains(datestart.strftime(r'%Y-%m-%d'))]
        # 将日期添加到列表中
        DATE.append(datestart.strftime(r'%Y-%m-%d'))
        # 计算使用率并添加到列表
        VALUE.append(len(kk))
        # 按照天循环
        datestart += datetime.timedelta(days=1)
    # 绘制折线图
    plt.plot(DATE,VALUE)
    plt.xticks([]) # 隐藏x刻度，应为太多了
    plt.xlabel('2018-01-01~2018-03-31')
    plt.title('每日接待车辆统计')
    plt.show()

# 车位使用率
def lyl():
    tcdf = pi_table.loc[pi_table['state']==1]
    # 循环的开始和结束时间
    start = '2018-1-1'
    end = '2018-03-31'
    # 开始转换开始于结束时间
    datestart = datetime.datetime.strptime(start,r'%Y-%m-%d')
    dateend = datetime.datetime.strptime(end,r'%Y-%m-%d')
    VALUE = [] # 数据列表
    DATE = [] # 日期列表
    # 循环日期
    while datestart <= dateend:
        # 判断当前日期出车库的车辆多少
        kk = tcdf[tcdf['timeout'].str.contains(datestart.strftime(r'%Y-%m-%d'))]
        # 将日期添加到列表中
        DATE.append(datestart.strftime(r'%Y-%m-%d'))
        # 计算使用率并添加到列表
        yh = 100 - kk['rps'].mean()
        VALUE.append(yh)
        # 按照天循环
        datestart += datetime.timedelta(days=1)
    # 绘制折线图
    plt.plot(DATE,VALUE)
    # yticks格式转换为百分比
    def to_percent(temp,position):
        return '%1.0f' % (temp) + '%'
    # 格式化yticks
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    plt.xticks([]) # 隐藏x刻度，应为太多了
    plt.xlabel('2018-01-01~2018-03-31')
    plt.title('车位利用率')
    plt.show()



pygame.init() # 初始化game
size = width, height = 340, 260
# 定义颜色
WHITE = (255,255,255)
BLUE = (72,61,139)
# 显示窗口
screen = pygame.display.set_mode(size)

# 设置背景颜色
screen.fill(WHITE)
while True: # 建立一个死循环
    
    button1 = btn.Button(screen,(90,50),140,60,BLUE,WHITE,'停车分布',20)    # 创建停车分布按钮
    button2 = btn.Button(screen,(90,130),140,60,BLUE,WHITE,'停车高峰时间',20)    # 创建停车分布按钮
    button3 = btn.Button(screen,(90,210),140,60,BLUE,WHITE,'周繁忙统计',20)    # 创建周繁忙统计按钮
    button4 = btn.Button(screen,(250,50),140,60,BLUE,WHITE,'月收入分析',20)    # 创建月收入分析按钮
    button5 = btn.Button(screen,(250,130),140,60,BLUE,WHITE,'每日接待车辆',20)    # 创建每日接待车辆统计按钮
    button6 = btn.Button(screen,(250,210),140,60,BLUE,WHITE,'车位使用率',20)    # 创建车位使用率按钮
    # 绘制按钮
    button1.draw_button()
    button2.draw_button()
    button3.draw_button()
    button4.draw_button()
    button5.draw_button()
    button6.draw_button()
    # 刷新窗口
    pygame.display.update()

    for event in pygame.event.get():    # 遍历所有事件,事件包括鼠标移动，鼠标点击等都会被捕捉，每次循环都遍历一次事件
        if event.type == pygame.QUIT:   # 如果检测到事件的类型是退出，那么就执行退出窗口
            pygame.quit()   # 退出pygame
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 停车时间分布
            if 20 <= event.pos[0] and event.pos[0] <=90 + 70 and 20 <= event.pos[1] and event.pos[1] <= 50 + 30: # 只能根据位置判断按钮
                sjfb()
            elif 20 <= event.pos[0] and event.pos[0] <=90 + 70 and 100 <= event.pos[1] and event.pos[1] <= 130 + 30: # 只能根据位置判断按钮
                tcgf()
            elif 20 <= event.pos[0] and event.pos[0] <=90 + 70 and 180 <= event.pos[1] and event.pos[1] <= 210 + 30: # 只能根据位置判断按钮
                fmtj()
            elif 180 <= event.pos[0] and event.pos[0] <=250 + 70 and 20 <= event.pos[1] and event.pos[1] <= 50 + 30: # 只能根据位置判断按钮
                ysrfx()
            # 每日接待车辆统计
            elif 180 <= event.pos[0] and event.pos[0] <=250 + 70 and 100 <= event.pos[1] and event.pos[1] <= 130 + 30: # 只能根据位置判断按钮
                cljd()
            # 车位利用率
            elif 180 <= event.pos[0] and event.pos[0] <=250 + 70 and 180 <= event.pos[1] and event.pos[1] <= 210 + 30: # 只能根据位置判断按钮
                lyl()
            
            