class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def isGreater(self, v1, v2):
        firstLetter1 = v1[0]
        firstLetter2 = v2[0]

        if firstLetter1 == firstLetter2:
            return self.isGreater(v1[1:], v2[1:])
        
        

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value:
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