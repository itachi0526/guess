import random
r = random.randint(1, 100)
a = 0
while True:
    num = input('猜個數字： ')
    num = int(num)
    a = a + 1
    print('一共猜了', a, '次')
    if num == r:
        print('猜對了ㄛ！')
        break
    elif num < r:
        print('數字再大一點')
    elif num > r:
        print('數字再小一點') 