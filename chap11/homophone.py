"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

def read_dictionary(filename='c06d.txt'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d


def homophone():
    d=read_dictionary()  #dictionary of words as keys, pronunciations as values
    fin =open('words.txt')
    t=[]    #list of final values
    for word in fin:
        word=word.strip()
        if len(word)!=5:
            continue
        hom1=word[1:]
        hom2=word[0]+word[2:]
        if hom1 in d and hom2 in d:
            if d[hom1]==d[hom2]:
                t.append([word,hom1,hom2])


    return t

print homophone()






