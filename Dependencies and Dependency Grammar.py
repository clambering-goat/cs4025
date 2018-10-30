 # Simple usage
from stanfordcorenlp import StanfordCoreNLP
import teasting


teasts=teasting.teast()

import open_traning_data
data=open_traning_data.open_data()


nlp = StanfordCoreNLP(r'./stanford-corenlp-full-2018-10-05')




for test_time in range(10):

    data=teasts.get()


    sentence1=(data[0])
    sentence2=(data[1])


    #sentence1="A man in a black jacket is doing tricks on a motorbike"

    #sentence2="A person is riding the bicycle on one wheel"

    sentance1_split=sentence1.split(" ")
    sentance2_split=sentence2.split(" ")


    print("sentance 1",sentence1)
    print("sentance 2",sentence2)
    print(" ")

    s1_dependonsy=nlp.dependency_parse(sentence1)
    s2_dependonsy=nlp.dependency_parse(sentence2)

    #print ('Dependency Parsing:', s1_dependonsy)


    #print("#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{#{}}}}}}}}}}}}}}}}}}}}}}}}}}}\n")


    #print("Dependency Parsing 2 ",s2_dependonsy,"\n")



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



    print("sentance 1 ")
    for q in s1_subgect_dempndsy:
        print(q)

    print("sentace 2")
    for q in s2_subgect_dempndsy:
        print(q)


    s1_action_on_object=[]
    s2_action_on_object=[]

    for q in s1_subgect_dempndsy:
        for w in s2_subgect_dempndsy:
            if q[1]==w[1]:
                print("s1 and s2 are talk about the same thing")
                s1_action_on_object.append(q[0])
                s2_action_on_object.append(w[0])

    print("action on object ",s1_action_on_object,s2_action_on_object)

    if (s1_action_on_object)==s2_action_on_object:
        teasts.guss("ENTAILMENT")
        print("geuss ENTAILMENT")
    elif  len(s1_action_on_object)==0:
        teasts.guss("NEUTRAL")
    else:
        teasts.guss("CONTRADICTION")
        print("gessing CONTRADICTION")

    print("anser was ",teasts.anser)

print("got right",teasts.got_right)
print("got wong",teasts.got_wrong)
nlp.close()  # Do not forget to close! The backend server will consume a lot memery.