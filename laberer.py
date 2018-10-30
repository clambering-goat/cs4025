import nltk




'''
list of tags
CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when



'''













import open_traning_data

data=open_traning_data.open_data()
print("line1 ",data[1])

sentence1=(data[1][0])
sentence2=(data[1][1])


print("sentance 1",sentence1)
print("sentance 2",sentence2)
print(" ")

sentence_tocken1 = nltk.word_tokenize(sentence1) #tokenize sentences
sentence_tocken2 = nltk.word_tokenize(sentence2) #tokenize sentences

sentence_tagded1= nltk.pos_tag(sentence_tocken1)
sentence_tagded2= nltk.pos_tag(sentence_tocken2)

print(sentence_tagded1)


print("")

print(sentence_tagded2)
print("")


list_of_nousrs_for_s1=[]
for word in sentence_tagded1:
    if word[1]=="NN" or word[1]=="NNS" or word[1]=="NNP" or word[1]=="NNPS":
        list_of_nousrs_for_s1.append(word)

print ("list of nours ")
for q in list_of_nousrs_for_s1:
    print(q)

print ("list of nours 2")
list_of_nousrs_for_s2=[]
for word in sentence_tagded2:
    if word[1]=="NN" or word[1]=="NNS" or word[1]=="NNP" or word[1]=="NNPS":
        list_of_nousrs_for_s2.append(word)




for q in list_of_nousrs_for_s2:
    print(q)





