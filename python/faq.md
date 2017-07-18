#### 0001

我已经添加了 文件 test.py 到环境变量 path中， 为什么执行命令 python test.py ，
解释器还是提示 can't open file 'test.py' :[Errno 2] No such file or directory

```python
答： 

环境变量 path 是针对命令中 可执行程序(比如上述的 python) 设置的搜索路径, 
不是 命令中的参数文件 （比如上述的 test.py）设置的搜索路径.
参数文件必须使用正确的相对路径或者绝对路径

```



<br><br><br>
#### 0002

import paramiko 出现如下错误

```python
 result_path = result_path + p_path
UnicodeDecodeError: 'ascii' codec can't decode byte .....
```

```python
答： 
这是环境变量 path 里面有中文导致的
```



<br><br><br>
#### 0003
list、dict里面有中文的时候，为什么print 它们，显示的是像二进制的数字呢？

```python
答： 
print 一个对象，其实就是调用这个对象的__str__方法或者__repr__方法。
列表、字典的__str__方法，就是这样实现的，对于不在acii范围内的字节，就显示为16进制的数字
```

