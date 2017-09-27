```python
江老师的小广告：
请各位同学，帮忙到我的腾讯课堂给我的课程写一些评价。  
对我的考核有好处哦，谢谢大家。
```

### 评价到达40个，我会在群里给大家发红包。。。有劳各位啦。。。
<br><br>
课堂链接 https://ke.qq.com/course/212215#tuin=ba4122
<br>
![点击这里](https://github.com/jcyrss/songqin-testdev/raw/master/pictures/rate.png "我的课堂")
<br><br><br>



# Python 编程作业 02 

### 请实现一个程序，实现如下需求点

```java


1.程序开始的时候提示用户输入学生年龄信息 格式如下：

Jack Green ,   21  ;  Mike Mos, 9;

我们假设 用户输入 上面的信息，必定会遵守下面的规则：
  学生信息之间用分号隔开（分号前后可能有不定数量的空格），
  学生姓名长度最多不超过20个字符。
  每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格） 。
  输入学生的数量不限

2. 程序随后将输入的学生信息分行显示，格式如下
Jack Green :   21;
Mike Mos   :   09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零


```



## 参考答案，往下翻


<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

```python
inputStr = input('Please input student age info:')
studentInfo = inputStr.split(';')
for one in studentInfo:
    # check if it is valid input 
    if ',' not in one: 
        continue
        
    name,age = one.split(',')
    name = name.strip()
    age  = age.strip()
    
    #  check is age digit
    if not age.isdigit():
        continue
    
    age = int(age)

    print('%-20s :  %02d' % (name, age))
    # print('{:20} :  {:02}'.format(name, age))
    # print(f'{name:20} :  {age:02}')
```
