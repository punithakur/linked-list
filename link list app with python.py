class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linklist:
    def __init__(self):
        self.start=None

    def insert(self,data):
        newnode=node(data)
        if(self.start):
            current=self.start
            while(current.next):
                current=current.next
            current.next=newnode
        else:
            self.start=newnode
    
    def printing(self):
        
        if(self.start):
            print(self.start.data)
            current=self.start
            while(current.next):
                current=current.next
                print(current.data)
                

    def finding(self,vl):
        if(self.start):
            p=1
            current=self.start
            if current.data==vl:
                print("data is found and its index position is -: ",p)
            elif(current.next):
                current=current.next
                p+=1
                if current.data==vl:
                    print("data is found and its index position is -: ",p)
                
            else:
                print("data not found")
        else:
            print("empty linklist")

    def deletion(self,nm):
        current=self.start
        index=1
        if index==nm:
            self.start=current.next
        else:
            while(current.next):
                temp=current
                current=current.next
                if current.data==nm:
                    temp.next=current.next
                    




ll= linklist()
while True:
    print("choose any one option in following")
    print("1. inter value in new node")
    print("2. printing all value of nodes")
    print("3. find node index of any value")
    print("4. node deletion")
    n=int(input())
    if n==1:
        ll.insert(int(input("enter the value")))
    elif n==2:
        ll.printing()
    elif n==3:
        ll.finding(int(input("enter the value for find")))
    elif n==4:
        ll.printing()
        ll.deletion(int(input("enter the value for deletion")))

            
