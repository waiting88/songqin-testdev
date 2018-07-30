
# Appium 作业 1 

根据课堂视频，安装搭建Appium运行环境，并运行示例代码

<br><br>
## 安装Appium Python Client 包

安装Appium Python Client 包的命令

pip install Appium-Python-Client


<br><br>
## 安装 Appium Server 

下载安装Appium Desktop的安装包，
下载地址 https://github.com/appium/appium-desktop/releases/latest
下载扩展名为.exe的包


<br><br>
## 安装 Android SDK

方法1：

官方中文网站
https://developer.android.google.cn/studio/archive.html
选择2.3.3 版本，包含了sdk的安装包 Windows IDE bundle with SDK (64-bit)

特别注意，安装程序要求路径中最好不要有空格。


方法2：百度云盘下载 zip包，解压

![image](https://user-images.githubusercontent.com/10496014/43395777-eb115d32-9431-11e8-9612-3a5f245ba5f3.png)


## 设置android_home 环境变量的值为 sdk 目录

<br><br>
## 安装JDK
到 oracle 官方网站下载JDK 1.8 的安装包，进行安装

<br><br>
## 安装安卓模拟器

先试试android studio里面自带的模拟器

打开 studio，创建一个项目，通过tools - android - AVD Manager菜单创建一个安卓模拟设备

-----------


如果不行，可以试试Genymotion，安装过程参考 https://github.com/jcyrss/songqin-testdev/issues/3

<br><br>
## 运行自动化测试
- 运行虚拟机，下载开发者头条应用，http://toutiao.io/s/apk <br>
安装到虚拟机中并运行；<br>
注册一个账号<br>
- 根据课堂教学视频，运行Appium Server，并设置、启动服务<br>
- 下载自动化脚本https://github.com/jcyrss/songqin-testdev/blob/master/appium/src/lesson1/toutiao_login.py
修改其中用户名，密码为你注册的账号，运行脚本完成一个自动登录功能




 

