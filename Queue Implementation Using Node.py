class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.end=None
        
    def insert(self,data):
        if self.end==None:
            self.front=Node(data)
            self.end=self.front
        else:
            self.end.next=Node(data)
            self.end=self.end.next
    def delete(self):
        if self.front is None:
            return None
        else:
            deleted_data=self.front.data
            self.front=self.front.next
            return deleted_data
    def display(self):
        if self.front is None:
            print('Empty is Queue')
        else:
            a=self.front
            while self.front!=None:
                print(self.front.data,end=' ')
                self.front=self.front.next
            self.front=a
obj=Queue()
try:
    while True:
        print('\n \nMenu ')
        print('Queue implementation using Node ')
        print('1. Enter data ')
        print('2. Delete data ')
        print('3. Display')
        print('4. Quit')
        ch=int(input())
        if ch==1:
            item=int(input('Enter Data :'))
            obj.insert(item)
        elif ch==2:
            print('The deleted data is',obj.delete())
        elif ch==3:
            obj.display()
        elif ch==4:
            break
        else:
            print('Wrong Choice')
except:
    print('Error accepted!!!! \n BYE')
            
            