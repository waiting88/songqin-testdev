## 安装虚拟机，虚拟机中安装Linux

请大家自行百度搜索，安装虚拟机管理器 virtualbox 或者 vmvareplayer， 创建 64位 虚拟机，
安装centos镜像

cetos6.5 下载地址 :
http://archive.kernel.org/centos-vault/6.5/isos/x86_64/CentOS-6.5-x86_64-bin-DVD1.iso

## 安装 Mysql 服务

1 执行下面命令安装mysql 5.6 基于 centos 6.5 的yum源

```
wget http://repo.mysql.com/mysql-community-release-el6-5.noarch.rpm
rpm -ivh mysql-community-release-el6-5.noarch.rpm
```
	
2 执行下面命令安装 mysql server 和 mysql devel


```
yum install mysql-server
yum install mysql-devel
```


## 启动mysql

执行命令 service mysqld start


## 创建 数据库管理员 账号

执行命令 mysql 启动 mysql 命令行客户端，在交互式命令行输入

```
CREATE USER 'dbadmin'@'localhost' IDENTIFIED BY 'ohmyjcy1!';   
CREATE USER 'dbadmin'@'%' IDENTIFIED BY 'ohmyjcy1!';
```

然后 给 数据库管理员 账号 dbadmin 赋予超级权限

```
GRANT ALL ON *.* TO 'dbadmin'@'localhost';
GRANT ALL ON *.* TO 'dbadmin'@'%';
```

执行quit 退出 mysql client
