def interlock():
	fin=open('words.txt')
	t=[]
	for line in fin:
		word = line.strip()
		t.append(word)

	for word in t:
		word1= word[::2]
		new_word=word[1:]
		word2=new_word[::2]

		if word1 in t and word2 in t:
			print word1,word2, word
