# DataAnalysisWork
数据分析期末作业

github地址：https://github.com/xinghai-org/DataAnalysisWork

## 项目目录结构

```
│  .gitignore
│  DataAnalysisWork.code-workspace
│  LICENSE
│  README.md
│  requirements.txt
│
├─chapter7
│  │  01_支持向量回归函数.py
│  │  chart.py
│  │  house_analisis.py
│  │  main.py
│  │  MainWindow.py
│  │  MainWindow.ui
│  │
│  ├─data
│  │      data.csv
│  │
│  └─img
│          MainWindow.py
│          图标-1.png
│          图标-2.png
│          图标-3.png
│          图标-4.png
│          图标-5.png
│          背景图.png
│
├─chapter8
└─chapter9
```

## 项目目录解释

- .gitignore	git的配置文件，不用管
-  DataAnalysisWork.code-workspace      vscode的配置文件，不用管
- LICENSE       MIT开源证书，允许任何人免费许可，以无限制方式处理项目副本
- README.md        这个文件就是你现在看到的这些说明
-  requirements.txt        存放运行这个项目所需要用到的python库,运行项目前需要用pip安装，后面会提到
- chapter7       第七章项目的文件路径
- chapter8       第八章项目的文件路径
- chapter9       第九章项目的文件路径

## 搭建项目环境

项目下载后，自行搭建python，进入项目根目录，输入以下命令安装必要的库

```
pip install -r .\requirements.txt
```



# 二手房数据分析预测系统

第七章目录结构

```
│  01_支持向量回归函数.py
│  chart.py
│  house_analisis.py
│  main.py
│  MainWindow.py
│  MainWindow.ui
│
├─data
│      data.csv
│
└─img
        MainWindow.py
        图标-1.png
        图标-2.png
        图标-3.png
        图标-4.png
        图标-5.png
        背景图.png
```

- 01_支持向量回归函数.py       这个是书本上提到的知识点，与项目没什么关系，不用管
- house_analisis.py        这个文件存放所有关于处理数据的函数，将数据读取出来，创建各种函数对数据进行分析，这里只有函数，也就是这些函数是给别的python文件调用的
- chart.py   这个里面也是只用各种函数，函数包括，输入参数，绘制折线图，输入参数，绘制条形图等等，也是给别的函数调用的
- MainWindows.ui       PyQt5的ui文件，这个是界面
- MainWindows.py       PyQt5的ui文件转换成的python代码文件，只有这个文件才能允许
- main.py         运行文件，这个文件通过调用`MainWindows.ui `,`chart.py `,`house_analisis.py`和整合这些文件里面的函数实现整体的运行逻辑
- data 这里里面就一个csv文件，这个csv文件就是项目要处理的源数据
- img       这里的图片是MainWindows.py 界面里面需要用到的图片

## 运行项目

打开`main.py`运行`main.py`

## main文件

main文件导入了以下模块

```python
import house_analisis # 数据分析函数集文件
import chart # 绘制图形的函数文件
from PyQt5.QtWidgets import QApplication,QMainWindow # pyqt需要的模块
from MainWindow import Ui_MainWindow # ui文件
```

在文件中定义了Main类

```python
class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 绑定按键函数
        self.button_connect()
```

- Main类旁边的括号不是参数，而是表示Main继承于`(QMainWindow,Ui_MainWindow)`这两个类，也就是说，Main类包含所有(QMainWindow,Ui_MainWindow)类里面的函数和方法
- `__init__`函数是一个特殊函数，当创建类为对象的时候，就会执行这个函数里的内容，所以这个函数常常用来初始化一些内容
- `super().__init__()`,运行父类的init方法，就是运行QMainWindow类的init方法，应为使用这个类也需要先初始化，不然会报错
- self.setupUi(self)，这个self表示自己，自己的setupUi函数，我们没有自己定义这个函数也可以使用，这是应为继承了`(QMainWindow,Ui_MainWindow)`这两个类，这个方法是`Ui_MainWindow`类里面的，应为我们继承了，所以可以直接调用

**self.button_connect()**函数内容

```
    # 将按钮绑定函数
    def button_connect(self):
        self.btn_1.triggered.connect(self.show_average_price)
        self.btn_2.triggered.connect(self.show_house_number)
        self.btn_3.triggered.connect(self.show_renovation)
        self.btn_4.triggered.connect(self.show_type)
        self.btn_5.triggered.connect(self.show_total_price)
```

这个函数里的`self.btn_*`是UiMainWindow类里面的属性，表示按钮，可以直接调用，每一句话的作用就是讲这些按钮绑定函数，只要点击按钮就执行函数

**class函数体**

```python
    # 显示各区二手房分析图
    def show_average_price(self):
        region,average_price = house_analisis.get_average_price()
        chart.average_price_bar(region,average_price,'各区二手房价分析')

    # 各区二手房数量所占比例
    def show_house_number(self):
        region,percentage = house_analisis.get_house_number()
        chart.pie_chart(percentage,region,'各区二手房数量所占比例')

    # 全市二手房装修程度分析
    def show_renovation(self):
        atype,number = house_analisis.get_renovation()
        chart.renovation_bar(atype,number,'全市二手房装修程度分析')
    
    # 热门户型均价分析
    def show_type(self):
        type,price = house_analisis.get_house_type()
        chart.bar(price,type,'热门户型均价分析')
    
    # 显示二手房预测图
    def show_total_price(self):
        true_price,forecast_price = house_analisis.get_price_forecast()
        chart.broken_line(true_price,forecast_price,'二手房价预测')
```

- 这些函数无一例外都被绑定到了按钮中，只要点击按钮就会执行对应的函数
- 函数都使用了`house_analisis`文件和`chart`文件里面的方法，每个函数的逻辑都一样，house_analisis用于数据分析，分析出来的结果返回给`chart`文件里面的函数绘制成图表显示
