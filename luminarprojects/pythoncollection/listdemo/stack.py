size=int(input("enter the size:"))
stk=[]
top=0
def push(element):
    global top
    if(top>=(size)):
        print("stack full")
    else:
        stk.append(element)
        top+=1
def pop():
    global top
    if(top<=0):
        print("stack empty")
    else:
        top-=1
        print(stk[top],"popped out")
def display():
    for i in range(0,top):
        print(stk[i])
n=1
while(n!=0):
    options=int(input("enter the operation 1)push 2)pop 3)display:"))
    if(options==1):
        element=int(input("enter the element to push:"))
        push(element)
    elif(options==2):
        pop()
    elif(options==3):
        display()
    n=int(input("do u want to continue:press 0 for exit,1 for continue:"))