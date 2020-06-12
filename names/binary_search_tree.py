"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #self.value is root node
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                #run insert() again, will compare to value its 
                #on and then go right or left
                self.left.insert(value)
        else:
            #no right value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        if target > self.value:
            if not self.right:
                return False 
            else:
                return self.right.contains(target)

        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)    

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        # if don't put return, will auto put a return after
        # which will return nothing
        return self.right.get_max()
    
    #traverse like a linklist
    def interative_get_max(self):
        current_max = self.value
        current = self
        #traverse 
        while current is not None:
            if current.value > current_max:
                  #update our current_max
                current_max = current.value
            #continue to traverse
            current = current.right
          
    

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        #will first go through all values on right
        if self.right:
            self.right.for_each(fn)
        #when finished with last value, will go to previous value
        #and start searching left
        if self.left:
            self.left.for_each(fn)


    def interative_for_each(self, fn):
        stack = []

        #add the root to stack
        stack.append(self)

        #loop if stack is not empty
        while len(stack) > 0:
            #will remove from back of stack
            removed = stack.pop()
            if removed.right:
                stack.append(removed.right)
        
            if removed.left:
                stack.append(removed.left)

                fn(removed.value)
    
    #use in a que
    from collections import deque

    def breadth_for_each(self, fn):
        #queue = deque()
        queue =[]

        #add the root to stack
        queue.append(self)

        #loop if stack is not empty
        while len(queue) > 0:
            #will remove from front of que
            #removes in row going down the tree
            removed = queue.pop(0)
            if removed.right:
                queue.append(removed.right)
        
            if removed.left:
                queue.append(removed.left)

            fn(removed.value)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # que, while loop
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
