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
# s1 = 72 #上月成绩
# s2 = 85 #本月成绩
# r = (s2/s1-1)*100
# print('{0}成绩提成了：{1:.1f}%'.format('小明',r))

#list Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
# classmates = ['Xiaoming','Xiaohong','Xiaogang']
# print(classmates)
# print(len(classmates))
# print(classmates[0])#Xiaoming
# print(classmates[-1])#Xiaogang
# #在list中追加元素
# classmates.append('老师')
# print(classmates)#['Xiaoming', 'Xiaohong', 'Xiaogang', '老师']
# classmates.insert(1,'校长')
# print(classmates)#['Xiaoming', '校长', 'Xiaohong', 'Xiaogang', '老师']
# #删除list末尾的元素
# print(classmates.pop())#老师
# print(classmates)#['Xiaoming', '校长', 'Xiaohong', 'Xiaogang']
# #要删除指定位置的元素，用pop(i)方法，其中i是索引位置
# print(classmates.pop(1))#校长
# print(classmates)#['Xiaoming', 'Xiaohong', 'Xiaogang']
# #要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
# classmates[1] = '小敏'
# print(classmates)#['Xiaoming', '小敏', 'Xiaogang']

# list里面的元素的数据类型也可以不同，比如：
# L = ['Apple',123,True]
# print(L)

# list元素也可以是另一个list，比如：
# s = ['python','java',['asp','php'],'scheme']
# print(len(s))#4
# print(s)#['python', 'java', ['asp', 'php'], 'scheme']
# #拆开等同于
# p = ['asp','php']
# s = ['python','java',p,'scheme']
# print(len(s))#4
# print(s)#['python', 'java', ['asp', 'php'], 'scheme']

#tuple 有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
#...

#练习
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])#Apple

#条件判断
# birth = input('birth:')#birth出生
# birth = int(birth)
# if birth < 2000: print('00前')
# else : print('00后')

# 练习
# h = 1.70
# w = 77
# BMI = w/(h*h)
# print(BMI)
# if BMI <= 18.5:
#     print('过轻')
# elif BMI <= 25:
#     print('正常')
# elif BMI <= 28:
#     print('过重')
# elif BMI <= 32:
#     print('肥胖')
# else :
# #elif BMI > 32:
#     print('严重肥胖')

#循环
# names = ['小明','小红','小刚']
# for name in names:
#     print(name)#依次输出list里的内容

# sum = 0
# for x in [1,2,3,4,5,6,7,8,9,10]:
#     sum = sum + x
# print(sum)#55

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)#5050

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)#2500

# 练习
# L = ['小明','小红','小刚']
# for l in L:
#     print('我是：',l)

# n = 1
# while n <= 100:
#     # if n > 10:
#     #     break
#     print(n)
#     n = n + 1
# print('END')

# n = 0
# while n < 10:
#     n = n + 1
#     # if n % 2 == 0:
#     #     continue
#     print(n)

#dict和set
# names = ['Michael', 'Bob', 'Tracy']
# scores = [95, 75, 85]

# d = {'Michael': 95,'Bob': 75,'Tracy': 85}
# print(d['Michael'])

# 'Thomas' in d
# d.get('Thomas')
# print(d.get('Thomas',-1))

# s = set([1,1,2,2,3,3])
# print(s)#{1, 2, 3}
# s.add(4)
# print(s)#{1, 2, 3, 4}
# s.add(4)
# print(s)#{1, 2, 3, 4}
# s.remove(4)
# print(s)#{1, 2, 3}

# 两个集合的交集与并集
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)#{2, 3}
print(s1 | s2)#{1, 2, 3, 4}

a = 'abc'
b = a.replace('a', 'A')
print(a)#abc
print(b)#Abc



