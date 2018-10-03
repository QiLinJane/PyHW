# coding=utf-8
print "How old are you?",
age = raw_input() # 不能填在这里，应该填在终端命令行。当脚本暂停，输入你的年龄。
print "How tall are you?",
height = raw_input ()
print "How much do you weight?",
weight = raw_input ()

print "so you're %r old, %r tall, and %r heavy." % (age, height, weight)

# cost 20min  