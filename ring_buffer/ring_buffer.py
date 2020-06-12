from doubly_linked_list import DoublyLinkedList

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    #current keeps track of oldest value
    #can add 1, and reset to 0 when hits capacity
    self.current = 0
    #sets up an initial list of Nones x capacity
    self.storage = [None]*capacity

  def append(self, item):
    #if capacity not full, add to list
    if len(self.storage) < self.capacity:
      self.storage.append(item)
    if len(self.storage) == self.capacity:
      #if head is last one
      self.storage[self.current] = item
      if self.current < self.capacity - 1:
        self.current +=1 
      else:
        self.current = 0 


  def get(self):
    myList = []
 #  None <- prev (Head node) next -> <-prev (node) next -> <- prev (Tail node) next -> None 
    for x in self.storage:
      if x != None:
        myList.append(x)
    return myList