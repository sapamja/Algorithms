'''
Choice of sorting algorithm depends on:
* How much data there is
* Does the data fit in memory
* Is the data mostly sorted
* Are there duplicate keys or values?
* What are the requirements for the sort?
* Should I optimize best, worst, or average case performance?
* Does the sort need to be stable?
* Is the largest size of data to be sorted bigger / smaller than available memory?


* How much additional memory does algorithm require
* Is relative order preserved

Selection sort
Insertion sort
Quick sort
Merge sort
Sort array of arrays according to multiple columns

Python functions for sorting:
http://wiki.python.org/moin/HowTo/Sorting/
* sorted(array) - any iterable
* array.sort() - only lists
* use key parameter to apply function before sorting
	key = lambda x: x[2]
* Use also itemgetter from operator module
	key = itemgetter(1) - to sort by 1st element
	key = itemgetter(1,2) - to sort first by 1st and then by 2nd
* use reverse=True to do descending order
* sorts in python are stable


'''

import math
import random

# O(n^2), inplace, nonstable, fewest swaps
# Find minimum in rest of array and swap
def selection_sort(array):
	
	for i in range(len(array)-1):
		# find minimum
		min_index = i
		for j in range(i+1,len(array)):
			if array[j] < array[min_index]:
				min_index = j
		# swap
		if min_index != i:
			array[i],array[min_index] = array[min_index],array[i]

	return array


# Insertion sort, best case O(n), worse O(n^2), inplace, stable, best for small datasets
def insertion_sort(array):
	for i in range(1,len(array)):
		j = i 
		while j > 0 and array[j] < array[j-1]:
			array[j],array[j-1] = array[j-1],array[j]
			j -= 1
	return array

# Quick sort
# Recursive sort 
# Not in place with extra arrays
def quicksort1(array):
	if len(array) <= 1:
		return array
	else:
		pivot_index = random.randrange(len(array))
		pivot = array.pop(pivot_index)
		low = []
		high =[]
		for x in array:
			if x >= pivot:
				high.append(x)
			else:
				low.append(x)

		return quicksort1(low)+[pivot]+quicksort1(high)


# Quicksort in place
def quicksort2(array):
	if len(array) <= 1:
		return array
	elif len(array) == 2:
		if array[0] > array[1]:
			array[0],array[1] = array[1],array[0]
			return array
		else:
			return array
	else:
		pivot_index = random.randrange(len(array))
		#pivot = array[pivot_index]
		pivot = array.pop(pivot_index)
		#pivot = 11
		print "pivot=",pivot
		h = len(array)-1
		l = 0
		while h > l:
			#print l,h,array[l],array[h]
			if array[l] >= pivot:
				if array[h] < pivot:
					array[l],array[h] = array[h],array[l]
					l += 1
					h -= 1
				elif array[h] >= pivot:
					h -= 1
			else:
				l += 1
		# it may be so that in last step when l=h, array[h] < pivot stays on right side
		# for example [1,2,5,4] for pivot=5, 4 will stay on right, to fix it check: 
		if l == h and array[h] < pivot:
			h += 1
			

		#print l,h
		#print array
		s = max(l,h)

		#print [l,h],s,array[0:s],array[s:]
		return quicksort2(array[0:s]) + [pivot] + quicksort2(array[s:])



# Combine two sorted lists
def combine(l1,l2):
	i = 0
	j = 0
	out = []
	
	while i < len(l1) and j < len(l2):	
		if l1[i] <= l2[j]:
			out.append(l1[i])
			i += 1
		else:
			out.append(l2[j])
			j += 1
	
	if i >= len(l1) and j < len(l2):
		out.extend(l2[j:])
	
	elif j >= len(l2) and i < len(l1):
		out.extend(l1[i:])


	return out

# Merge sort O(nlogn) - time, O(n) - memory (during list combine we need an extra array of size n)
# not stable, good for large data, efficiency predictable but needs a lot of memory
def merge_sort(array):
	#print array
	if len(array) == 1:
		return array
	elif len(array) == 2:
		if array[0] > array[1]:
			array[0],array[1] = array[1],array[0]
			return array
		else:
			return array
	else:
		pivot = int(math.floor(len(array)/2))
		return combine(merge_sort(array[0:pivot]),merge_sort(array[pivot:]))


# Multi key sort
def stable_sort(array):
	for i in range(len(array)):
		array[i] = (array[i],i)
	print array
	return sorted(array)


# 2 sorted arrays one with size X and another with size X+Y which has only Y elements.
# The rest is empty. Merge these arrays in to second array such that resultant
# array at end will be sorted.
def two_arrays_sort(x,y):
	i = len(x)-1
	j = 0
	while y[j+1] != None:
		j += 1
	k = len(y)-1
	while i >= 0 and j >= 0:
		if x[i] > y[j]:
			y[k] = x[i]
			k -= 1
			i -= 1
		else:
			y[k] = y[j]
			k -= 1
			j -= 1
	
	if j < 0:
		while i >= 0:
			y[k] = x[i]
			k -= 1
			i -= 1
	return y




# Pancake sort p 142
def flip(array,i,j):
	while i < j:
		array[i],array[j] = array[j],array[i]
		i += 1
		j -= 1
	return array

def pancake_sort(array):
	if len(array) <= 1:
		return array
	else:

		mi = 0
		m = 0

		# find maximum element and its index
		for i in range(len(array)):
			if array[i] > m:
				m = array[i]
				mi = i
		
		# Flip array accordingly
		if mi > 0 and mi < len(array)-1:
			array = flip(array,mi,len(array)-1)
			array = flip(array,0,len(array)-1)
		elif mi == len(array)-1:
			array = flip(array,0,len(array)-1)

		return [array[0]] + pancake_sort(array[1:])




s = [0,9,7,8,6,3,4,5,1,4,6,1]
print selection_sort(s)
s = [0,9,7,8,6,3,4,5,1,4,6,1]
print insertion_sort(s)
s = [0,9,7,8,6,3,4,5,1,4,6,1]
print quicksort1(s)
print "----"
s = [10,5,3]
print merge_sort(s)
print "----"
print stable_sort([3,2,2,1])
print "----"
x = [1,3,5,5,9]
y = [2,4,6,8,10,None,None,None,None,None]
print two_arrays_sort(x,y)
print "----"
#s = [1,9,3,5,7,3,6,10,11,2]
#s = []
#s = [1,1,1]
s = []
#print s
print quicksort2(s)
print "------"
s = [5,9,1,8,4,7,3]
print pancake_sort(s)


