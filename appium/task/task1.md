
# Appium 作业 1 

根据课堂视频，安装搭建Appium运行环境，并运行示例代码

<br><br>
## 安装Appium Python Client 包
新版本的Selenium 和Appium Server配合有问题，需要安装3.3.1 版本的selenium

怎么看selenium版本
```python
d:\data>python
>>> import selenium
>>> selenium.__version__
'3.3.1'

如果版本不是 3.3.1 

pip uninstall selenium
pip install selenium==3.3.1
```

安装Appium Python Client 包的命令

pip install Appium-Python-Client


<br><br>
## 安装 Appium Server 

下载安装Appium Desktop的安装包，
下载地址 https://github.com/appium/appium-desktop/releases/latest



<br><br>
## 安装 Android Studio

官方中文网站
https://developer.android.google.cn

特别注意，安装程序要求路径中最好不要有空格。


<br><br>
## 安装JDK
百度搜索一下jdk(操作一下)，下载安装就可以


<br><br>
## 安装安卓模拟器

android studio里面自带的模拟器
打开 studio，创建一个项目，通过tools - android - AVD Manager菜单创建一个安卓模拟设备

Genymotion
Genymotion 官网上下载安装包， https://www.genymotion.com/




需要注册一个账号，注册好了以后，就可以下载了


安装Genymotion-ARM-Translation_v1.1.zip包，刷入虚拟设备。它支持将ARM的机器指令转换为x86的机器指令。 
共享地址 ： http://pan.baidu.com/s/1jIfx44u

<br><br>
## 运行自动化测试
1 运行虚拟机，下载开发者头条应用，http://toutiao.io/s/apk， 
安装到虚拟机中并运行；
注册一个账号
2 根据课堂教学视频，运行Appium Server，并设置、启动服务
3 下载自动化脚本，修改其中用户名，密码为你注册的账号，运行脚本完成一个自动登录功能




 

