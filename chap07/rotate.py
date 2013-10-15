def rotate_word(word,n):
	""" rotates word by n letters

		word: string
		n: number of letters to rotate (int)

		Returns: string
	"""
	word = word.upper()
	new_word=''
	for i in word:
		if ord(i)<65 or ord(i)>91:
			new_val=val
		else:
			val=ord(i)-64
			new_val=(val+n)%26+64
		letter=chr(new_val)
		new_word=new_word+letter

	return new_word

print rotate_word('V unq ab vqrn gung EBG13 jnf bevtvanyyl hfrq va HFRARG tebhcf gb boshfpngr fcbvyref naq bssrafvir pbagrag. V nyjnlf gubhtug EBG13 jnf whfg n wbxr (“zl arj 2EBG13 rapelcgvba fpurzr…”) be n gbby va trqnaxra rkcrevzragf (“vs V EBG13 zl svyrf, pbhyq V fhr gur tbireazrag haqre gur QZPN vs gurl fhocbran naq qrpelcg gurz?”).', 13)

