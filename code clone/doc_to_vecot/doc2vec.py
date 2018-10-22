


from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
model= Doc2Vec.load("d2v.model")
#to find the vector of a document which is not in training data
test_data = word_tokenize("I love chatbots".lower())
v1 = model.infer_vector(test_data)

test_data2 = word_tokenize("I love chatbots".lower())
v2 = model.infer_vector(test_data)

print("V1_infer", (v1))

print("v2 infier",v2)
# to find most similar doc using tags
#similar_doc = model.docvecs.most_similar('1')
#print(similar_doc)


#print(model.docvecs['1'])
