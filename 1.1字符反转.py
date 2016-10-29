#! python2
# coding=utf-8
# 2016-10-6
# return直接可以调用到print中
def reverse(s):
	rt = ''
	for i in range(len(s)-1, -1, -1):
		rt += s[i]
	return rt


ta = raw_input('输入需要反转的字：')
print reverse(ta)
