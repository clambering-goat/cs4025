from nltk.corpus import wordnet as wn
#import nltk
#nltk.download('wordnet')
res=wn.synset('locomotive.n.01').lemma_names()
print (res)
