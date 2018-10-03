# coding=utf-8
from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script) # 终端输入 python ex14.py qilin，output Hi qilin, I'm the ex14.py script.
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name

likes = raw_input (prompt) # 运行，并改变 promt 的值;这里让你填是否喜欢

print "Where do you live %s?" % user_name
lives = raw_input (prompt)

print "What kind of computer do you have?"
computer = raw_input (prompt)

print '''
Alright, so you said %r about liking me.
You live in %r, Not sure where that is.
And you have a %r computer. Nice.
''' % (likes, lives, computer)


# cost 15min
