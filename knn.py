from math import sqrt


a = int(input("Enter x-coordinate: "))
b = int(input("Enter y-coordinate: "))


tinitial = (a,b)

print("t-initial =", tinitial)

n = int(input("Enter Number of Coordinate Pairs: "))

def setdef():
	p = 0
	global x,y
	x = int(input("Enter x-coordinate: "))
	y = int(input("Enter y-coordinate: "))
	p += 1
	t = (x,y)
# 		print("t",p,"=",t)

def formula():
	for i in range(n):
		t=setdef()
		print(sqrt(((a-x)**2)+((b-y)**2)))

formula()
