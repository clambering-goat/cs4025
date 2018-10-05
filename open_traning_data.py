






def  open_data():

    train_data="./sick_train/SICK_train.txt"

    file=open(train_data,"r")

    file=file.read()

    data=file.split("\n")

    #[0] heater name not needed
    #print(data[1])

    print("last entey",data[-1])

    train_data={}
    for q in data[1:-1]:
        temp=q.split("	")
        #print(temp[0])
        key=int(temp[0])
        data=temp[1:]
        train_data[key]=data
    return(train_data)
    #print((train_data[10000]))
    #print("done")
