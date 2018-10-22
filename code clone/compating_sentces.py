d1 = "plot: two teen couples go to a church party, drink and then drive."
 d2 = "films adapted from comic books have had plenty of success , whether they're about superheroes ( batman , superman , spawn ) , or geared toward kids ( casper ) or the arthouse crowd ( ghost world ) , but there's never really been a comic book like from hell before . "
 d3 = "every now and then a movie comes along from a suspect studio , with every indication that it will be a stinker , and to everybody's surprise ( perhaps even the studio ) the film becomes a critical darling . "
 d4 = "damn that y2k bug . "
 documents = [d1, d2, d3, d4]






 import nltk, string, numpy
 nltk.download('punkt') # first-time use only
 stemmer = nltk.stem.porter.PorterStemmer()
 def StemTokens(tokens):
     return [stemmer.stem(token) for token in tokens]
 remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
 def StemNormalize(text):
     return StemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

 from sklearn.feature_extraction.text import CountVectorizer
 LemVectorizer = CountVectorizer(tokenizer=LemNormalize, stop_words='english')
 LemVectorizer.fit_transform(documents)

 
