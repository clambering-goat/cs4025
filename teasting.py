



import random

class teast():
    def __init__(self):
        train_data="./sick_teast/SICK_test_annotated.txt"
        file=open(train_data,"r")
        file=file.read()
        self.data=file.split("\n")

        self.got_right=0
        self.got_wrong=0

    def get(self):
        #[0] heater name not needed
        #print(len(data))
        pick=random.randint(1,4297)
        data_picked=self.data[pick]
        #print("random pick \n",data_picked)
        data_picked=data_picked.split("	")
        data_out=data_picked[1],data_picked[2]
        self.anser=data_picked[4]
        return(data_out)

    def guss(self,there_guss):
        if there_guss==self.anser:
            self.got_right+=1
            return("yes")
        else:
            self.got_wrong+=1
            return("no")

temp=teast()

x=temp.get()
for q in x:
    print(q)


y=temp.guss("ENTAILMENT")

print(y)