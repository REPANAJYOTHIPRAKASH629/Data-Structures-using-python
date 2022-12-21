class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self,data=None,):
        self.head = None
        self.tail = None
        self.size = 0
    def print(self):
        if self.head is None:
            print("Doubly linked list is empty.")
            return
        itr = self.head
        dllstr = ''
        while itr:
            dllstr = dllstr + str(itr.data)+'<===>'
            itr = itr.next
        print(dllstr)
    def is_empty(self):
        return self.size == 0
    def insert_at_beginning(self,new_node):
        new_node = Node(new_node)
        if self.is_empty():
            self.head = self.tail = new_node
            self.size+=1
            return
        new_node.next = self.head
        new_node.prev = None
        self.head = new_node
        self.head.next.prev = new_node
        self.size += 1
    def insert_at_end(self,new_node):
        new_node = Node(new_node)
        if self.is_empty():
            self.head = self.tail = new_node
            self.size+=1
            return
        new_node.next = None
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    def insert_at_position(self, at, new_elem):
        if at < 0 or at > self.size:
            raise Exception('Overflow: The given "at" postion is invalid')

        if at == 0:
            self.insert_at_beginning(new_elem)
            return
        if at == self.size:
            self.insert_at_end(new_elem)
            return

        index = 1
        new_node = Node(new_elem)
        curr_node = self.head
        next_node = self.head.next
        while index < at:
            curr_node = curr_node.next
            next_node = next_node.next
            index += 1

        new_node.next = next_node
        new_node.prev = curr_node
        curr_node.next = new_node
        next_node.prev = new_node
        self.size += 1
    def remove_first(self):
        if self.is_empty():
            raise Exception("Nothing to remove")
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp.data
    def remove_last(self):
        if self.is_empty():
            raise Exception("Nothing to remove")

        temp = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size -= 1

        if self.is_empty():
            self.head = None
        return temp.data
    def remove_at_position(self, position):
         if(position < 1):
            print("\nposition should be >= 1.")
         elif (position == 1 and self.head != None):
             nodeToDelete = self.head
             self.head = self.head.next
             nodeToDelete = None
             if (self.head != None):
                          
                 self.head.prev = None
         else:
             temp = self.head
             for i in range(1, position-1):
                 if(temp != None):
                     temp = temp.next                        
             if(temp != None and temp.next != None):
                 nodeToDelete = temp.next
                 temp.next = temp.next.next
                 if(temp.next.next != None):
                     temp.next.next.prev = temp.next  
                     nodeToDelete = None 
             else:
                 print("\nThe node is already null.")
    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
 
if __name__=="__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning('akash')
    dll.insert_at_beginning('prakash')
    dll.insert_at_beginning('bubu')
    dll.print()
    dll.insert_at_end('mukesh')
    dll.print()
    dll.insert_at_position(3,'12345')
    dll.print()
    a = dll.get_length()
    print(a)
    dll.remove_at_position(3)
    dll.print()
    dll.remove_first()
    dll.print()
    dll.remove_last()
    dll.print()
    
    
