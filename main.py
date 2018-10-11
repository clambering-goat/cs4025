


import open_traning_data
import teasting


data=open_traning_data.open_data()


print(data[1])


temp=teasting.teast()

x=temp.get()

for q in x:
    print(q)


y=temp.guss("ENTAILMENT")

print(y)
