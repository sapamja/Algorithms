# ----------------------------
# String pattern matchin
# ----------------------------
# Book p. 43
# 
# input: a text string t and a pattern string p
# output: does t contain the pattern p as a substring, and if so where?

# Be careful with the order of things in while loop!

def findmatch(t,p):
	
	lt = len(t)
	lp = len(p)
	
	for i in range(lt-lp):
		k = 0
		
		while k < lp and t[i+k] == p[k]:
			k += 1
		if k == lp:
			return i

	return(-1)


print findmatch('abcdefgh','deff')




