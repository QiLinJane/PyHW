# coding=utf-8
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

# we could do thes two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file) # exists 这个命令将文件字符串作为参数，文件存在则返回True;学会通过 import 调用它

print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'write')
out_file.write(indata)

print "Alright, all done"

out_file.close()
in_file.close()

