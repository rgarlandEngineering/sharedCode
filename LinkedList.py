class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        #self.visited = [value]
        self.queue = [str(value) + "->"]

    def print_list(self):
        temp = self.head
        while temp != None:
            #self.queue.append(temp.value)
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.queue.append(str(value) + "->")
            #print(self.queue)
        self.length += 1
    
    def pop(self): #<-- First remove
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def remove(self, arr): #<-- Optimized remove
        arr.pop()
        self.length -= 1

        
    
linked_list = LinkedList(5)
linked_list.append(8)
linked_list.append(12)
linked_list.append(15)

linked_list.remove(linked_list.queue)
linked_list.remove(linked_list.queue)
print(linked_list.queue)

#linked_list.print_list()
print("Length of this List is: " + str(linked_list.length) + " Nodes ")
