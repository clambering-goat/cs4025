 # Simple usage
from stanfordcorenlp import StanfordCoreNLP
import teasting
import re




teasts=teasting.teast()

import open_traning_data
data=open_traning_data.open_data()


nlp = StanfordCoreNLP(r'./stanford-corenlp-full-2018-10-05')


counter={}

for test_time in range(4927):

    data=teasts.full_teast()


    sentence1=(data[0])
    sentence2=(data[1])

    #full stop remover
    if sentence1[-1]==".":
        sentence1=sentence1[0:-2]
    if sentence2[-1]==".":
        sentence2=sentence2[0:-2]



    sentance1_split=re.split(" |,|'",sentence1)
    sentance2_split=re.split(" |,|'",sentence2)
    # depencper count "," bracking code

    print("sentance 1",sentence1)
    print("sentance 2",sentence2)
    print(" ")

    s1_dependonsy=nlp.dependency_parse(sentence1)
    s2_dependonsy=nlp.dependency_parse(sentence2)

    for q in s1_dependonsy:
        if q[0] in counter.keys():
            counter[q[0]]=counter[q[0]]+1
        else:
            counter[q[0]]=1


for q in counter:
    print ('counter:',q," ",counter[q] )

nlp.close()  # Do not forget to close! The backend server will consume a lot memery.