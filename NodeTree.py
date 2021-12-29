# code for NodeTree is based and modified from the following:
# https://www.programiz.com/dsa/huffman-coding

class NodeTree():

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __str__(self):
        return '%s_%s' % (self.left, self.right)