# 检查两个字符串相等和不等
car_1 = 'audi'
car_2 = 'bwm'
if car_1 == car_2:
    print("不执行")
if car_1 != car_2:
    print('执行')


# 使用函数lower()的测试
car = 'audi'
if car.lower() == 'audi':
    print('执行')
if car.lower() != 'audi':
    print('不执行')

# 检查两个数相等、不等、小于、大于等于和小于等于
number_1 = 416
number_2 = 504
if number_1 == number_2:
    print("相等")
if number_1 != number_2:
    print("不等")
if number_1 > number_2:
    print('大于')
if number_1 < number_2:
    print('小于')
if number_1 >= number_2:
    print('大于等于')
if number_1 <= number_2:
    print('小于等于')

# 使用关键字and和or的测试
number_1 = 416
number_2 = 504
char_1 = 'LZIT'
char_2 = 'HIT'
if (number_1 < number_2) and (char_1 != char_2):
    print(f"I love {char_2.upper()}!")
if (number_1 != number_2) or (char_1 != char_2):
    print(f"\nI love {char_1.upper()}!")

# 测试特定的值是否包含在列表中
schools = ['LZIT','BTBU','HIT']

if 'HIT' in schools:
    print("I love it!")
if 'HIT' not in schools:
    print(schools[0:])
