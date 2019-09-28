"""
@author: brianperez
"""
# =============================================================================
# def read_file(): 
#     file = open("vivendi.txt", 'r') 
#     file2 = open("activision.txt", 'r') 
#     
#     ID_list = Linked_list()
#     
#     for elements_a in file.read().split('\n'):
#         self.next = elements_a 
# #        print(self)
# #    for elements_b in file2.read().split('\n'):
# #        print (elements_b)        
# =============================================================================
  




class Node(object):
    item = -1
    next = None
   
    def __init__(self, item, next):
       self.item = item
       self.next = next
   
    def get_next(self):
       return self.next
   
    def set_next(self, item):
       self.next = item
   
    def get_data(self):
       return self.item
   
    def set_data(self, item):
       self.item = item
        
class Linked_list (object):
    def __init___(self, r = None): 
            self.item = r 
            self.size = 0 
    
    def get_size (self): 
        return self.size



def addLast(self, item): 
	new_node = Node (item, None)
    
    if self.head is None: 
		self.head = new_node
		self.size += 1
        return 
    
	last_node = self.head
	while last_node.next: 
		last_node = last_node.next
	
    last_node.next = new_node
    self.size+= 1 
    return 

    def remove (self, item):
        this_node = Node (item, self.head)
        prev_node = None 
        while this_node:
            if this_node.get_data() == item:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node
                self.size -= 1
                return True
            else: 
                prev_node = this_node 
                this_node = this_node.get_next()
        return False 
    def find (self, item): 
        this_node = self.head
        while this_node:
            if this_node.get_data() == item:
                return item
            else: 
                this_node = this_node.get_next()
        return None
    
    def display (self):
        elements = []
        curr_node = self.head 
        while curr_node.next != None :
            curr_node = curr_node.next 
            elements.append(curr_node.get_data)
        print (elements)

file = open("vivendi.txt", 'r') 
file2 = open("activision.txt", 'r') 
    
ID_list = Linked_list()



for elements in file:
    #print(elements)
    ID_list.add_to_last(elements)
    print("already in the ll" , ID_list.head)

#print(ID_list.head.get_data)


#ID_list.display()
#print(ID_list.find("4964"))


# =============================================================================
# 
# def compare :
#     
# def bubble_sort:
#     
# def merge_recursion:
#     
# =============================================================================

