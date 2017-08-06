# -*- coding: utf-8 -*-

from sys import argv # 导入参数变量

script, filename = argv # unpack解包，一一对应

txt = open(filename) # open一个脚本文件

print "Here's your file %r:" % filename
print txt.read() #read(),执行打开文件
print txt.close()

print "I'll also ask you to type it again:"
file_again = raw_input("> ") #说明raw_input用途

txt_again = open(file_again)

print txt_again.read()
print txt_again.close()
