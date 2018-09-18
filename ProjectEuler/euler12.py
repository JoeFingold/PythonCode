divisors = 0
summation = 0
trianglesize = 0

while divisors <= 500:
	divisors = 0
	summation = 0
	trianglesize += 1

	for i in range(1,trianglesize+1):
		summation += i

	for i in range(1,int(trianglesize**0.5)+1):
		if summation % i == 0:
			divisors += 2

	print trianglesize


print "done"








