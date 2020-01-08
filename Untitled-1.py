#!/usr/bin/env python3
#print('holler word')
#print(1+2)

#print('The quick brown fox', 'jumps over', 'the lazy dog')
#print(100 + 200)
#print('100 + 200 =',100+200)

#name = input()
#print('Hello,', name)

#name = input('please enter your name:')
#print('hello,',name)

#打印整数的绝对值
#a = 100
#if a >=0:
#    print(a)
#else:
#    print(-a)

#转义(\)与不转义(r)
#print('I\'m \"ok\"!')
#print('I\'m learning\nPython.')
#print('\\\t\\')
#print(r'\\\t\\')

#print(r'''hello,\n
#word''')

# 添加注释Ctrl+K 删除注释Ctrl+U
# age = 19
# if age > 18 :
#    print('太老')
# else :
#    print('年轻')

# a = 123 #a是整数
# print(a)
# a = 'ABC' #a变为字符串
# print(a)

# 上面是动态变量，下面为静态变量，当变量a已经被定义为整数型，如果赋值的时候类型不匹配，就会报错
# a = 123
# a = "abc"
# print(a)

# x = 10
# x = x + 2
# print(x) #x=12

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(a) #XYZ
# print(b) #ABC

#在Python中，有两种除法，一种除法是 /;/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
# >>> 10/3
# 3.3333333333333335
# >>> 9/3
# 3.0
#还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
# >>> 10//3
# 3
# 余数运算，可以得到两个整数相除的余数
# >>> 10%3
# 1

# 练习
# n = 123
# f = 456.789
# s1 = 'Hello,Word'
# s2 = 'Hello,\'Adam\''
# s3 = r'Hello,"Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print(n,f,s1,s2,s3,s4)

#https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896

#格式化函数：format()
s1 = 72 #上月成绩
s2 = 85 #本月成绩
r = (s2/s1-1)*100
print('{0}成绩提成了：{1:.1f}%'.format('小明',r))

#hhh
