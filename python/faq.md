#### *******

我已经添加了 文件 test.py 到环境变量 path中， 为什么执行命令 python test.py ，解释器还是提示 can't open file 'test.py' :[Errno 2] No such file or directory

```python
答： 

环境变量 path 是针对命令中 可执行程序(比如上述的 python) 设置的搜索路径, 不是 命令中的参数文件 （比如上述的 test.py）设置的搜索路径.
参数文件必须使用正确的相对路径或者绝对路径

```
