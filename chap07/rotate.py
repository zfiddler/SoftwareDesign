def rotate_word(word,n):
	""" rotates word by n letters

		word: string
		n: number of letters to rotate (int)

		Returns: string
	"""
	word = word.upper()
	new_word=''
	for i in word:
		val=ord(i)-64
		new_val=(val+n)%26+64
		letter=chr(new_val)
		new_word=new_word+letter

	return new_word

print rotate_word('Q. Do female frogs croak? A. Paul Lynde: If you hold their little heads under water long enough.', 13)
