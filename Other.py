#fizbuzz
# Using any language you want (even pseudocode), write a program or
# subroutine that prints the numbers from 1 to 100, each number on a
# line, except for every third number write "fizz", for every fifth
# number write "buzz", and if a number is divisible by both 3 and 5 write "fizzbuzz".

import math

def fizzbuzz():
	for i in range(1,101):
		if i % 3 == 0 and i % 5 == 0:
			print "fizzbuzz"
		elif i % 3 == 0:
			print "fizz"
		elif i % 5 == 0:
			print "buzz"
		else:
			print i


#fizzbuzz()


# Calculate a derivative of a polynomial
class Term:
	def __init__(self,coef,power):
		self.coef = coef
		self.power = power

	def __str__(self):
		if self.power == 0:
			return str(self.coef)
		elif self.power == 1:
			return str(self.coef) + "x"
		else:
			return str(self.coef)+"x^"+str(self.power)

	def D(self):
		if self.power == 0:
			return Term(0,0)
		else:
			return Term(self.coef*self.power,self.power-1)

class Polynomial:
	def __init__(self):
		self.equation = []

	def add_term(self,coef,power):
		self.equation.append(Term(coef,power))

	def D(self):
		derivative = Polynomial()
		for t in self.equation:
			new_term = t.D()
			if new_term.coef != 0:
				derivative.add_term(new_term.coef,new_term.power)
		return derivative

	def __str__(self):
		if len(self.equation) == 0:
			return "0"
		else:
			out_str = ""
			for t in self.equation:
				if t.coef < 0:
					tn = Term(-t.coef,t.power)
					out_str += " - " + tn.__str__()
				else:
					out_str += " + " + t.__str__()
			if out_str[1] == "-":
				return out_str
			else:
				return out_str[3:]

#t = Term(2,0)
#print t
f = Polynomial()
f.add_term(-2,3)
f.add_term(5,2)
f.add_term(-1,1)
f.add_term(5,0)
d = f.D()
s = d.D()
print f
print f.D()
print f.D().D()
print f.D().D().D()
print f.D().D().D().D()

# This checks each number if it is divisible
def prime1(n):
	print 1
	print 2
	i = 2
	num = 3
	while i < n:
		not_prime = False
		for div in range(2,int(math.sqrt(num)+1)):
			if num % div == 0:
				num += 2
				not_prime = True
				break
		if not_prime == False:
			print num
			i += 1
			num += 2

# Find all primes up to n
def prime2(n):
	primes = []
	primes.append(1)
	primes.append(2)
	array = [True]*n
	i = 2
	while i < n:
		x = 2
		p = x*i
		while p < n:
			array[p] = False
			x += 1
			p = x*i
		i += 1
		if array[i] == True:
			array.append(i)

	print primes		


def square_root(x):
	guess = (1.+x)/2.
	while (guess*guess - x) > 0.01:
		guess = (guess + x/guess)/2.
		print guess
	return guess

# Given n intervals (xi,yi), find maximum number of overlapping intervals
# Given as [[],[],[],[],...]
def overlapping_intervals(array):
	n = len(array)
	start = []
	stop = []
	for s in array:
		start.append(s[0])
		stop.append(s[1])
		start = sorted(start)
		stop = sorted(stop)

	i = 0
	j = 0
	max = 0
	c = 0
	while i < n:
		if start[i] < stop[j]:
			c += 1
			if c > max:
				max = c
			i += 1
		else:
			c -= 1
			j += 1

	print max

def n2s(n):
	return chr(n + ord('a') - 1)

def translate(array):
	out = ""
	for n in array:
		out += n2s(n)
	return out

# numbers to strings!
def num2string(string,array,k):
	#print array
	#print k
	n = len(string)
	if k == n:
		print array
		#print translate(array)
	else:
		if string[k-1] <= 9:
			a = array[:]
			a.append(string[k])
			num2string(string,a,k+1)
			b = array[:]
			b[-1] = b[-1]*10+string[k]
			if b[-1] <= 24:
				num2string(string,b,k+1)
		else:
			a = array[:]
			a.append(string[k])
			num2string(string,a,k+1)




print "---"
num2string([1,1,1,1,1],[1],1)



#prime1(10)
#prime2(20)
#print square_root(1024)

#overlapping_intervals([[1,10],[1,5],[2,3],[2,7]])
#overlapping_intervals([[1,10],[2,7]])








