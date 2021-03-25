"""


Quick-ChromeDriver
Author: yurhett @ https://github.com/yurhett/
Update this script on: https://github.com/yurhett/Quick-ChromeDriver


"""

import urllib.request
import winreg
import re
import zipfile
import os


class q_chromedriver:
    def __init__(self):
        self.driver_ver = None
        self.chrome_ver = None

    def _del_olddriver(self):
        if os.path.exists('./chromedriver.exe'):
            os.remove('./chromedriver.exe')
        if os.path.exists('./chromedriver_win32.zip'):
            os.remove('./chromedriver_win32.zip')

    def _unzip_file(self, src_file, dest_dir, password=None):
        if password:
            password = password.encode()
        zf = zipfile.ZipFile(src_file)
        try:
            zf.extractall(path=dest_dir, pwd=password)
        except RuntimeError:
            raise OSError('文件解压错误！')
        zf.close()

    def _download_target(self, target_ver):
        below73_map = {
            '73': '2.46',
            '72': '2.46',
            '71': '2.46',
            '70': '2.45',
            '69': '2.44',
            '68': '2.42',
            '67': '2.41',
            '66': '2.40',
            '65': '2.38',
            '64': '2.37',
            '63': '2.36',
            '62': '2.35',
            '61': '2.34',
            '60': '2.33',
            '59': '2.32',
            '58': '2.31',
            '57': '2.29',
            '56': '2.29',
            '55': '2.28',
            '54': '2.27',
            '53': '2.26',
            '52': '2.24',
            '51': '2.23',
            '50': '2.22',
            '49': '2.22',
            '48': '2.21',
            '47': '2.21',
            '46': '2.21',
            '45': '2.20',
            '44': '2.20',
            '43': '2.20',
            '42': '2.16',
            '41': '2.15',
            '40': '2.15',
            '39': '2.14',
            '38': '2.13',
            '37': '2.12',
            '36': '2.12',
            '35': '2.10',
            '34': '2.10',
            '33': '2.10',
            '32': '2.9',
            '31': '2.9',
            '30': '2.8',
            '29': '2.7'
        }
        if target_ver <= 73:
            if not str(target_ver) in below73_map:
                raise KeyError('There isn\'t a chromedriver that supports your Chrome version. ')
            try:
                urllib.request.urlretrieve('https://npm.taobao.org/mirrors/chromedriver/' + below73_map[
                    str(target_ver)] + '/chromedriver_win32.zip', 'chromedriver_win32.zip')
            except:
                print('服务器连接失败！')
                raise ConnectionError('服务器连接失败！')
            else:
                print('解压中，请稍候...')
                self._unzip_file('chromedriver_win32.zip', '')
                print('下载成功！')
                if os.path.exists('./chromedriver_win32.zip'):
                    os.remove('./chromedriver_win32.zip')
        else:
            available_versions = {}
            try:
                url_read = urllib.request.urlopen(
                    urllib.request.Request('https://npm.taobao.org/mirrors/chromedriver/')).read().decode()
            except:
                print('服务器连接失败！')
                raise ConnectionError('服务器连接失败！')
            else:
                for i in re.findall('<a href="/mirrors/chromedriver/(.*?)</a>', url_read):
                    if i[0] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' or 'RELEASE' in i or int(
                            i.split('.')[0]) <= 72:
                        continue
                    if not i.split('.')[0] in available_versions:
                        available_versions[i.split('.')[0]] = i.split('/">')[0]
                if not str(target_ver) in available_versions:
                    raise KeyError('There isn\'t has a chromedriver that supports your Chrome version. ')
                try:
                    print('下载中，请稍候... \nURL:https://npm.taobao.org/mirrors/chromedriver/' + available_versions[
                        str(target_ver)] + '/chromedriver_win32.zip')
                    urllib.request.urlretrieve('https://npm.taobao.org/mirrors/chromedriver/' + available_versions[
                        str(target_ver)] + '/chromedriver_win32.zip', 'chromedriver_win32.zip')
                except:
                    print('下载失败，请重试...')
                else:
                    print('解压中，请稍候...')
                    self._unzip_file('chromedriver_win32.zip', '')
                    print('下载成功！ ')
                    if os.path.exists('./chromedriver_win32.zip'):
                        os.remove('./chromedriver_win32.zip')

    def has_driver(self):
        if os.path.isfile('./chromedriver.exe'):
            result = os.popen('chromedriver.exe -v')
            res = result.read()
            if 'ChromeDriver' in res:
                self.driver_ver = res.split(' ')[1].split('.')
                return self.chrome_ver
            else:
                print('ChromeDriver已损坏，请自行删除再试。')
                return None
        else:
            print('未找到ChromeDriver，处理中...')
            return None

    def has_chrome(self):
        try:
            full_chrome_ver = \
                winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Google\\Chrome\\BLBeacon'),
                                    'version')[
                    0]
            self.chrome_ver = int(full_chrome_ver.split('.')[0])
            return self.chrome_ver
        except:
            self.chrome_ver = None
            print('未找到Chrome...')
            return None

    def update_driver(self):
        if self.has_chrome() is None:
            print("请安装Chrome后重试...")
        elif self.has_chrome() is not None:
            if self.has_driver() is None:
                self._download_target(self.chrome_ver)
            elif self.has_driver() is not None:
                if self.chrome_ver != int(self.driver_ver[0]):
                    print(f"错误的版本，Chrome版本是:{self.chrome_ver}, ChromeDriver的版本是:{self.driver_ver[0]}, 正在更新...")
                    self._del_olddriver()
                    self._download_target(self.chrome_ver)
                elif self.chrome_ver == int(self.driver_ver[0]):
                    print("ChromeDriver的版本已经是匹配的了，请继续其它操作。")

#q_chromedriver().update_driver()
