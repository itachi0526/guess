start = input('請輸入你想要的開始值：')
end = input('請輸入你想要的結束值：')
start = int(start)
end = int(end)

import random
r = random.randint(start, end)
a = 0

while True:
    num = input('猜個數字： ')
    num = int(num)
    a = a + 1
    print('猜了', a, '次')
    if num == r:
        print('猜對了ㄛ！')
        break
    elif num < r:
        print('數字再大一點')
    elif num > r:
        print('數字再小一點') 