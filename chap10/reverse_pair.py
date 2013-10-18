def reverse_pair():
	fin=open('words.txt')
	t=[]
	for line in fin:
		word=line.strip()
		t.append(word)

	for word in t:
		reverse=word[::-1]
		if reverse in t:
			print word, reverse 


reverse_pair()
