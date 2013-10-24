def rotate_word(word,n):
	""" rotates word by n letters

		word: string
		n: number of letters to rotate (int)

		Returns: string
	"""
	word = word.lower()
	new_word=''
	for i in word:
		if ord(i)<97 or ord(i)>122:
			new_val=ord(i)
		else:
			val=ord(i)-96
			new_val=(val+n)%26+96
		letter=chr(new_val)
		new_word=new_word+letter

	return new_word

def rotate_pairs():
	fin=open('words.txt')
	pairs = dict()
	d=dict()
	for line in fin:
		word=line.strip()
		d[word]=[]
	for word in d:
		for i in range(25):
			new=rotate_word(word,i+1)
			if  new in d and new not in pairs:
				pairs[new]=word
				print 'found'

	return pairs

print rotate_pairs()


	