"""
数据类型：
数值（int整形，float浮点型）
布尔型（True真False假）
str（字符串）
list（列表）
tuple（元祖）
set（集合）
dict（字典）
"""
"""
1.按经验将不同变量存储不同的类型的数据
2.验证这些数据到底是什么类型 -- 检测数据类型  --type(数据)
"""
num1 = 1
num2 = 1.1

# type(num1)
print(type(num1))
# 'int'
print(type(num2))
# 'float'

a = 'hello world'
print(type(a))
# 'str'

b = True
print(type(b))
# 'bool' -- 布尔型，通常判断使用，两个值 True False

c = [10, 20, 30]
print(type(c))
# 'list' -- 列表

d = (10, 20, 30)
print(type(d))
# 'tuple' -- 元祖

e = {10, 20, 30}
print(type(e))
# 'set' -- 几个

f = {'name': 'TOM', 'age': 18}
print(type(f))
# 'dict' -- 字典 -- 键值对










