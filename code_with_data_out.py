 # Simple usage
from stanfordcorenlp import StanfordCoreNLP
import teasting
import re
import gensim.downloader as api


word_vectors = api.load("glove-wiki-gigaword-100")




import open_traning_data
data=open_traning_data.open_data()


nlp = StanfordCoreNLP(r'./stanford-corenlp-full-2018-10-05')


sentece_we_got_wong=[]
for q in range(50):

    teasts = teasting.teast()
    senthace_simaly_thershold=q/10
    print("theshold used is ",q/10)
    for test_time in range(30):

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
        # depencper count "," bracking code

        #print("sentance 1",sentence1)
        #print("sentance 2",sentence2)
        #print(" ")

        s1_dependonsy=nlp.dependency_parse(sentence1)
        s2_dependonsy=nlp.dependency_parse(sentence2)

        #print ('Dependency Parsing:', s1_dependonsy)


        #print("#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{}}}}}}}}}}}}}}}}}}}}}}}}}}}\n")
        #print("Dependency Parsing 1 ", s1_dependonsy, "\n")
        #print("Dependency Parsing 2 ", s2_dependonsy, "\n")



        s1_subgect_dempndsy=[]
        for q in s1_dependonsy:

            if q[0]=="nsubj":
                place1=q[1]-1
                place2=q[2]-1
                s1_subgect_dempndsy.append((sentance1_split[place1], sentance1_split[place2]))



        s2_subgect_dempndsy=[]
        for q in s2_dependonsy:

            if q[0]=="nsubj":
                place1=q[1]-1
                place2=q[2]-1
                s2_subgect_dempndsy.append((sentance2_split[place1], sentance2_split[place2]))



        #print("sentance 1 ")
        #for q in s1_subgect_dempndsy:
        #    print(q)

        #print("sentace 2")
        #for q in s2_subgect_dempndsy:
        #    print(q)


        s1_action_on_object=[]
        s2_action_on_object=[]
        theshold2=0.8
        for q in s1_subgect_dempndsy:
            for w in s2_subgect_dempndsy:
                object1 = w[0]
                object2 = q[0]
                try:
                    sim = word_vectors.similarity(object1, object2)
                except(KeyError):
                    print("errorr in word to vec ")
                    print("word was ",object1," or ",object2)
                    if object1==object2:
                        sim=1
                    else:
                        sim=0
                if sim>theshold2:
                    print("s1 and s2 are talk about the same thing")
                    s1_action_on_object.append(q[0])
                    s2_action_on_object.append(w[0])

        print("action on object ",s1_action_on_object,s2_action_on_object)
        try:
            object1=s1_action_on_object[0]
            object2=s2_action_on_object[0]
            sim = word_vectors.similarity(object1,object2)
        except:
            #print("compare error")
            sim=1
        theshold=0.8
        #print("object simality =",sim)
        gess=""


        try :
            simlarity_of_sentances= word_vectors.wmdistance(sentance1_split, sentance2_split)
            print(simlarity_of_sentances)
        except:
            print("snetce compare error")
            simlarity_of_sentances=1000

        if sim>theshold and not len(s1_action_on_object)==0 and simlarity_of_sentances>senthace_simaly_thershold:
            gess="ENTAILMENT"
            result=teasts.guss("ENTAILMENT")
          #  print("geuss ENTAILMENT")

        elif  len(s1_action_on_object)==0:
            gess = "NEUTRAL"
            result =teasts.guss("NEUTRAL")
           # print("gessing NEUTRAL ")

        else:
            gess = "CONTRADICTION"
            result =teasts.guss("CONTRADICTION")
            #print("gessing CONTRADICTION")



        #print("anser was ",teasts.anser)
        if result=="no":
            sentece_we_got_wong.append((sentence1,sentence2,teasts.anser ,gess))
    print("got right",teasts.got_right)
    print("got wong",teasts.got_wrong)
    print("% accucery ",teasts.got_right/(teasts.got_right+teasts.got_wrong))


nlp.close()  # Do not forget to close! The backend server will consume a lot memery.

print("##########################")
'''
for q in sentece_we_got_wong:
    print("sentace1 ",q[0])
    print("sentace2 ",q[1])
    print("asnser was ",q[2])
    print("gessed ",q[3])
    print(q[2],q[3])
    print("")
    print("")
'''