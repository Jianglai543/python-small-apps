import numpy as np
import os


def save_menu():

    np.save('a.npy', list)


list2 = np.load('a.npy', allow_pickle=True) #记录所有名片字典
list = list(list2)
# print(type(list))
# list = list.extend(list2)
def show_menu():
    print("数据库信息管理 1.0")
    print("*" * 50)
    print("1. 新增数据库信息")
    print("2. 显示全部数据库信息")
    print(" ")
    print("3. 查询数据库信息")
    print(" ")
    print("4. 保存数据库信息")
    print("0. exit数据库")
    print(" ")
    print("*" * 50)


def add_menu(name, phone, qq, email):
    """print("新增名片: ")
    name = input("请输入名字: ")
    phone = input("请输入phone: ")
    qq = input("请输入qq: ")
    email = input("请输入email: ")"""
    card_dict = {
        "name": name,
        "phone": phone,
        "email" : email,
        "qq": qq
    }
    list.append(card_dict)
    # return ("add %s 成功 " % card_dict["name"])


def show_all():
    """
    显示所有名片
    """
    print("显示全部名片: ")

    yield ("共有%d人信息:" % len(list))
    for x in list:
        yield ("名字：%s 电话：%s qq: %s 电子邮件：%s" % (x["name"], x["phone"], x["qq"], x["email"]))
        yield '\n'



def check_menu(namex):
    """查询"""

    for y in list:
        if namex in y["name"] or namex in y["phone"]:
            yield ("名字：%s 电话：%s qq: %s 电子邮件：%s" % (y["name"], y["phone"],y["qq"],y["email"]))#y 是一字典
            """value = input("你要干嘛：1.删名片||2.修改名片")
            if value == '1':
                list.remove(y)
                if len(list) ==  0:
                    print("删除成功，当前无信息：")
                    break
                else:
                    print("删除成功，更新如下：")
                    for list_c in list:
                        print("名字：%s 电话：%s qq: %s 电子邮件：%s" % (list_c["name"], list_c["phone"], list_c["qq"], list_c["email"]))
            else:
                for key_bb in y:
                    str_x = input(f"请输入新{key_bb}：（不改直接回车）")#value
                    if str_x !='':# 有内容不是回车 进来
                        if str_x.isspace() == True:# 内容是空格
                            print("别啥也不输啊！")

                        elif str_x.isspace()!= True:# 内容是值
                            y[key_bb] = str_x

                print("名字：%s 电话：%s qq: %s 电子邮件：%s" % (y["name"], y["phone"], y["qq"], y["email"]))
            break"""



    # yield ("没这个人，你逗我")



