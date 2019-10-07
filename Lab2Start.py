"""
Created on Mon Sep  20 12:40:04 2019
Course: CS 2302 - Data Structures
Author: Brian Perez
Assignment: Lab 2 
Instructor: Diego Aguirre 
D.O.L.M.: 10/7/19 (to write this)
"""
def create_list(LL): 
    file = open("vivendi.txt", 'r') 
    file2 = open("activision.txt", 'r') 

    for x in file.read().split('\n'):
        LL.add_last(x) 
    for x in file2.read().split ('\n'):
        LL.add_last(x)
        
        
#    for elements_b in file2.read().split('\n'):
#        print (elements_b)        
class Node:
    item = -1
    next = None
   
    def __init__(self, item, next):
       self.item = item
       self.next = next
        
class Linked_list:
    
    def __init__(self, head=None):
        self.head = head
        
    def add_last(self, item):

        if self.head is None:  # If the list is empty, add a new head
            self.head = Node(item, self.head)
            return

        current = self.head
        while current.next is not None:  # Looking for the second to last node
            current = current.next

        current.next = Node(item, None )

    def add(self, index, item):
        if index == 0:
            self.head = Node(item, self.head)
            return

        if index < 0:  # Don't do anything if index is invalid
            return

        current = self.head
        for i in range(index - 1):  # Looking for the node at position index - 1
            if current is None:
                return

            current = current.next

        if current is not None:
            current.next = Node(item, current.next)
    
    def index_of(self, item):
        current = self.head
        i = 0
        while current:
            if int(current.item) == int(item):
                return i
            i += 1
            current = current.next
        return -1
    
    def print_list(self):
        current = self.head
        
        while current is not None:
            print(current.item)
            current = current.next
            
    def size(self):
        current = self.head
        
        length = 0
        while current is not None:
            length += 1
            current = current.next

        return length
    
    def biggest(self):
        current = self.head
        biggest = 0
        while current:
            if biggest < int(current.item):
                biggest = int(current.item)
            current = current.next
        return biggest
                
    def remove(self, index):
        if index < 0:  # Don't do anything if index is invalid
            return

        if index == 0:  # Handling special case - when the item to remove is the head
            self.remove_first()
            return

        current = self.head

        for i in range(index - 1):  # Looking for the second to last node
            if current is None:
                return

            current = current.next

        if current is not None and current.next is not None:
            current.next = current.next.next
            
    def bubble_sort (self):
        swap_counts  = 0 
        start = self.head
        p = self.head
        q = p.next
        while p.next :
            if q is None :
                if swap_counts == 0 :
                    print("stopped")
                    return 
            swap_counts = 0
            if int(p.item) > int(q.item) :
                temp = q.item
                q.item = p.item
                p.item = temp
                swap_counts += 1 
            if swap_counts != 0: 
                p = start
                q = p.next
            else : 
                p = q
                q = p.next
                
    def next_same_delete(self):
        current = self.head 
        if current.next is None :
            return 
        while current.next: 
            if current.item == current.next.item:
                current.next = current.next.next
            current = current.next
            
    def solution1(self):
        current = second = self.head
        while current is not None:
            while second.next is not None:   # check second.next here rather than second
                if second.next.item == current.item:   # check second.next.data, not second.data
                    second.next = second.next.next   # cut second.next out of the list
                else:
                    second = second.next   # put this line in an else, to avoid skipping items
            current = second = current.next

    def solution2 (self): 
        self.bubble_sort()
        self.next_same_delete()
            
    def solution3(self):
        self.head = merge_sort(self.head)
        #self.print_list()
        #print("\n")
        self.next_same_delete()
        
    def solution4(self):
        seen = [False] * (self.biggest()+1)
        current = self.head
        while current:
            if seen[int(current.item)] == True:
                self.remove(self.index_of(int(current.item)))
            else:     
                seen[int(current.item)] = True
            current = current.next
        return 
          
def merge_sort(head):
    if head is None or head.next is None:
        return head
    l1, l2 = divide_lists(head)
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    head = merge_lists(l1, l2)
    return head

def merge_lists(l1, l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if int(l1.item) <= int(l2.item):
        temp = l1
        temp.next = merge_lists(l1.next, l2)
    else:
        temp = l2
        temp.next = merge_lists(l1, l2.next)
    return temp
        
def divide_lists(head):
    slow = head                     # slow is a pointer to reach the mid of linked list
    fast = head                     # fast is a pointer to reach the end of the linked list
    if fast:
        fast = fast.next            
    while fast:
        fast = fast.next            # fast is incremented twice while slow is incremented once per loop
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid
            

        
    
def main () :
    LL = Linked_list()
    create_list(LL) 
    LL.print_list()
    print("\n")
    
    #LL.solution1()
    #LL.solution2()
    #LL.solution3()
    #LL.solution4()
    
    #LL.print_list()

main ()

