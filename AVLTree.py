# Data Structures - Assignment 2
# Christina Chan
# Monday, Feb 17th, 2014
from random import randrange

# vertex class, has left child and right child as well as a value
class AVL_Vertex(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class AVL_Tree(object):
    def __init__(self, root = None):
        self.vertex = None
        self.height = -1
        self.balance = 0
        self.root = root
        self.balCount = 0

    # gets height of given vertex
    def height(self):
        if self.vertex:
            return self.vertex.height
        else:
            return 0

    # insert function (calls rebalance to fix the tree)
    def insert(self, value):
        tree = self.vertex

        newVertex = AVL_Vertex(value)
        
        if tree == None:
            self.vertex = newVertex
            self.vertex.left = AVL_Tree()
            self.vertex.right = AVL_Tree()
            # inserts value if the tree is empty
        else:
            if tree.value > value:
                self.vertex.left.insert(value)
            else:
                self.vertex.right.insert(value)

        self.rebalance()

    # makes the tree all pretty again
    def rebalance(self):
        self.balCount = self.balCount + 1
        # already inserted the key, check for balance
        # runs update functions non-recursively
        self.updateHeights(False) 
        self.updateBalances(False)
        
        # while we are not balanced
        while self.balance < -1 or self.balance > 1:
            # if we are unbalanced on the left side
            if self.balance > 1:
                if self.vertex.left.balance < 0:
                    self.vertex.left.lRotate()
                    self.updateHeights()
                    self.updateBalances()
                self.rRotate()
                self.updateHeights()
                self.updateBalances()

            # if we are unbalanced on the right side
            if self.balance < -1:
                if self.vertex.right.balance > 0:
                    self.vertex.right.rRotate()
                    self.updateHeights()
                    self.updateBalances()
                self.lRotate()
                self.updateHeights()
                self.updateBalances()
    
    def rRotate(self):
        # rotates whole AVL tree right
        X = self.vertex
        Y = self.vertex.left.vertex
        Z = Y.right.vertex

        self.vertex = Y
        Y.right.vertex = X
        X.left.vertex = Z

    def lRotate(self):
        # rotates whole AVL tree left
        X = self.vertex
        Y = self.vertex.right.vertex
        Z = Y.left.vertex

        self.vertex = Y
        Y.left.vertex = X
        X.right.vertex = Z

    # fixes the heights of all verticies after we've changed the tree
    def updateHeights(self, recurse = True):
        if not self.vertex == None:
            if recurse:
                if self.vertex.left != None:
                    self.vertex.left.updateHeights()
                if self.vertex.right != None:
                    self.vertex.right.updateHeights()

            self.height = 1 + max(self.vertex.left.height,
                                  self.vertex.right.height)
        else:
            self.height = -1

    # fixes the balance value of verticies after we've changed the tree
    def updateBalances(self, recurse = True):
        if not self.vertex == None:
            if recurse:
                if self.vertex.left != None:
                    self.vertex.left.updateBalances()
                if self.vertex.right != None:
                    self.vertex.right.updateBalances()

            self.balance = self.vertex.left.height - self.vertex.right.height
        else:
            self.balance = 0

    def delete(self, value):
        if self.vertex != None:
                # if we found the value to be deleted
                if self.vertex.value == value:
                        # if we are a leaf, just delete the vertex
                        if self.vertex.left.vertex == None and self.vertex.right.vertex == None:
                                self.vertex = None
                        # if left child is empty
                        elif self.vertex.left.vertex == None:
                                # shift vertex up a level
                                self.vertex = self.vertex.right.vertex
                        # if right child is empty
                        elif self.vertex.right.vertex == None:
                                # shift vertex up a level
                                self.vertex = self.vertex.left.vertex
                        else:
                                replacement = self.smallest(self.vertex)
                                if replacement != None: # just checking
                                        self.vertex.value = replacement.value
                                        # we replaced the value, now delete it
                                        self.vertex.right.delete(replacement.value)
                        self.rebalance()
                        return
                # if value is less than value at this vertex
                elif value < self.vertex.value:
                        self.vertex.left.delete(value)
                # if value is greater than value at this vertex
                elif value > self.vertex.value:
                        self.vertex.right.delete(value)
                self.rebalance()
        else:
                return

    def smallest(self, vertex):
        # find the smallest value vertex in the right child
        vertex = vertex.right.vertex
        if vertex != None:
                while vertex.left != None:
                        if vertex.left.vertex == None:
                                return vertex
                        else:
                                vertex = vertex.left.vertex
        return vertex
                                
    
    # prints the tree
    def display(self, level=0, pref=''):
            # '-' indicates the level/subtree that we are at
            # absence of '-' means we are at the root
            if self.vertex != None:
                    print '-' * level * 2, pref, self.vertex.value
                    if self.vertex.left != None:
                            self.vertex.left.display(level + 1, 'l<')
                            # indicates we are a left child
                    if self.vertex.right != None:
                            self.vertex.right.display(level + 1, 'r>')
                            # indicates we are a right child

    def printCount(self):
            print "count: ", self.balCount

# done AVL_Tree class

# main function to test!
values = ["Copperfield",
        "Houdini",
        "Cardini",
        "Blackstone",
        "Dante",
        "Malini",
        "Vernon",
        "Liepzig",
        "Wild",
        "Farquhar",
        "Thurston",
        "Page",
        "Dedi",
        "Hofzinser",
        "Farmer",
        "Burton",
        "Lorayne",
        "Devant",
        "Maskelyne",
        "Blaney",
        "Ortiz",
        "Munoz",
        "Bertram",
        "Daniels",
        "Beam",
        "Regal",
        "Ammar",
        "Nicola",
        "Fulves",
        "Ganson",
        "Close",
        "Jennings",
        "Cervon",
        "Annemann"
        ]

myTree = AVL_Tree()

for val in values:
    myTree.insert(val)
myTree.display()

# sample output
        ##  Houdini
        ##-- l< Copperfield
        ##---- l< Blackstone
        ##------ l< Beam
        ##-------- l< Ammar
        ##---------- r> Annemann
        ##-------- r> Bertram
        ##------ r> Burton
        ##-------- l< Blaney
        ##-------- r> Cervon
        ##---------- l< Cardini
        ##---------- r> Close
        ##---- r> Farmer
        ##------ l< Dedi
        ##-------- l< Dante
        ##---------- l< Daniels
        ##-------- r> Devant
        ##------ r> Fulves
        ##-------- l< Farquhar
        ##-------- r> Hofzinser
        ##---------- l< Ganson
        ##-- r> Ortiz
        ##---- l< Malini
        ##------ l< Liepzig
        ##-------- l< Jennings
        ##-------- r> Lorayne
        ##------ r> Munoz
        ##-------- l< Maskelyne
        ##-------- r> Nicola
        ##---- r> Thurston
        ##------ l< Page
        ##-------- r> Regal
        ##------ r> Vernon
        ##-------- r> Wild

myTree.delete("Farmer")
myTree.delete("Houdini")
myTree.delete("Maskelyne")
myTree.display()

# sample output
        ##  Jennings
        ##-- l< Copperfield
        ##---- l< Blackstone
        ##------ l< Beam
        ##-------- l< Ammar
        ##---------- r> Annemann
        ##-------- r> Bertram
        ##------ r> Burton
        ##-------- l< Blaney
        ##-------- r> Cervon
        ##---------- l< Cardini
        ##---------- r> Close
        ##---- r> Farquhar
        ##------ l< Dedi
        ##-------- l< Dante
        ##---------- l< Daniels
        ##-------- r> Devant
        ##------ r> Ganson
        ##-------- l< Fulves
        ##-------- r> Hofzinser
        ##-- r> Ortiz
        ##---- l< Malini
        ##------ l< Liepzig
        ##-------- r> Lorayne
        ##------ r> Munoz
        ##-------- r> Nicola
        ##---- r> Thurston
        ##------ l< Page
        ##-------- r> Regal
        ##------ r> Vernon
        ##-------- r> Wild


n = 1000
newTree = AVL_Tree()
# generate the tree with n random values
for i in range(n):
        newTree.insert(randrange(0, n))
# delete a value from the tree
#insert a new distinct value into the tree
for j in range(n):
        newTree.delete(randrange(0, n))
        newTree.insert(randrange(0, 50))
# print the number of total balance operations
newTree.printCount()
        




