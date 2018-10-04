# coding=utf-8

print "Let's practis everything."
print 'You\'d need to know \'bout escapes with \\that do \n newlines and\t tabs'  # 需要斜杠吗？\t 什么意思 空格？

poem = """
\tThe lovely world 
with logic so firmly planted
cannot discer \n th enedds of love
nor comprehend passion from intuition
adn requires an explanation
\n\t\twhere there is none.

"""
# \t\t?

print "-------------"
print poem
print "-------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_fomula(started):
	beans = started * 500
	jars = beans / 1000
	crates = jars / 100
	

start_point = 10000
beans, jars, crates = secret_fomula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)


start_point = start_point / 10

print "We'd have %d beans, %d jars, and %d crates." % secret_fomula(start_point)



