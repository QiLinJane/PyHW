# coding=utf-8
# 策略：写一个变量，打印；不需要全部写完再打印
tabby_cat = "\tI'm tabbed in." # 终端显示:加不加\t 都可以完整显示I'm tabbed in.
persian_cat = "I'm split\non a line." #复习前面一个练习 \n
backslash_cat = "I'm \\ a \\ cat." # I'm \ a \ cat.为什么非要双反斜杠？单反斜杠同样能打印出来

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat

print fat_cat

# 超级喜欢\t 这个水平制表符（tab）

# 试一下 \'(单引号) 和 \" (双引号)

print "I am 6'2\" tall."  # 6寸2分，这句话中四个引号难以区分谁是真正的引号，所以要人为标出来，以免程序识别错误
print 'I am 6\'2" tall.' 

# 此练习最关键的是最后两个 print;
# cost 30min

