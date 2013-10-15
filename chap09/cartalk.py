def odometer():
	for i in range(100000,1000000):
		s=str(i)
		if s[-1]!=s[-4] or s[-2]!=s[-3]:
			continue
		x=i+1
		s=str(x)
		if s[1]!=s[-1] or s[2]!=s[-2]:
			continue
		x+=1
		s=str(x)
		if s[1]!=s[-2] or s[2]!=s[-3]:
			continue
		x+=1
		s=str(x)
		if s[0]!=s[-1] or s[1]!=s[-2] or s[2]!=s[3]:
			continue

		print i

def triple_double():
	fin=open('words.txt')
	for line in fin:
		word=line.strip()
		if len(word)<6:
			continue
		for i in range(len(word)-5):
			if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
				print word

triple_double()

