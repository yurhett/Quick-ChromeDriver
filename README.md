# Quick-ChromeDriver

## (A quicker way to install webdriver)

## CN：

### 简介：

Quick-Chrome Driver是一个单文件python脚本，里面包含了一个类，具备一键安装或更新Chrome Driver的能力，解决了小白难以为爬虫或其它Python脚本安装必备的Chrome Driver的问题。

### 教程：

下载quickChromeDriver.py或quickChromeDriverCN.py，这两个文件的区别如下：

|          | quickChromeDriver.py | quickChromeDriverCN.py |
| -------- | -------------------- | ---------------------- |
| 下载源   | 官网地址             | 淘宝镜像               |
| 提示信息 | 英文                 | 中文                   |

#### 调用：

##### 直接运行脚本：

将脚本最后一行的注释符号"#"删掉，运行Python脚本；或者，将以下代码粘贴到脚本的尾部：

```python
q_chromedriver().update_driver()
```

##### 在其它脚本中调用：

```python
import quickChromeDriver as qcd
qcd.q_chromedriver.update_driver()
```

## EN：

### Introduction：

Quick chrome driver is a single file Python script, which contains a class, which has the ability to install or update chrome driver with one click. It solves the problem that novices are difficult to install the necessary chrome driver for Python scripts.

### Tutorial：

Download quickChromeDriver.py or quickChromeDriverCN.py. The differences between the two files are as follows:

|                 | quickChromeDriver.py | quickChromeDriverCN.py |
| --------------- | -------------------- | ---------------------- |
| Download source | Official Website     | mirror form Taobao     |
| Language        | English              | Chinese                |

#### Run:

##### Run the script directly:

Delete the comment symbol "#" on the last line of the script and run the python script; or paste the following code at the end of the script and run the python script:
```python
q_chromedriver().update_driver()
```
##### In other script:
```python
import quickChromeDriver as qcd
qcd.q_chromedriver.update_driver()
```



# 鸣谢：

#### 感谢[@CarlGao4](https://blog.csdn.net/weixin_45888599)在CSDN上的代码，本脚本就是在他的[基础](https://blog.csdn.net/weixin_45888599/article/details/105854329)上简单修改来的。



