# --------------------------------------------
# Find first nonrepeated character in a string
# - consider also memory allocatio
# - Dofference in using an array or hash

# O(n^2) solution for each letter check all letters
def find_nonrepeat1(s):
	for i in range(len(s)):
		repeat = 0
		for j in range(len(s)):
			if s[i]==s[j]:
				repeat += 1
		if repeat == 1:
			return s[i]


# O(n)
def find_nonrepeat2(s):

	d = dict()
	for l in s:
		if l in d.keys():
			d[l] += 1
		else:
			d[l] = 1
	for l in s:
		if d[l] == 1:
			return l

s = "aaabbvcccc"
print find_nonrepeat1(s)
print find_nonrepeat2(s)

# --------------------------------------------
# Remove specified characters from string

# O(nm) solution
def remove1(inputstring,removecharacters):
	new_string = ""
	for l in inputstring:
		flag = 0
		for r in removecharacters:
			if r == l:
				flag = 1
				break
		if flag == 0:
			new_string += l
	return new_string


# O(n) solution using dictionary
# Better for short strings and when many possible charasters ie unicode
def remove2(inputstring,removecharacters):
	# Initialize and fill dictionary
	# O(n)
	d = dict()
	for l in inputstring:
		if l not in d.keys():
			d[l] = False
	

	# O(m) for each letter in remove list increment dictionary
	for l in removecharacters:
		if l in d.keys():
			d[l] = True


	# Go through the sentence once more
	# O(n)
	new_string = ""
	for l in inputstring:
		if not d[l]:
			new_string += l
	return new_string

# Implementation in array
# Better for long strings and not long list of characters ie ascii
# Needs an array for all possible characters
def remove3(inputstring,removecharacters):
	new_string = ""
	a = [False for i in range(256)]
	for l in removecharacters:
		a[ord(l)] = True
	for l in inputstring:
		if not a[ord(l)]:
			new_string += l
	return new_string


	

s = "ala ma kota i sie spieszy na autobus"
print 1,remove1(s,"aeiouy")
print 2,remove2(s,"aeiouy")
print 3,remove3(s,"aeiouy")



# -------------
# Reverse order of words in a string

# O(n)
def reverse_string(string):
	# strings are not mutable in python, so I need to use new string
	new_string = ""
	for s in string:
		new_string = s + new_string
	return new_string

# Assume we define words as something separated by spaces
def reverse_order_of_words(sentence):
	new_sentence = ""
	word = ""
	for i in range(len(sentence)):
		if sentence[i] != " ":
			word += sentence[i]
		else:
			new_sentence = word + " " + new_sentence
			word = ""
		
	new_sentence = word + " " + new_sentence
	return new_sentence[:-1]

# Reverse each word but sentence stays the same!
def reverse_words(sentence):
	#return reverse_order_of_words(reverse_string(sentence))
	return reverse_string(reverse_order_of_words(sentence))



# By hand O(n+m)
def reverse1(sentence):
	stack = []
	word = ""
	for l in sentence:
		if l != " ":
			word += l
		else:
			stack.append(word)
			word = ""
	stack.append(word)

	reversed_sentence = ""
	while len(stack) > 0 :
		reversed_sentence += stack.pop() + " "

	return reversed_sentence


# Using regular expressions and split function
def reverse2(sentence):
	stack = sentence.split()
	reversed_sentence = ""
	while len(stack) > 0 :
		reversed_sentence += stack.pop() + " "

	return reversed_sentence


s = "Ala ma kota i sie spieszy na autobus."
print 1,reverse1(s)
print 2,reverse2(s)

# ----------------
# Conversion

# String to integer
# Any numerics as string has such a asci code that 
# ord('num')-ord('0') = num
# String to digit
def convert1(str):
	neg = False
	value = 0
	for l in str:
		if l == "-":
			neg = True
		else:
			# Horner's rule
			value = value*10 + ord(l)-ord('0')
	if neg:
		return -1*value
	else:
		return value

# integer to string
def convert2(liczba):
	if liczba == 0:
		return 0
	else:
		if liczba < 0:
			neg = "-"
			liczba *= -1
		else:
			neg = ""


		string = ""
		d = liczba % 10

		while liczba != 0:
			str_d = chr(d + ord('0'))
			string = str_d + string
			liczba = (liczba - d)/10
			d = liczba % 10
		return neg+string


print convert1("-124")
print convert2(-14)

# --------------------------------
# Write a function to search for the existence
# of a string (target) in another string (str).
# The function takes two strings as the input and
# returns the index where the second string is found.
# If the target string cannot be found, then return -1

# By hand O(mn) solution
def search_string1(target,string):
	# If target longer than string
	if len(target) > len(string):
		print "Target longer than string"
		return None
	# If any of the strings is None
	elif target == None or string == None:
		print "One of the strings None"
		return None
	else:
		for i in range(len(string)-len(target)+1):
			for j in range(len(target)):
				if target[j] != string[i+j]:
					break
			if j == len(target)-1 and target[j] == string[i+j]:
				print "strings equal at:",i
				break
		
		if j == len(target)-1 and target[j] == string[i+j]:
			return i
		else:
			print "Substring does not exist"
			return None


s1 = 'baab'
s2 = 'aaaaaaab'
print search_string1(s1,s2)

# -----------------------------
# Convert path to absolute path 
# /home/abc/.././def/./ghi/../.

def convert_path(path):
	print path
	path = path.split("/")
	new_path = []
	for i in range(len(path)):
		if path[i] == ".":
			pass
		elif path[i] == "..":
			new_path.pop()
		else:
		 	new_path.append(path[i])
	
	#print new_path
	out_path = ""
	for s in new_path:
		out_path += s + "/"
	return out_path



s = "/home/abc/.././def/./ghi/../."
#print convert_path(s)


# -----------------------------
# Find the start position of the largest block of repeated characters
# If more than one block of same size, return first one
# O(n+m) memory 
def repeated1(string):
	if string == None:
		print "There is no string"
		return None
	if len(string) == 0:
		print "String is empty"
		return None
	else:
		previous = None
		letters = []
		counts = []
		start = []
		for i in range(len(string)):
			if previous == None or string[i] != previous:
				counts.append(1)
				letters.append(string[i])
				start.append(i)
			else:
				counts[len(counts)-1] += 1
			previous = string[i]		

		print counts
		print letters
		print start
		#return [[letters[i],j] for i,j in enumerate(counts) if j == max(counts)]
		print "For a string",string
		print "Maximum block starts at position",start[counts.index(max(counts))]
		print "Maximum block of letter",letters[counts.index(max(counts))]
		print "Maximum block length",max(counts)
		#return start[counts.index(max(counts))]

print repeated1('abbcccddddcccccaaaaaaffffff')
#print repeated1('')
#print repeated1(None)
#print repeated1('aabbcc')

# -------------------------
# Are two strings anagrams
# Complexity O(3n) = O(n)
def are_anagrams(s1,s2):
	if len(s1) != len(s2):
		print "Not anagrams, strings have different length"
		return False
	else:
		d1 = dict()
		d2 = dict()
		for s in s1:
			if s in d1.keys():
				d1[s] += 1
			else:
				d1[s] = 1
		for s in s2:
			if s in d2.keys():
				d2[s] += 1
			else:
				d2[s] = 1
		for k in d1.keys():
			if d1[k] != d2[k]:
				print "Not anagrams, different letter counts"
				return None
		print "Strings are anagrams"
		return True

s1 = "aaabbbccc"
s2 = "abcabcabc"
are_anagrams(s1,s2)
print "--------"
print reverse_string("ala ma kota")
print reverse_order_of_words("ala ma kota")
print reverse_words("ala ma kota")











