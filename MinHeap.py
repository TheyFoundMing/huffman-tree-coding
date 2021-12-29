# code for minheap is based and modified from the following
# https://www.programiz.com/dsa/heap-data-structure

# creates the priority queue for the huffman tree
class MinHeap:

    def __init__(self):
        self.__array = []

    # inserts the node into the minheap
    def insert_node(self, node): 
        size = len(self.__array)
        
        # if there is nothing in the array, simply append into it
        if size == 0:
            self.__array.append(node)
        # if there is, append then heapify the whole tree
        else:
            self.__array.append(node)
            for i in range((size//2)-1, -1, -1):
                self.heapify(self.__array, size, i)
            
    def extract_node(self):
        # swaps the first node with the last node before deleting the last node
        self.__array[0], self.__array[-1] = self.__array[-1], self.__array[0]
        popped = self.__array.pop()

        size = len(self.__array)

        # heapify is called to make sure that the nodes are in order
        for i in range((size//2), -1, -1):
            self.heapify(self.__array, size, i)

        return popped

    def heapify(self, array, n, i):
        # array[i][0] letter
        # array[i][1] freq count

        smallest = i    # largest val index
        l = 2 * i + 1   # left child index
        r = 2 * i + 2   # right child index

        # if left child is within range of array's size and is smaller than the parent node
        # left child will become the smallest node
        if l < n and array[i][1] > array[l][1]:
            smallest = l

        # if right child is within range of array's size and is smaller than the smallest node
        # right child will become the smallest node
        if r < n and array[smallest][1] > array[r][1]:
            smallest = r

        # if the smallest node was replaced with either left or right child,
        # both parent and smallest node will swap and call heapify again 
        if smallest != i:
            self.__array[i], self.__array[smallest] = self.__array[smallest], self.__array[i]
            self.heapify(array, n, smallest)

    def get_tree(self):
        return self.__array

    def get_tree_length(self):
        return len(self.__array)