def power(a,n):
	if n==0:
		return 1
	else:
		if n % 2 == 0:
			return power(a,n/2)**2
		else:
			return a*power(a,(n-1)/2)**2

print power(3,4)