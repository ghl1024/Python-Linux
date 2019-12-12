#!/usr/bin/env python
# -*- coding:utf-8 -*-

import psutil, time, xlsxwriter
from  xlsxwriter import Workbook
import socket
import socket
import time

##当前时间
time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

##主机名
hostname = socket.gethostname()

##IP地址
outside_ipaddr=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     ##获取外网网卡
inside_ipaddr=socket.gethostbyname(socket.gethostname())              ##获取内网网卡
# u'外网网卡',u'内网网卡',
#outside_ipaddr,inside_ipaddr,

##CPU
user_cpu_time = psutil.cpu_times().user     ##获取用户时间比
cpu_number = psutil.cpu_count(logical=False)   ##CPU物理个数

##内存信息
mem_total = psutil.virtual_memory().total/1048576
mem_free = psutil.virtual_memory().free/1048576
mem_used = psutil.virtual_memory().used/1048576

##磁盘信息
disk_total = psutil.disk_usage('/').total/1048576
disk_used = psutil.disk_usage('/').used/1048576
disk_free = psutil.disk_usage('/').free/1048576

##网络信息
net_in = psutil.net_io_counters().bytes_recv/1048576
net_out = psutil.net_io_counters().bytes_sent/1048576


##建立一个列表存放获取的系统信息
text = [time,outside_ipaddr,inside_ipaddr,hostname,user_cpu_time,cpu_number,mem_total,mem_free,mem_used,disk_total,disk_used,disk_free,net_in,net_out]

workbook = xlsxwriter.Workbook('巡检.xlsx')    ##建立一个excel表格
##建立一个工作表对象，也就是excel左下角的sheet1，sheet2等，这里建立了一个。
worksheet = workbook.add_worksheet()

##存放excel表格标题信息的列表
title = [u'时间',u'外网地址',u'内网地址',u'主机名',u'用户cpu时间比',u'cpu数量',u'内存总量',u'已使用内存',u'空闲内存',u'磁盘总量',u'已使用磁盘',u'空闲磁盘',u'网卡出流量',u'网卡入流量']

##建立设置单元格格式的内容，如set_border是边框加粗，set_bg_color是单元格背景颜色
format_title = workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')

format_text = workbook.add_format()
format_text.set_border(1)

##写入单元格操作
worksheet.set_column('A:Z',18)   ##设置A到K列宽度20像素
worksheet.write_row('A1',title,format_title)   ##将title列表有A1开始横向写入，并且格式为format_title

worksheet.write_row('A2',text,format_text)

workbook.close()   ##关闭工作表
