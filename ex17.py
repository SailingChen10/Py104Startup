# -*- coding: utf-8 -*-
# import argv
# inport exists
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# 打开文件，只读文件
input = open(from_file)
indata = input.read()

# len()字节长度
print "The input file is %d bytes long" % len(indata)
# exists,存在与否,ture or false
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."

# raw_input()输入设置，任何
raw_input()

# 'w'以write的模式打开文件
output = open(to_file, 'w')
# 在output文件中write indata 参数
output.write(indata)

print "Alright, all done."
# 关闭output文件
output.close()
# 关闭input文件
input.close()
