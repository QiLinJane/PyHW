# coding=utf-8

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True) # 必须大写
print formatter % (formatter, formatter, formatter, formatter)

print "wo ui" # 想知道双引号是否打印
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

