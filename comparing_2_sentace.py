import gensim.downloader as api
import teasting
import re
word_vectors = api.load("glove-wiki-gigaword-100")


import open_traning_data



upper=0

lower=0

chang1=0
change2=0
lern_rate=0.01
loops=100
old_score=0
for loop1 in range(loops):
    for loop2 in range(loops):
        for loop3 in range(loops):
            for loop4 in range(loops):
                print("loop ",loop1+loop2+loop3+loop4)
                data = open_traning_data.open_data()

                teasts = teasting.teast()
                for test_time in range(4927):
                    chang1=loop1/100-loop2/100
                    change2=loop3/100-loop4/100
                    data=teasts.full_teast()


                    sentence1=(data[0])
                    sentence2=(data[1])

                    #full stop remover
                    if sentence1[-1]==".":
                        sentence1=sentence1[0:-2]
                    if sentence2[-1]==".":
                        sentence2=sentence2[0:-2]

                    #sentence1="A girl from Asia, in front of a brick window, looks surprised"

                    #sentence2="A person is riding the bicycle on one wheel"

                    sentance1_split=re.split(" |,|'",sentence1)
                    sentance2_split=re.split(" |,|'",sentence2)


                    #print("sentance 1",sentence1)
                    #print("sentance 2",sentence2)
                    #print(" ")

                    #sentence_obama = 'Obama speaks to the media in Illinois'.lower().split()
                    #sentence_president = 'The president greets the press in Chicago'.lower().split()

                    similarity = word_vectors.wmdistance(sentance1_split, sentance2_split)

                    if similarity<1+chang1:
                        teasts.guss("NEUTRAL")
                    if similarity>1-chang1 and similarity < 3.7+change2:
                        teasts.guss("CONTRADICTION")
                    if similarity>3.7-change2:
                        teasts.guss("ENTAILMENT")
                    #print("{:.4f}".format(similarity))
                score=teasts.got_right/(teasts.got_right+teasts.got_wrong)
                #print("score for vaules",chang1,change2)

                if score>old_score:
                    old_score=score
                    print("best vaule fround are ")
                    print("chage1",chang1)
                    print("chage2",change2)
                    print("score ", score)
