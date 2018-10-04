 # coding=utf-8

from sys import argv

script, input_file = argv

def print_all(f):# 第一个函数
	print f.read()

def rewind(f): #第二个函数
	f.seek(0)

def print_a_line(line_count, f): # 第三个函数
	print line_count, f.readline() #读取第几行的内容

current_file = open(input_file)

print  "First, let's print whole file: \n"
print_all(current_file) # 给第一个函数的参数赋变量

print "Now,let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)





