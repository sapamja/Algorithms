# Combine two sorted lists into one sorted list
def combine(l1,l2):
	i = 0
	j = 0
	out = []
	p = 0
	while i < len(l1) and j < len(l2):
		p += 1
		if l1[i] <= l2[j]:
			out.append(l1[i])
			i += 1
		else:
			out.append(l2[j])
			j += 1
	
	if i >= len(l1) and j < len(l2):
		p += 1
		out.extend(l2[j:])
	
	elif j >= len(l2) and i < len(l1):
		p += 1
		out.extend(l1[i:])

	print p,len(l1)+len(l2)
	return out

l1 = [1,2,3,4,5,6,7,8]
l2 = [1,2,3,5,8,9,35]

# best case
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
print combine(l1,l2)

# worst case
l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]
print combine(l1,l2)

