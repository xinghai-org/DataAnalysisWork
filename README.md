# 1.   DataAnalysisWork
数据分析期末作业

github地址：https://github.com/xinghai-org/DataAnalysisWork

## 1. 1   项目目录结构

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

## 1.2    项目目录解释

- .gitignore	git的配置文件，不用管
-  DataAnalysisWork.code-workspace      vscode的配置文件，不用管
- LICENSE       MIT开源证书，允许任何人免费许可，以无限制方式处理项目副本
- README.md        这个文件就是你现在看到的这些说明
-  requirements.txt        存放运行这个项目所需要用到的python库,运行项目前需要用pip安装，后面会提到
- chapter7       第七章项目的文件路径
- chapter8       第八章项目的文件路径
- chapter9       第九章项目的文件路径

## 1.3    搭建项目环境

项目下载后，自行搭建python，进入项目根目录，输入以下命令安装必要的库

```
pip install -r .\requirements.txt
```



# 2.   二手房数据分析预测系统

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

## 2.1   运行项目

打开`main.py`运行`main.py`

## 2.2   main文件

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
- self.setupUi(self)，这个self表示自己，自己的setupUi函数，没有自己定义这个函数也可以使用，这是应为继承了`(QMainWindow,Ui_MainWindow)`这两个类，这个方法是`Ui_MainWindow`类里面的，应为继承了，所以可以直接调用

## 2.3   **button_connect**函数内容

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

## 2.4   **class函数体**

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



# 3.   抑郁症状因素分析系统

## 3.1    项目目录

```
│  main.py
│  MyWindow.py
│  MyWindow.qrc
│  MyWindow.ui
│  MyWindow_rc.py
│
├─data
│      Depression_Students.csv
│      result.csv
│
└─img
        bj.jpg
```

- main.py 主程序    用python运行就可进入程序
- myWindow.py    pyqt界面转成的py文件，这个文件会被main.py调用，作用就是显示ui界面
- MyWindow.qrc 这个是图片路径关系的文件，保存了ui文件和图片的路径关系
- MyWindow_rc.py    上面的qrc文件转成的py文件，也是为了能让python调用
- MyWindow.ui    ui页面文件，也就是窗口
- data/    这里放置的是要分析的csv数据
- img/    这里放置的是ui界面的背景图片

## 3.2    系统框架

### 3.2.1    Main.py 文件

python代码的主要结构如下

```
frame = pd.read_csv()

def xxyl()
def yysx()
def nlfb()
def jjyl()
def ysxg()
def jl()


class MyWin(QMainWindow,Ui_MainWindow)
	def __init__(self)
    def closeEvent(self, event)
    def connect(self)

app = QApplication([])
win = MyWin()
win.show()
app.exec()
```

- 项目首先使用pd.read_csv导入了csv文件，然后后面的代码都是对这个csv文件做处理分析
- 项目一共分为三个部分
- 第一个部分就是上面那6个函数，这六个函数的作用都是一样，就是获取csv文件，然后进行数据分析，然后将结果显示在图表中，通过弹窗的方式显示
- 第二个部分创建了MyWin类，这个类继承了ui文件，也就是页面文件，这个类的主要作用就是将ui文件里面的六个按钮和上面六个函数绑定在一起，当点击按钮的时候，就会运行对应的函数，分析对应的数据
- 第三个部分就是显示ui界面



## 3.3.1 **学习压力与抑郁的关系**

`对应的是xxyl()函数`

- 将学生按学习压力进行分组，并计算每组中“是否抑郁”的总和，绘制折线图

![image-20241223011712917](https://db.xinghai.ink/github_DataAnalysisWork/image-20241223011712917.png)

- 通过对数据的分析，结果表明，发现学习压力与抑郁症状之间存在显著的正相关关系，随着学习压力的增加，抑郁的发生率也显著上升。具体而言，处于高学习压力的学生群体，其抑郁症状更为明显。这一结论表明，学习压力是导致抑郁的重要因素，特别是在学业负担较重的群体中。因此，学校和相关心理健康机构应关注学生的学习压力，并采取相应措施帮助缓解。

## 2. **抑郁与各项指标的关系**

`对应yysx()函数`

进一步的分析揭示了抑郁症状与多个心理和环境因素之间的密切关系

- 通过按“是否抑郁”进行分组，计算学习压力、经济压力、学习满意度等指标的平均值，并绘制了条形图。

![image-20241223011938935](https://db.xinghai.ink/github_DataAnalysisWork/image-20241223011938935.png)

- 结果显示，抑郁群体的学习压力和经济压力普遍较高，而学习满意度较低。这意味着，较大的压力和较低的满意度可能是抑郁的潜在风险因素。因此，在预防和干预抑郁症的过程中，帮助学生降低压力和提高学习满意度将是非常重要的措施

## 3. **抑郁与自杀念头的年龄关系**

`对应nlfb()函数`

在分析抑郁症状与自杀念头的年龄关系时，发现随着年龄的增加，抑郁症状和自杀念头的发生率也有所上升。

- 通过对不同年龄段的数据进行分组，并计算每组中“是否抑郁”和“是否有过自杀的念头”的平均值

![image-20241223012213460](https://db.xinghai.ink/github_DataAnalysisWork/image-20241223012213460.png)

- 结果表明，年轻群体更容易出现抑郁，而中年群体更容易出现自杀念头。这一趋势提示，随着年龄的增长，学生可能会面临更为复杂的心理压力，可能由抑郁转向自杀，因此，心理健康干预应针对不同年龄段的学生群体进行差异化设计

## 4. **经济压力与抑郁的关系**

`对应jjyl()函数`

经济压力被发现是影响学生抑郁症状的重要因素之一

- 通过对学生按“经济压力”进行分组，并计算每组中“是否抑郁”的总和

![image-20241223012443986](https://db.xinghai.ink/github_DataAnalysisWork/image-20241223012443986.png)

- 分析结果表明，经济压力较大的群体抑郁症状的发生率显著较高。这意味着，经济压力不仅仅是个人生活质量的重要指标，也直接影响到学生的心理健康。因此，在解决学生的抑郁问题时，除了关注学习压力外，经济压力也是不容忽视的重要因素

## 5. **饮食习惯与抑郁症和自杀念头的关系**

`对应ysxg()函数`

饮食习惯与抑郁症状之间的关系也是本次研究中的一个关键发现

- 通过对饮食习惯进行分组，计算“是否抑郁”和“是否有过自杀的念头”的平均值

![image-20241223012547586](https://db.xinghai.ink/github_DataAnalysisWork/image-20241223012547586.png)

- 结果表明，饮食习惯对抑郁症和自杀念头的发生有极为显著的影响。健康饮食习惯的学生群体相比不良饮食习惯的学生群体，抑郁症状和自杀念头的发生率较低。此结果表明，良好的饮食习惯可能是缓解学生抑郁症状的重要因素，因此学校可以通过倡导健康饮食，帮助学生改善心理健康状况

## 6. **KMeans聚类分析**

`对应jl()函数`

在对数据进行KMeans聚类分析时，选择了包括年龄、学习压力、学习满意度、睡眠时间、学习时间和经济压力等特征，对学生群体进行聚类。分析结果将学生划分为三个不同的群体

第一类患抑郁症群体别主要分布在学习压力大，年龄在26左右的岁的人群中，这类人群通常只有几年的工作经验，许多人在这个年纪开始面临结婚、生育、买房等生活中的重大决策和压力

![image-20241223012717887](https://db.xinghai.ink/github_DataAnalysisWork/image-20241223012717887.png)

第二类聚集在学习压力较低，但是年龄较小的部分大多都是刚入学的大学生，与同学的交往压力以及对未来职业的迷茫，这些问题往往是导致年轻大学生患抑郁症的重要因素

![image-20241223012730559](https://db.xinghai.ink/github_DataAnalysisWork/image-20241223012730559.png)

第三类聚集在年龄35岁左右，但是经济压力大的人群中，这类人数最多，35岁左右的人群面临的主要压力来源于职业发展瓶颈、家庭责任和自我认知，也是自杀倾向最多的人群

![image-20241223012722617](https://db.xinghai.ink/github_DataAnalysisWork/image-20241223012722617.png)

每个群体在学习压力、经济压力、学习满意度等方面存在显著差异。通过这种方式，能够识别出哪些学生群体可能面临更大的抑郁风险。例如，某些群体可能由于较高的学习压力和经济压力而更容易发展为抑郁症状。聚类分析有助于为心理健康干预提供更加精准的目标群体，进而制定更加有针对性的心理健康教育和干预方案

## 总结

本项目通过pandas读取和处理CSV数据，结合数据分析与可视化技术，探讨了抑郁症状与多个因素之间的关系。首先，对数据进行了规约和清洗，使用matplotlib可视化了各类数据分析结果。随后，使用sklearn的StandardScaler对数据进行了标准化处理，并通过KMeans聚类算法将学生群体进行分类，识别出不同的抑郁症高风险群体



1. **学习压力与抑郁症的正相关性**：学习压力较大的群体抑郁症状较为明显。学业压力是导致学生抑郁的重要因素。
2. **经济压力和学习满意度**：经济压力较大、学习满意度较低的群体抑郁风险更高，降低压力和提升满意度有助于减少抑郁症状。
3. **年龄对抑郁症状和自杀念头的影响**：随着年龄的增长，抑郁和自杀念头的发生率逐步增加，尤其是35岁左右的群体，职业和家庭压力较大。
4. **饮食习惯的影响**：健康的饮食习惯能有效减少抑郁症状和自杀念头的发生。
5. **KMeans聚类分析**：聚类分析揭示了不同群体在学习压力、经济压力、年龄等方面的差异，有助于识别高风险群体。



这些分析结果有助于识别学生群体中抑郁症状的高风险群体，指导心理健康干预工作。通过针对不同因素（如学习压力、经济压力、年龄、饮食习惯等）采取有针对性的干预措施，可以有效减少学生的抑郁风险，改善其心理健康状态。通过聚类分析的结果，也能帮助制定个性化的心理健康支持方案，精准定位需要帮助的群体。

记忆已更新

你可以按以下方式美化并添加总结内容，以提升项目的清晰度和可读性。

------

# 4. 员工离职情况分析

## 4.1 项目目录

```
kotlin复制代码E:.
│  analysis.py
│  main.py
│  MyWindow.py
│  MyWindow.qrc
│  MyWindow.ui
│  MyWindow_rc.py
│
├─data
│      员工离职分析.xlsx
│
└─img
        bj.jpg
        label.svg
```

- **main.py**：本文件为项目的入口，启动程序后会进入主界面。
- **MyWindow.py**：此文件为UI文件转换后的Python代码，包含了整个程序的图形界面组件和交互逻辑。
- **MyWindow.ui**：采用Qt Designer工具设计的UI文件，描述了界面布局和组件。
- **MyWindow.qrc**：资源文件，存储了UI界面中涉及的图片资源的路径信息。
- **MyWindow_rc.py**：自动生成的Python文件，包含了通过`qrc`文件嵌入的所有图片的二进制数据。
- **data**：包含用于分析的员工离职数据的Excel文件。
- **img**：存储项目中使用的静态图片资源。

## 4.2 main.py文件

程序的主要逻辑体现在`main.py`文件中，结构如下：

```
python复制代码from MyWindow import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QPoint
from analysis import DataAnalysis

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 设置界面
        self.function = DataAnalysis()  # 创建数据分析对象
        self.to_connect(self.function)  # 绑定UI控件和分析函数

    def to_connect(self, f):
        # 为按钮绑定相应的分析函数
        self.toolButton_4.clicked.connect(f.gongzi_lzl)
        self.toolButton_2.clicked.connect(f.yxgz)
        self.toolButton_3.clicked.connect(f.gcsl)
        self.toolButton.clicked.connect(f.gongl)
        self.toolButton_6.clicked.connect(f.sjsl)

if __name__ == '__main__':
    app = QApplication([])  # 启动Qt应用
    win = MyWindow()  # 创建并显示主窗口
    win.show()
    app.exec()  # 运行应用
```

1. **MyWindow类**：继承自`Ui_MainWindow`，封装了界面的所有控件和事件处理逻辑。
2. **构造函数**：初始化时创建`DataAnalysis`类的实例，负责所有数据分析相关的操作。
3. **to_connect方法**：将UI控件（如按钮）与数据分析函数相连接，确保用户交互时能触发相应的分析逻辑。

## 4.3 数据分析：数据处理

在`analysis.py`文件中，`DataAnalysis`类负责数据的清洗和预处理。

1. 使用`pandas`库读取`员工离职分析.xlsx`文件。
2. 对原始数据进行清洗，去除工作时间为零的记录，确保数据的准确性和完整性。

![image-20241224195541970](https://db.xinghai.ink/Typora/17350413470245125.png)



数据清洗是分析的第一步，目的是确保后续分析基于干净、可靠的数据源。去除无效或异常数据，能够有效提高分析结果的可信度和精度。

## 4.4 数据分析：工资与离职关系

在`gongzi_lzl`方法中，分析了员工工资水平与离职之间的关系。



1. 通过筛选，只保留已离职员工的数据，并提取出工资和离职状态的相关列。
2. 将数据按工资水平进行分组，并统计每个工资段对应的离职情况。
3. 使用`matplotlib`绘制离职率与工资水平的关系图，直观展示分析结果。

![image-20241224202450332](https://db.xinghai.ink/Typora/17351759111283703.png)



从结果中可以明显看出，工资水平较高的员工，其离职率相对较低。这一结论对于公司来说具有重要意义，尤其是在制定薪酬策略时，可以考虑通过提供更具竞争力的薪资来减少员工流失，从而提高员工的留任率。

## 4.5 数据分析：工资与其他指标的关系

在`yxgz`方法中，进一步分析了员工工资与其他关键指标（如考核得分、工龄、满意度等）之间的关系。



1. 按工资水平对员工进行分组，计算每个工资段的考核得分、工龄和满意度的均值。
2. 使用`matplotlib`可视化分析结果，展示不同工资段的员工在这些指标上的表现。

![image-20241224204028941](https://db.xinghai.ink/Typora/17350444402757473.png)



高工资员工不仅在工龄和考核得分上表现更为突出，同时其工作满意度也明显高于低薪员工。这表明公司可以通过优化薪酬结构，提升员工的工作表现和整体满意度，从而推动更高的生产力和忠诚度。

## 4.6 数据分析：工资与工程数量及离职的关系

在`gcsl`方法中，分析了工资水平与工程数量及离职之间的关系。



1. 从原始数据中筛选出工资、工程数量和离职状态三个关键字段。
2. 按工资分组，计算每个工资段的工程数量和离职率的平均值。
3. 使用`matplotlib`展示分析结果。

![image-20241224204710629](https://db.xinghai.ink/Typora/1735044436798724.png)



分析结果表明，高薪员工的离职率较低，并且分配的工程数量较少。较低薪资员工可能面临更多的工作压力，这可能是他们选择离职的一个因素。公司可以通过调整薪酬结构，减轻员工的工作压力，同时提高他们的工作满意度。

## 4.7 数据分析：工龄与离职的关系

在`gongl`方法中，分析了员工的工龄与离职之间的关系。



1. 筛选数据，仅保留工龄和离职状态字段。
2. 按工龄对数据进行分组，并计算每个工龄段的离职率。
3. 使用`matplotlib`展示分析结果，直观展现不同工龄段员工的离职率。

![image-20241224205338684](https://db.xinghai.ink/Typora/1735175895453515.png)



结果显示，员工的离职率随着工龄的增加逐渐上升，尤其是在工作年限达到五年时，离职率达到顶峰。这一发现表明，公司应特别关注工龄较长员工的工作状态，及时采取有效的干预措施，以降低离职风险。

## 4.8 数据分析：随机森林预测

为了更深入地分析员工离职的影响因素，我们采用了随机森林算法对员工离职进行预测。

### 数据预处理：

1. 对工资字段进行标签编码，将其转化为整数值，以便进行机器学习模型的训练。
2. 将数据集划分为训练集（80%）和测试集（20%），以验证模型的预测效果。

```
python复制代码from sklearn.preprocessing import LabelEncoder
data['工资'] = LabelEncoder().fit_transform(data['工资'])
X = data.drop(columns=['离职'])
```

### 模型训练与预测：

我们使用随机森林模型对训练数据进行训练，并对测试集数据进行预测。

![image-20241224221824275](https://db.xinghai.ink/Typora/17351758802165253.png)

### 结果评估：

通过对比预测值和实际值，我们得到了99%的准确率，表明模型具有极高的预测准确性。

![image-20241224222351503](https://db.xinghai.ink/Typora/17351756646443536.png)



使用随机森林算法可以有效地预测员工的离职倾向，准确率高达99%。这一结果不仅验证了数据分析模型的有效性，也为公司提供了一种精确的员工流失预测工具，帮助人力资源部门提前识别潜在的离职风险，制定相应的留人策略。

------

通过本次数据分析，结合薪酬、工龄、工作压力等多维度因素，深入探讨了员工离职的主要影响因素。基于这些数据驱动的见解，企业可以制定更具针对性的管理策略，从而降低员工流失率，提升整体的工作满意度和公司稳定性。
