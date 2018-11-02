#train_data="./sick_teast/SICK_test_annotated.txt"
train_data="./sick_train/SICK_train.txt"
file=open(train_data,"r")
file=file.read()




data=file.split("\n")

total_n=0
total_e=0
total_c=0

c1=0
c2=0
c3=0

vaule_of_nutral=[]
vaule_of_entment=[]
vaule_of_corndiction=[]

y_vaules1=[]
y_vaules2=[]
y_vaules3=[]
import matplotlib.pyplot as plt








for q in data[1:-1]:

    feilds=q.split("	")


    simler=float(feilds[3])
    result=feilds[4]

    #print(simler,result)

    if result=="NEUTRAL":
        vaule_of_nutral.append(simler)
        y_vaules1.append(2)
        total_n=total_n+simler
        c1=c1+1

    if result=="ENTAILMENT":
        vaule_of_entment.append(simler)
        y_vaules2.append(3)
        total_e=total_e+simler
        c2=c2+1


    if result=="CONTRADICTION":
        vaule_of_corndiction.append(simler)
        y_vaules3.append(4)
        total_c=total_c+simler
        c3=c3+1


print("NEUTRAL",(total_c/c1))

print("ENTAILMENT",(total_e/c2))

print("CONTRADICTION",(total_c/c3))

plt.plot(vaule_of_nutral,y_vaules1,'ro')
plt.plot(vaule_of_entment,y_vaules2,'ro')
plt.plot(vaule_of_corndiction,y_vaules3,'ro')



plt.axis([0, 6, 1, 5])
plt.show()
