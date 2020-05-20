class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,item):
        if self.top is None:
            self.top=Node(item)
        else:
            push_item=Node(item)
            push_item.next=self.top
            self.top=push_item
    def pop(self):
        if self.top is None:
            return None
        else:
            poped_item=self.top.item
            self.top=self.top.next
            return poped_item
    def disp(self):
        print('\n','.'*12)
        a=self.top
        while self.top!=None:
            print(self.top.item)
            self.top=self.top.next
        print('\n','*'*12)
        self.top=a
obj=Stack()
try:
    while True:
        print('Menu')
        print('1. Push')
        print('2. Pop')
        print('3. Display')
        print('4. Exit')
        inp=int(input())
        if inp==1:
            print('Enter Item: ')
            obj.push(int(input()))
        elif inp==2:
            item=obj.pop()
            print('Poped item is',item)
        elif inp==3:
            obj.disp()
        elif inp==4:
            break
        else:
            print('Wrong Choice')
except:
    pass
            
            