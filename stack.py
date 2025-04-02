class DLL:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class stack:
    def __init__(self):
        self.head=None
        self.mid=None
        self.size=0
    def push(self,x):
        new=DLL(x)
        new.next=self.head
        if self.head:
            self.head.prev=new
        self.head=new
        self.size+=1
        if self.size==1:
            self.mid=new
        else:
            if self.size%2!=0:
                self.mid=self.mid.prev
    def pop(self):
        if not self.head:
            return None
        popped=self.head.val
        self.head=self.head.next
        if self.head:
            self.head.prev=None
        self.size-=1
        if self.size%2==0:
            self.mid=self.mid.next if self.mid else None
        return popped
    def find_middle(self):
        if not self.mid:
            return None
        return self.mid.val
    def delete_node(self):
        if not self.mid:
            return None
        mid=self.mid.val
        if self.mid.prev:
            self.mid.prev.next=self.mid.next
        if self.mid.next:
            self.mid.next.prev=self.mid.prev
        if self.size%2==1:
            self.mid=self.mid.next
        else:
            self.mid=self.mid.prev
        self.size-=1
        return mid
stack = stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.find_middle())  # Output: 2
stack.delete_node()
print(stack.find_middle())  # Output: 3

print(stack.pop())  # Output: 4
print(stack.pop())  # Output: 3
