class ListNode:
    def __init__(self, value, index = None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        self.index = index
    

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value, index=None):
        current_next = self.next
        self.next = ListNode(value, index, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(value)
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(value, self.length - 1)
        else:
            self.tail.insert_after(value, self.length - 1)
            self.tail = self.tail.next

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        #If list empty
        if self.head and not self.tail:
            print("ERROR: Attempted to delete node not in list")
            return
        #If node is head or tail or both
        elif node == self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        #If node is in middle
        else:
            node.delete()

        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.length == 0:
            print("ERROR: No values in list.")
            return

        highestValue = self.head.value
        node = self.head.next
        while True:
            if node is not None:
                if node.value > highestValue:
                    highestValue = node.value
                node = node.next
            else:
                break
        
        return highestValue

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.abcs = DoublyLinkedList()
        self.abcs.add_to_tail("a")
        self.abcs.add_to_tail("b")
        self.abcs.add_to_tail("c")
        self.abcs.add_to_tail("d")
        self.abcs.add_to_tail("e")
        self.abcs.add_to_tail("f")
        self.abcs.add_to_tail("g")
        self.abcs.add_to_tail("h")
        self.abcs.add_to_tail("i")
        self.abcs.add_to_tail("j")
        self.abcs.add_to_tail("k")
        self.abcs.add_to_tail("l")
        self.abcs.add_to_tail("m")
        self.abcs.add_to_tail("n")
        self.abcs.add_to_tail("o")
        self.abcs.add_to_tail("p")
        self.abcs.add_to_tail("q")
        self.abcs.add_to_tail("r")
        self.abcs.add_to_tail("s")
        self.abcs.add_to_tail("t")
        self.abcs.add_to_tail("u")
        self.abcs.add_to_tail("v")
        self.abcs.add_to_tail("w")
        self.abcs.add_to_tail("x")
        self.abcs.add_to_tail("y")
        self.abcs.add_to_tail("z")


    def isGreater(self, v1, v2):
        firstLetter1 = v1[0]
        firstLetter2 = v2[0]

        fl1Value = -1
        fl2Value = -1
        node = self.abcs.head
        while node:
            if firstLetter1 == node.value:
                fl1Value = node.index
            if firstLetter2 == node.value:
                fl2Value = node.index
            node = node.next
            if fl2Value != -1 and fl1Value != -1:
                break

        if fl1Value == fl2Value:
            return self.isGreater(v1[1:], v2[1:])
        
        if fl1Value > fl2Value:
            return True
        if firstLetter1 < firstLetter2:
            return False
        

    # Insert the given value into the tree
    def insert(self, value):
        if self.isGreater(self.value, value):
            if self.left == None:
                self.left = BinarySearchTree(value)
                return
            self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
                return
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left != None:
                return self.left.contains(target)
        elif self.value <= target:
            if self.right != None:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left != None:
            self.left.for_each(cb)

        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        leftSidePrinted = False
        if node.left != None:
            leftSidePrinted = node.left.in_order_print(node.left)
        else:
            print(node.value)
            if node.right != None:
                node.right.in_order_print(node.right)
            return True
        
        if leftSidePrinted:
            print(node.value)
            if node.right != None:
                node.right.in_order_print(node.right)
            return True

import time
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

names_1_tree = BinarySearchTree(names_1[0])
for i in range(1, len(names_1)):
    names_1_tree.insert(names_1[i])

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
# RUNTIME OF THE STARTER CODE IS O(N^2) OR MORE ACCURATELY:
# IF NAMES_1 IS N AND NAMES_2 IS T THE RUNTIME IS O(N * T)
# IF THE READING FROM THE FILES IS COUNTED IN THE BIG O THEN
# O((N*T) + N + T)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
