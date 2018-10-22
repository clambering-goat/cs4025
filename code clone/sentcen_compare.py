from gensim.models import Word2Vec
from nltk.corpus import brown
b = Word2Vec(brown.sents())
temp=b.most_similar('money', topn=5)
print(temp)
