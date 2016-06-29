import sys

#
# The following program computes the least common ancestor and hence the distance of a binary tree
#

globvar_var1_ht = -1
globvar_var2_ht = -1

class BinaryTree() :

    def __init__(self, rootid):
        self.left = None
        self.right = None
        self.rootid = rootid
        self.height = -1

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, value):
        self.rootid = value

    def getNodeValue(self):
        return self.rootid

    def setNodeHeight(self, val):
        self.height = val

    def getNodeHeight(self):
        return self.height

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree


    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree

    def printInorder(self):
        if self != None:
            left_child = self.getLeftChild();
            right_child = self.getRightChild();

            if left_child != None:
                left_child.printInorder()

            print(self.rootid)

            if right_child != None:
                right_child.printInorder()


    def LCA(self, val1, val2):

        global globvar_var1_ht
        global globvar_var2_ht

        if self != None:
            if (self.rootid == val1):
                return self
            elif (self.rootid == val2):
                return self
            else:
                left_child = self.getLeftChild()
                if (left_child != None and left_child.getNodeHeight() == -1):
                    left_child.setNodeHeight(self.getNodeHeight() + 1)

                right_child = self.getRightChild();
                if (right_child != None and right_child.getNodeHeight() == -1):
                    right_child.setNodeHeight(self.getNodeHeight() + 1)

                left = None
                right = None

                if (left_child != None):
                    left = left_child.LCA(val1, val2)

                if (right_child != None):
                    right = right_child.LCA(val1, val2)

                if left != None and  right != None:
                    globvar_var1_ht = left.getNodeHeight()
                    globvar_var2_ht = right.getNodeHeight()
                    return self
                elif (left != None):
                    return left
                else :
                    return right
        else:
            return None;

def main():
    print("Starting the program to test")
    testTree = BinaryTree(50)
    testTree.setNodeHeight(0)
    testTree.insertLeft(200)
    testTree.getLeftChild().insertRight(400)
    testTree.insertLeft(210)
    testTree.getLeftChild().insertRight(430)
    testTree.getLeftChild().getRightChild().insertLeft(435)
    testTree.insertRight(420)
    testTree.getRightChild().insertRight(450)
    testTree.getRightChild().insertLeft(417)

    testTree.printInorder()


    node = testTree.LCA(435, 417)

    print("The lowest common ancestor is :", node.rootid, node.getNodeHeight(), globvar_var1_ht, globvar_var2_ht)
    dist = globvar_var1_ht + globvar_var2_ht - 2 * node.getNodeHeight()
    print("The distance is :", dist)

if __name__ == '__main__':
    main()

