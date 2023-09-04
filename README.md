# Tree Code Example (Python)
 The purpose of this assignment was to construct a Huffman tree from character occurrences and generate Huffman codes.
 It was also to demonstrate knowledge and understanding of the widely used Huffman code algorithm for lossless data compression, where characters are encoded with variable-lengths, and shorter codes are assigned to more frequent characters.
 Huffman codes can be used for data compression and decompression.
 # Key Features
Build the Huffman Tree: obviously as the name presents itself the purpose of this function is to construct a Huffman tree based on character occurrences in a given input string.
The input for this function 'char_occurrences', is a dictionary where keys represent character indices[0, 255], and the values represent the occurrences of each character in the input string.
The function initializes a priority queue of ‘HNode’ objects, which each represent a character and it’s occurrence count.
‘HNode’ objects are for all characters that range from 0-255, initializing the occurrences to 0.
For characters with occurrences greater than 0 in the input string, their ‘HNode’ objects are added to the priority queue. 
This function then builds the Huffman tree by repeatedly merging the two nodes with lowest occurrences until only one node remains in the queue. 
The final Huffman tree is represented by an ‘HTree’ object and is returned.

Huffman Code Generation: The purpose of this segment of the code is to generate Huffman codes for characters within the Huffman tree.
‘generate_huffman_codes’ is a method that is called upon by the ‘HTree’ object (Huffman tree).
It will initialize an empty dictionary ‘huffman_codes’ to store the mapping of characters to their Huffman code
The method then starts a recursive traversal through the Huffman trees, starting from the root_node. 
For each leaf_node encountered during traversal, the character and its corresponding Huffman code are then added to the ‘huffman_codes’ dictionary containing all Huffman codes for all characters in the tree.
