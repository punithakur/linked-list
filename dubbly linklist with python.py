class node:
    def __init__(self,data=None,next=None,pre=None):
        self.data=data
        self.next=next
        self.pre=pre

class dubblyLL:
    def __init__(self):
        self.start=None

    def insert(self, data):
        newnode=node(data)
        if(self.start):
            current=self.start
            while(current.next):
                current=current.next
            current.next=newnode
            newnode.pre=current
        else:
            self.start=newnode

    def printing(self):
        if(self.start):
            current=self.start
            print(current.data)
            while(current.next):
                current=current.next
                print(current.data)
        else:
            print("empty list")
ll=dubblyLL()

while True:
    print("1. create link list")
    print("2. print link list")
    n=int(input("inter your choise"))
    if n==1:
        ll.insert(int(input("enter the value")))
    elif n==2:
        ll.printing()
        
          



          
            
            
