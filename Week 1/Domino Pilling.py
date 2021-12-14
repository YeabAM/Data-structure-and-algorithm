values = input()
x=values.split(" ")
if(1 <=int(x[0]) and int(x[0])<=int(x[1]) and int(x[1])<=16):
	num= (int(x[0])*int(x[1]))/2
	print(int(num))
