# PyHW
《笨办法学 Python》实战
plan done erros ref

- 必须十分小心，单词拼写十分小心；
- 改掉坏习惯 指头打 改掉了这个习惯；但一打中文的时候就回到了坏习惯。很有意思。做一些新鲜的事情有助于发现自己的旧模式
- 学会了看报错；不再简单地复制粘贴到 浏览器，也不再简单地截图问老公，这是怎么回事。
- 学习一个长期的项目时，通过建仓库把这件事仪式化。

给那些初学的人什么建议
- 比想象得有意思，不要想这是程序员干的，我又不当程序员，学他干嘛；类比看电影读如何写剧本的书
- 建一个仓库 外部化；不要默默干
-  readme 驱动进程
-  不理解就跳过，往前做几个练习后再返回做你不懂的。不要非弄懂
- 不要全部敲完代码才运行；用游戏心态，看看不写这句会怎么样，更有助于理解语法的含义；
比如下面这段，中间练习需要打完很多语句，我先把头尾加上，打印一句；
```
poem = """
\tThe lovely world
……
"""
```
## Plan
刷完 ex1-ex39;目标是做词云和 mapping/atl

## Log
- 181006
  + ex22:1-16;ex23;ex27-28
- 181005
    + [x]  ex25;
- 181004
    + [x] ex18-ex22;ex24; 6h 
      + [ ] ex22 倒序进行到 ex17     
- 181003
    + [x] ex9-ex17; 4h
- 181002
    - [x] ex1-ex8; cost 5.1h
    - [x] create repo"PyHW";log it; cost 0.5h

## 

## Error

### 1. encoding
报错:

```
➜  python python exl.py
  File "exl.py", line 5
SyntaxError: Non-ASCII character '\xef' in file exl.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

```
 
办法：
在 exl.py 最上面一行添加
`# coding=utf-8`

ref:[PEP 263 -- Defining Python Source Code Encodings | Python.org](https://www.python.org/dev/peps/pep-0263/)

### 3.1 % 为 X 除以 Y 还剩 J
### 3.2 浮点数
不太明白：

### 4. 文件另存后分清在哪一个文件上操作 
遇到一个特别奇葩的问题: 不断报错编码出问题

```
➜  python python ex4.py
  File "ex4.py", line 1
SyntaxError: Non-ASCII character '\xe8' in file ex4.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```

尝试1：检查是否有语法错误，发现不是语法错误；尝试用另一种编码方式

- 将`# coding=utf-8` 换为 `# -*- coding: utf-8 -*-`

- 继续报错

尝试2：在另一个有编码的文件中实验，发现同样的`# coding=utf-8` ，另一个文件就可以完美输出；

- 说明不是语法问题；
- 是文件问题



尝试3:复制文本到新文件 test.py ，发现可以输出打印；

- 说明是原文件 ex4.py 有问题；
- 检查：ex4.py 是另存前的文件；即两个同名文件分别在不同的文件夹，终端一直输出的是 python/ex4.py；而我修改的是 mac/ex4.py 	
- 根本问题是：我误以为另存后编辑器显示的是另存后的文件，实际是另存前的文件 
- 经验：改文件路径后，正在编辑的为原路径文件；不是另存后的文件。


等等又错了，是否验证过

- 另存后编辑器显示的不是另存后的文件？
- 需要验证：
- 新建、另存、编辑；
- 发现猜想错误：另存后编辑器显示的就是另存后的文件；
- 继续还原当时的场景：我选择的不是另存，是在 finder 中直接把原文件复制粘贴到目标文件夹了，且没有在编辑器重新打开新文件，造成了错误。


经验：小黄鸭
- 要不说出来
- 要不每做一步，写注释

太有意思了，以为自己犯错的地方，其实并不是真实错误，也就是说，真实问题没找对。

如何找到真实问题？而不是没根据地胡乱猜想？
- 双盲实验，控制变量
- 重现错误场景，才能真正找到问题，这也是我为什么要「重现血案」的原因。否则下次还会再犯


> 感知问题
> 分析现象
> 定义问题：需要排查
> 复现问题：人很容易想当然，想当然就定义不了真实问题，也就无法找对真正解决办法
> 设计方案:写在注释里
> 逐一检验
> 计划实施
> 复盘归档
> 是也乎哉


> 关键是你测试前的设计过程是否有

> 为什么测试
> 测试什么场景
> 场景构建怼卟?
> 怎么证明?
> 指令效果吻合预期嘛? 怎么证明?
> 为什么

这一个小事件，让我有机会用工程思维解决问题

### ex8. True, False 没有大写，打印不出来
ref: [为什么 Python 里的 True 和 False 两个布尔值首字母要大写呢？ - 知乎](https://www.zhihu.com/question/22564380)

### ex8. 为什么既有单引号又有双引号
```
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
```

'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'

### 11ex:把年龄身高输入到了weight = raw_input ()

不能填在这里，应该填在终端命令行。当脚本暂停，输入你的年龄。

### 12ex: pydoc raw_input
### 13ex: 运行程序不再是上面的 python ex13.py 而是 python ex13.py apple pear grape

参数 argument
模块 module

### 14ex argv & raw_input
### 17ex 语句里必须有变量；忘记加 %d 
### 18ex 函数后没有加冒号
### 18ex def 的意义是定义函数，只定义不调用，打印不出来
比如
```
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
```

终端是打印不出来，必须再加上函数的内容 
`print_two("qi", "lin")`

### 19ex 函数名不能有空格 cheese_and _crackers 是错误的
### 19ex print 缩进说明是函数模块的一部分，表示打印此函数的结果；
### 20ex 开始变难
### 24ex 如果函数没有返回值，没有加 return, 则报错信息为
`typeError: 'NoneType' object is not iterable`
下次遇到此类报错信息就能快速反应是没有加 return 的原因
\t\t?

### 25ex file.split(' ') 单引号里应该有空格；如没有则报错
报错

```
>>> words = ex25.break_words(sentence)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ex25.py", line 5, in break_words
    words = stuff.split(' ')
ValueError: empty separator

```

如何调试？
尝试1：

- 返回 ex25.py 在 words = stuff.split('') 加空格 => words = stuff.split(' ')
- 尝试：从头开始输入，不再报错

### 25ex shell 里的语句一句都不能少
比如：>>> ex25.print_last_word(sorted_words)
 当时觉得无关紧要就没有打印，后面 sortedwords 就全乱了
 说明函数的位置很重要

## 二、SymbleTable
边做边参考官方文档，非常清晰：https://python-reference.readthedocs.io/en/latest/docs/file/seek.html|ex20/ex2001
词|含义|解释
---|---|---|---
function|函数|y(x)|exall
return|返回|return 右边的东西作为函数的返回值|ex21
file.seek|指定文件位置|file.seek(0):从文件的开始位置;参考https://python-reference.readthedocs.io/en/latest/docs/file/seek.html|ex20/ex2001
file.read|Returns specified amount of bytes from the file.|f.read():返回全部内容|ex20
file.readline|Reads one entire line from the file.|f.readline():返回第一行的 string 字符|ex2001
file.write|写入|file.write(x);x=open(file_name)|ex17/16
file.truncate|清空文件|file.truncate()|ex16
file.close|关闭|file.close()|ex17
open|打开文件|打开文件并写入：open(file, 'w')|ex17
def|定义函数|类似于声明,ladies and gentlemen|ex18
exists|命令|exists 这个命令将文件字符串作为参数，文件存在则返回True;学会通过 import 调用它:from os.path improt exists/exists(file_name)|ex17
cat|命令|查看全部: cat test.txt|ex17
"w"|特殊字符串|表示文件的访问模式，写入；read只读；append 追加|ex16











