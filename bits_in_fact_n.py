import math
a=1
n=int(raw_input("enter n: "))
for i in range(n):
	a=a*(i+1)
	#print i+1,
print "Number of bits is: "+str(math.log(a,2))
