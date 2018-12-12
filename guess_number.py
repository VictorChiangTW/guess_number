import random
x = random.randint(1,100)
# print(x)
while True:
	anw = int(input("請猜一個數字"))
	if anw > x:
		print("比答案大")
	elif anw < x:
		print("比答案小")
	else:
		print("終於猜對了！")
		break