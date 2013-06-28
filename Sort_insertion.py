# ----------------------------
# Insertion sort
# ----------------------------
# Book p. 43
# Complexity n(n-1) ~ O(n^2)

def insertion_sort(l):
	for i in range(1,len(l)):
		j = 1
		while j > 0 and l[j]<l[j-1]:
			l[j], l[j-1] = l[j-1], l[j]
			j -= 1
	return l

print insertion_sort([5,12,1,7,3,2])
print insertion_sort(["b","c","a"])