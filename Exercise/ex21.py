# coding=utf-8
def add(a, b):
	print "ADDING %d + %d " % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d -%d" % (a, b)
	return a - b
def multyply(a, b):
	print "MULTYPLYING %d * %d" %(a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multyply(90, 2)
iq = divide(100, 2)

print "Age: %d, height: %d, weight: %d, Iq: %d" % (age, height, weight, iq)

# a puzzle for th eextra credit , type it in anyway.

print "Here is a puzzle"

what = add(age, subtract(height, multyply(weight, divide(iq, 2))))

print "That become:  ", what, "can you do it by hand? "


 