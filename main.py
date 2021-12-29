# code for both huffman and min heaps are based and modified from the following:
# https://www.programiz.com/dsa/heap-data-structure
# https://www.programiz.com/dsa/huffman-coding

from MinHeap import MinHeap
from Huffman import Huffman
from NodeTree import NodeTree

# where all the insertions are made
def main():
    # create instances of minheap and huffman
    minheap = MinHeap()
    huffman = Huffman()

    # created dictionary based on the values from A3 file
    dictionary = {
        'A': 77, 
        'B': 17,
        'C': 32,
        'D': 42,
        'E': 120,
        'F': 24,
        'G': 17,
        'H': 50,
        'I': 76, 
        'J': 4,
        'K': 7,
        'L': 42,
        'M': 24,
        'N': 67, 
        'O': 67,
        'P': 20,
        'Q': 5, 
        'R': 59, 
        'S': 67, 
        'T': 85, 
        'U': 37,
        'V': 12, 
        'W': 22, 
        'X': 4, 
        'Y': 22, 
        'Z': 2
    }

    # turning key, values into tuples so they could be
    # inserted into the minheap
    tuples_dict = list(dictionary.items())
    size = len(dictionary)

    for i in range(size):
        minheap.insert_node(tuples_dict[i])

    # instead of an array, we make use of a minheap
    # the first two extracted nodes are placed in a node tree 
    # and inserted in the minheap again to have it sorted accordingly
    while minheap.get_tree_length() > 1 :
        letter1, freq1 = minheap.extract_node()
        letter2, freq2 = minheap.extract_node()

        node = NodeTree(letter1, letter2)
        total = freq1 + freq2

        # pushes nodetree and total sum back into the minheap
        minheap.insert_node((node, total))

    # take the remaining node in the minheap and create a
    # huffman code dictionary 
    node = minheap.extract_node()
    huffmanCode = huffman.get_codes(node[0])

    # to keep total sum
    total_sum = 0
    
    # since the dictionary was already sorted beforehand,
    # there is no need to sort & simply just print out the freq & codes
    # and calculate the length, freq x length
    print(' Char | Freq |    Code    | Len | Freq_Len |')
    print('----------------------')
    for char in dictionary:
        length = len(huffmanCode[char])
        freq_length = dictionary[char] * length
        total_sum += freq_length

        print(' %-4r | %-4d | %10s | %-3d | %-8d |' % (char, dictionary[char], huffmanCode[char], length, freq_length ))        

    print("\nThe weighted minimum path length is: {} ".format(total_sum))

main()