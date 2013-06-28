# ----------------------------
# Select sort
# ----------------------------
# Book p. 42
# Complexity n(n-1)/2 ~ O(n^2)
# The minimum time is the same, because it always have to check the 
# same number of elements

def selection_sort(l):
	for i in range(len(l)):
		
		index_min = i
		
		for j in range(i+1,len(l)):
			if l[j] < l[index_min]:
				index_min = j
		
		l[i], l[index_min] = l[index_min], l[i]

	return(l)

print selection_sort([5,12,1,7,3,2])
print selection_sort(["b","c","a"])