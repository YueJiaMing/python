# a_age = 17
# b_age = 19
#
# if a_age > 18:
#     print('a您今年', a_age, '岁，已成年')
# elif a_age < 18:
#     print('a您今年', a_age, '岁，未成年')
# else:
#     print('a您今年18岁')
#
# if b_age > 18:
#     print('b您今年', b_age, '岁，已成年')
# elif b_age < 18:
#     print('b您今年', b_age, '岁，未成年')
# else:
#     print('b您今年18岁')


# 改进代码 -- 用户输入年龄
age = 15
age = int(input("请输入年龄："))
if age >= 18:
    print('成年')
else:
    print("您未成年")
