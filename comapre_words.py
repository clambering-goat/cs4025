import gensim.downloader as api


word_vectors = api.load("glove-wiki-gigaword-100")





sim=word_vectors.similarity("big","small")


print(sim)
