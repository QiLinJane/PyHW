# coding=utf-8

# this one is like your scripts with argv
# def 命令创建一个函数，函数名字叫 print_two，参数是 *args，参数必须放在圆括号，多个参数用逗号分隔；结束必须有冒号
def printtwo(*args): # *是把所有参数都接受进来
	arg1, arg2 = args #和脚本的 argv 类似 ；缩进
	print "arg1: %r, arg2: %r" % (arg1, arg2)
# ok, that *args is actually pointless, wecaj just do this 
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothing." # 如果不调用函数 print_none() print 是打印不出来的

printtwo("hugo", "yin")
print_two_again("qi", "lin")
print_one("dodododo")
print_none()

# 函数名是以字符和下划线组成的吗？验证一下，去掉下划线？可以打印，说明不是必须有下划线；但这是规范



