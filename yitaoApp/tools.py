import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import time
import os


# 自定义生成Excel表格
def toExcel(values):
    # 日期
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:-9]
    # 生成表格的名字
    filepath = './media/files/' + date + '.xls'
    # 判断表格是否存在,如果存在,追加写入,如果不存在,则创建表格
    if os.path.exists(filepath):
        rexcel = open_workbook(filepath)
        print('找到表格,正在写入...')
        rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
        print('现有行数为：', rows)
        excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
        table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
        # 要写入的是第几行
        row = rows
        for i in range(len(values)):
            table.write(row, i, values[i])  # xlwt对象的写方法，参数分别是行、列、值
        excel.save(filepath)  # xlwt对象的保存方法，这时便覆盖掉了原来的excel
        print('完成写入')
    else:
        print('表格不存在,正在创建表格')
        xls = xlwt.Workbook()
        sht1 = xls.add_sheet('订单表')
        # 添加字段
        sht1.write(0, 0, '订单日期')
        sht1.write(0, 1, '用户名')
        sht1.write(0, 2, '订单号')
        sht1.write(0, 3, '邀请人')
        sht1.write(0, 4, '订单时间')
        sht1.write(0, 5, '支付宝账号')
        sht1.write(0, 6, '手机号')
        # 给字段中加值   考虑使用循环
        for i in range(len(values)):
            sht1.write(1, i, values[i])

        xls.save(filepath)
        print('创建表格完成')
        print(filepath)
        print(type(filepath))
    return filepath


def getData(data):
    # 订单日期
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:-9]
    # 用户名
    nickName = data['nickName'][0]
    # 订单号
    orderNumber = data['orderNumber'][0]
    # 邀请人
    uploader = data['uploader'][0]
    # 订单时间
    pubdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 支付宝账号
    payAccount = data['payAccount']
    # 手机号
    phoneNumber = data['phoneNumber']

    values = [date, nickName, orderNumber, uploader, pubdate, payAccount, phoneNumber]
    return values
