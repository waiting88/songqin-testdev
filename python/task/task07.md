# Python 作业 7

下载附件cfiles.zip（见附件[cfiles.zip](https://raw.githubusercontent.com/jcyrss/songqin-testdev/master/python/task/attachs/cfiles.zip)）

```python


解压该压缩包，里面 包含了两个文件。 一个叫 'gbk编码.txt',
该文件是gbk编码的。
另一个文件叫 'utf8编码.txt', 该文件是utf8编码的。
两个文件里面的内容都包含中文。

要求大家编写一个python程序，该程序做到以下2点

1. 将两个文件内容读出， 合并内容到一个字符串中，
   并能用print语句将合并后的内容正确显示
   
2. 然后，程序用中文提示用户“请输入 新文件的名称”，用户输入文件名可以包含中文
   将上面合并后的内容存储到一个新文件中，以utf8格式编码。
   新文件的文件名就是上面用户输入的名字。


```





## 参考答案，往下翻
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

```python
# coding=utf8

#打开中文的文件名一定要用unicode。
with open(u'cfiles/gbk编码.txt') as f1, open(u'cfiles/utf8编码.txt') as f2:
    # 根据不同的编码格式，对内容进行解码
    content1 = f1.read().decode('gbk')
    content2 = f2.read().decode('utf8')

    # 要合并内容，必须先都转化成unicode，再合并
    newContent = content1 + content2

    print newContent

print u'请输入新文件的名称:',
newFile = raw_input()

# 用户输入的内容的编码方式，和代码的运行环境有关， 如果是dos命令行执行 得到的是gbk编码
uNewFile = newFile.decode('utf8')

with open(uNewFile,'w') as f:
    f.write(newContent.encode('utf8'))
```
