import nltk




sentence_obama='Obama speaks to the media in Illinois'

sentence = nltk.word_tokenize(sentence_obama) #tokenize sentences


temp= nltk.pos_tag(sentence)

print(temp)
