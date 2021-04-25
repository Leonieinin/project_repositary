#1
import nltk
nltk.download('book')
from nltk.probability import FreqDist
Word = []
for w in 'sents(7)':
    Word.append(w)
def nice(Word):
    fdist = FreqDist(samples=Word) 
    for (word, freq) in fdist.most_common(n=5):
        print(word,len(word))
nice(Word)



#2
import nltk
nltk.download('genesis') 
from nltk.corpus import genesis
kjv = genesis.words('english-kjv.txt')
ws = []
for w in kjv:
    ws.append(w)
def lexical_diversity(ws):
    fdist = FreqDist(samples=ws) 
    for (word, freq) in fdist.most_common(n=5):
        print(word,len(word))
lexical_diversity(ws)