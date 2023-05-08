def grocery_list():
    name=input("Enter name : ")
    age=input("Enter age : ");items=[]
    print(f"{name} enter the items you wish to add after the prompt")
    details=[name,age,items]
    print("Enter quit to quit the program")
    while(True):
        i=input("> ")
        if(i=="quit"):
            break
        items.append(i)
    print(details)
grocery_list()