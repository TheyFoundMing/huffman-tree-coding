# code for Huffman is based and modified from the following:
# https://www.programiz.com/dsa/huffman-coding

class Huffman:

    def __init__(self):
        pass

    def get_codes(self, node, left=True, binString=""):
        # node: NodeTree

        # when we reach a leaf, it would return a str instead
        # of a NodeTree
        if type(node) is str:
            return {node: binString}
        
        # in this case, NodeTree instead of str
        d = {}
        left = node.get_left()
        right = node.get_right()

        # traversing through the tree
        # binString will append 0 when it traverses left
        # binString will append 1 when it traverses right
        # dictionary tree will grow bigger and bigger as it goes
        # through every node
        d.update(self.get_codes(left, True, binString + '0'))
        d.update(self.get_codes(right, False, binString + '1'))

        return d
