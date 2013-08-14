import math
# http://www.youtube.com/playlist?list=PLTZbNwgO5ebqUqZ73C7K-TzchejHanwMB


# Binary search on sorted array of integers
# Return an index
def binary_search_with_recursion(array,a1,a2,x):
	# Check if array is empty
	# Check if x is not None
	# Check if array is sorted if not sort it
	# Check order of sorting descending or ascending
	# if descending then reverse order of array
	# Check if number is not outside of array
	# If all good:

	# select middle element
	if len(array[a1:a2]) == 0:
		print x,"is not in array"
		return None
	else:
		m = int(math.floor((a1+a2)/2))
		#print array[m],a1,a2,array[a1:a2]
		if x == array[m]:
			return m
		elif x < array[m]:
			return binary_search_with_recursion(array,a1,m,x)
		else:
			return binary_search_with_recursion(array,m+1,a2,x)

# Same as above but without recursion
def binary_search(array,x):
	a1 = 0
	a2 = len(array)-1
	while a1 != a2:
		m = int(math.floor((a1+a2)/2))
		if x == array[m]:
			return m
		elif x < array[m]:
			a2 = m
		else:
			a1 = m+1
	if a1 == a2:
		print x,"is not in the array"
		return None



a = [0,1,2,4,6,8,10,11,12,13,14]
print binary_search_with_recursion(a,0,11,3)
print binary_search(a,3)


# ------------------------
# Permitation of a string - all possible orderings of letters
# http://www.youtube.com/watch?v=MQcwxQK2DPA

# Recursive - awsome algorithm
def permutation(array,k):
	# Strings in python are immutable so I will put string as array
	n = len(array)
	if k == n-1:
		print array
	else:
		for i in range(k,n):
			array[i],array[k] = array[k],array[i]
			permutation(array,k+1)
			array[i],array[k] = array[k],array[i]

#a = [1,2,3]
#permutation(a,0)

# --------------------------
# Combinations of a string from length 1 to n
# eg. 123-> 1,2,3,12,13,23,123
# http://www.youtube.com/watch?v=p8SDPaX1wgw&list=PLTZbNwgO5ebqUqZ73C7K-TzchejHanwMB&index=9

# This solution is building recursively a tree with 0 and 1 branches
# every time it is time to add 1, we add to array a letter i from string 
# if we are at 0, we do not add anything
def combination(string,array,i):
	# stop condition
	if i >= len(string):
		print array
	# recursion
	else:
		# Need to make copy of arrays because otherwise it becomes a mess
		a1 = array[:]
		a2 = array[:]
		a2.append(string[i])
		combination(string,a1,i+1)
		combination(string,a2,i+1)

# Create all binary numbers up to 2**n	
def bin_tree(array,i,n):
	if i >= n:
		print array
	else:
		a1 = array[:]
		a2 = array[:]
		a1.append(0)
		a2.append(1)
		bin_tree(a1,i+1,n)
		bin_tree(a2,i+1,n)

print "------"
#a = [1,2,3,4]
#combination3(a)
#s = [1,2,3,4]
#combination(s,[],0)
#bin_tree([],0,3)


# Transform a phone number into word p.119
def digit_to_letter(digit,place):
	# digit 0-9
	# letter a-y
	converter = [
	["0"],
	["1"],
	["a","b","c"],
	["d","e","f"],
	["g","h","i"],
	["j","k","l"],
	["m","n","o"],
	["p","r","s"],
	["t","u","v"],
	["w","x","y"]]
	return converter[digit][place]

def phone_to_word(phone_number,word,i):
	if i >= len(phone_number):
		print word
	else:
		w1 = word[:]
		w2 = word[:]
		w3 = word[:]
		digit = phone_number[i]
		if digit == 0 or digit == 1:
			w1.append(digit_to_letter(digit,0))
			phone_to_word(phone_number,w1,i+1)
		else:
			w1.append(digit_to_letter(digit,0))
			w2.append(digit_to_letter(digit,1))
			w3.append(digit_to_letter(digit,2))
		
			phone_to_word(phone_number,w1,i+1)
			phone_to_word(phone_number,w2,i+1)
			phone_to_word(phone_number,w3,i+1)


# nonrecursive
def fibonacci_series(n):
	f1 = 0
	f2 = 1
	for i in range(2,n+1):
		
		f3 = f1+f2
		f1 = f2
		f2 = f3
		#print i,f3
	return f3

# analytical
def fib_series(n):
	# golden ratio
	g = (1+math.sqrt(5))/2
	return (g**n - (-g)**(-n))/math.sqrt(5)

# recursive
def fib(n):
	if n < 2:
		return n
	else:
		return fib(n-1)+fib(n-2)



print fibonacci_series(8)
print fib_series(8)
print fib(8)

#phone_to_word([2,2,3,4,3,1,7],[],0)












