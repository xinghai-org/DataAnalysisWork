import house_analisis
import chart
from PyQt5.QtWidgets import QApplication,QMainWindow
from MainWindow import Ui_MainWindow
class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 绑定按键函数
        self.button_connect()
    
    # 将按钮绑定函数
    def button_connect(self):
        self.btn_1.triggered.connect(self.show_average_price)
        self.btn_2.triggered.connect(self.show_house_number)
        self.btn_3.triggered.connect(self.show_renovation)
        self.btn_4.triggered.connect(self.show_type)
        self.btn_5.triggered.connect(self.show_total_price)

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
        print(price)
        chart.bar(price,type,'热门户型均价分析')
    
    # 显示二手房预测图
    def show_total_price(self):
        true_price,forecast_price = house_analisis.get_price_forecast()
        chart.broken_line(true_price,forecast_price,'二手房价预测')

if __name__ == '__main__':
    app = QApplication([])
    win = Main()
    win.show()
    app.exec()