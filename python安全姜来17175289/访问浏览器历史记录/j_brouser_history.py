import os
import sqlite3
import operator
from collections import OrderedDict
import matplotlib.pyplot as plt


def parse(url):
    """分析url并获得去除www.的网址"""

    try:
        url_values = url.split('//')
        url_split = url_values[1].split('/', 1)
        domain = url_split[0].replace("www.", "")  # 删除www.
        return domain

    except IndexError:
        print("URL is not available ！")


def analyze_the_result(results):
    """使用bar绘图"""
    plt.bar(range(len(results)), results.values(), align='edge')
    plt.xticks(rotation=90)
    plt.xticks(range(len(results)), results.keys())
    plt.show()

if __name__ == '__main__':

    data_path = r'C:\Users\future\AppData\Local\ChromeCore\User Data\Default' # 用户自己的浏览器用户数据文件夹路径
    files = os.listdir(data_path)

    history_db = os.path.join(data_path, 'history')
    print(history_db)

    c = sqlite3.connect(history_db)  # 连接
    cursor = c.cursor()  # 创建一个游标对象
    select_elements = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
    cursor.execute(select_elements)

    results = cursor.fetchall()  # tuple  获取所有的数据

    sites_count = {}

    """遍历字典并计数"""
    for url, count in results:
        url = parse(url)
        if url in sites_count:
            sites_count[url] += 1
        else:
            sites_count[url] = 1

    sites_sorted_counts = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))# 使用了有序字典

    analyze_the_result(sites_sorted_counts)
