# coding=utf-8

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C "
print "If you do want that, hit RETURN"

raw_input("?")

print "opening the file..."
target = open(filename, 'w')
print "Truncating the file. Goodbye" #运行脚本发现源文件ex15_sample.txt被擦除，不合理啊？还没执行下一步呀、 w 是什么鬼

target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write thse to the file."

target.write(line1) # 运行脚本，发现源文件 ex15_sample 写入了字符，键盘输入什么就显示什么
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "then close it"
target.close()


