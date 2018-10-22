import nltk

sentence_obama='Obama speaks to the media in Illinois'
sentence = nltk.sent_tokenize(sentence_obama) #tokenize sentences
nouns = [] #empty to array to hold all nouns

temp=nltk.pos_tag(nltk.word_tokenize(str(sentence)))

print(temp)
