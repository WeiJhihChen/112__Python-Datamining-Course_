side=int(input('請輸入對邊：'))
another_side=int(input("請輸入斜邊："))

import math
radian = math.asin(side/another_side) #利用sin算出弧度
degree = math.degrees(radian) #弧度換算成角度
print(round(degree,ndigits=2)) #round=最接近整數 ndigits=小數點後幾位