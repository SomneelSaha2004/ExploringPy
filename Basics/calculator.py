print("Welcome to the Python Calculator!")
op=['+','-','*','/','^','p','q']
print(f"Supported Operations :\nadd --> {op[0]}\nsubstract --> {op[1]}\nmultiply --> {op[2]}\ndivide --> {op[3]}\npower --> {op[4]}")
val=22/7
print(f"{val:3.4f}")
print("to print history --> p\nto quit --> q")
while(True):
    r=0
    o=input("Enter operation : ")
    if o=='p':
        f=open("history.txt")
        print(f.read())
        f.close()
    if(o=="q"):
        print("Thanks for using this product!")
        break
    a=float(input("Enter number 1  : "))
    b=float(input("Enter number 2 : "))
    match o:
        case '+' :
            r=a+b
        case '-':
            r=a-b
        case '*':
            r=a*b
        case '/':
            r=a/b
        case '^':
            r=a**b
        case _:
            print("Operation not supported")
            continue
    with open("history.txt",mode="a+") as f:
        s=f"{a} {o} {b} = {r}\n"
        print(s)
        f.write(s)

    