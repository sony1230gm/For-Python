

# 階乘

# 輸入
num = int(input("輸入數值(1-100): "))
factorial = 1


# 數字判別，不得為負數、0、及大於100


if num < 0:
   print("負數沒有在階乘的啦")

elif num == 0:
   print("0 的階乘就是 1 知道沒~~")

elif num > 100:
   print(" 100以上太大了不想算.... ")



else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("%d 的階乘是 %d" %(num,factorial))



