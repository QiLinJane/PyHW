# f.seek

from sys import argv

script, input_file = argv


# 定义函数 
def rewind(f):
	f.seek(0) 
	
	
	print f.read()


# 上面先定义函数 ，下面是给 f 参数赋值，当 f=current_file 的时候，rewind 等于多少
current_file = open(input_file)
print "now let's rewind, kind of like a tape:"

rewind(current_file)