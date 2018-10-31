



import random

class teast():
    def __init__(self):
        train_data="./sick_teast/SICK_test_annotated.txt"
        file=open(train_data,"r")
        file=file.read()
        self.data=file.split("\n")
        self.count=0
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

    def full_teast(self):
        self.count=self.count+1
        pick=self.count
        data_picked=self.data[pick]
        #print("random pick \n",data_picked)
        data_picked=data_picked.split("	")
        data_out=data_picked[1],data_picked[2]
        self.anser=data_picked[4]
        return(data_out)

    def guss(self,there_guss):
        #make sure self.anser is defind flag error if not
        try:
            self.anser
        except:
            print("need to get data using teast.get() befor teast.guss()")
            print("now closing python ")
            exit()
        if there_guss==self.anser:
            self.got_right+=1
            return("yes")
        else:
            self.got_wrong+=1
            return("no")

def exsample():

    teaxt='''
    temp=teast()

    x=temp.get()

    for q in x:
        print(q)


    y=temp.guss("ENTAILMENT")

    print(y)
    
    temp=teast()
for q in range(10):
    x=temp.full_teast()

    for q in x:
      print(q)


    y=temp.guss("ENTAILMENT")

    print(y)
    '''
    print(teaxt)


