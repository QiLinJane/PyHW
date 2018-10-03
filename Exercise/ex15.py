
# coding=utf-8

from sys import argv

# 用 argv 取文件名；script 是ex15.py;filename是 ex15_sample.txt
script, filename = argv


# 为什么不直接写 ex15_sample.txt?因为不想写死，这些信息应该用户输入才对；写死的文件名会给自己带来麻烦，所以需要用 argv raw_input 从用户那里获取信息

txt = open (filename)


print "Here's your file %r:" % filename
print txt.read () #读取 txt 内容并打印

# 下面的部分是熟悉 raw_inpu
print "Type the filename again:"
file_again = raw_input(">")

text_again = open(file_again)

print text_again.read()
