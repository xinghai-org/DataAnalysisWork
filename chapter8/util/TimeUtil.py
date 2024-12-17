# 引入模块
import datetime

# 返回 星期几标记 0代表星期一 1代表星期二...6代表星期天
def get_week_numbeer(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    day = date.weekday()
    return day