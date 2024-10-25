class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_at_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=newnode
    def insert_after(self,prev_data,data):
        newnode=Node(data)
        temp=self.head
        while temp is not None:
            if temp.data==prev_data:
                break
            temp=temp.next
        if temp is None:
            return
        newnode.next=temp.next
        temp.next=newnode
    def delete_head(self):
        if self.head is None:
            return
        self.head=self.head.next
    def delete_tail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head 
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def delete_node(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return
        prev=None
        while temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if temp is None:
            return
        prev.next=temp.next
        temp=None
    def print_list(self):
        temp=self.head
        if temp is None:
            print("The list is empty")
        else:
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
            print()

if __name__ == "__main__":
    obj=SinglyLinkedList()
    import sys
    input=sys.stdin.read
    data=input().strip().split('\n')
    num=int(data[0])
    for i in range(1,num+1):
        operation=list(map(int,data[i].split()))
        if operation[0]==1:
            obj.insert_at_beginning(operation[1])
        elif operation[0]==2:
            obj.insert_at_end(operation[1])
        elif operation[0]==3:
            obj.insert_after(operation[2],operation[1])
        elif operation[0]==5:
            obj.delete_tail()
        elif operation[0]==6:
            obj.delete_node(operation[1])
        elif operation[0]==4:
            obj.print_list()                                                        
