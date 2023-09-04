import heapq
from dataclasses import dataclass
from typing import Union


@dataclass
class HNode:
    occurrence: int
    left: Union['HNode', 'HTree', None]
    right: Union['HNode', 'HTree', None]

    def __init__(self, occurrence, left=None, right=None):
        self.occurrence = occurrence
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.occurrence < other.occurrence

    def is_leaf(self):
        # checks if the node is a leaf (has no left and right children)
        return not isinstance(self.left, HNode) and not isinstance(self.right, HNode)


@dataclass
class HTree:
    left: ['HTree', None]
    right: ['HTree', None]

    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

    def __str__(self):
        return f"HTree(occurrence = {self.root.occurrence})"


def build_huffman_tree(char_occurrences, input_str):
    priority_queue = [HNode(occurrence=char_occurrences[i], left=None, right=None) for i in range(256)]
    if char_occurrences(chr(input_str)) > 0:
        # HLeaf represents individual char as leaf nodes in the tree. each HLeaf
        # object contains info on character
        # and its occurrence count.
        heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged_node = HNode(occurrence=left_child.occurrence + right_child.occurrence,
                            left=left_child, right=right_child)
        heapq.heappush(priority_queue, merged_node)

    return HTree(root=priority_queue[0], left=char_occurrences, right=char_occurrences)


def generate_huffman_codes(self):
    # initializes empty dictionary to store the Huffman tree
    huffman_codes = {}

    # start recursive traversal of root of tree
    self._generate_codes_recursive(self.root, "", huffman_codes)

    return huffman_codes


def _generate_codes_recursive(self, node, current_node, huffman_codes):
    # base case: if current node is a leaf and add its code to dictionary
    if node.is_leaf():
        huffman_codes[node.char] = current_node
        return

    # recursive traversal of left child with '0' appended to code
    if node.left:
        self._generate_codes_recursive(node.left, current_node + "0", huffman_codes)
    # recursive traversal of right child with appended '1' to code
    if node.right:
        self._generate_codes_recursive(node.right, current_node + "1", huffman_codes)


@dataclass
class HTLeaf:
    def __init__(self, character, occurrence):
        self.character = character
        self.occurrence = occurrence
        self.head = None

    def __lt__(self, other):
        return self.occurrence < other.occurrence

    def __le__(self, other):
        return self.occurrence <= other.occurrence


def tree_lt(self, other):
    return self.occurrence < other.occurrence


def cnt_freq(input_str):
    char_freq = {}

    # initialize the numpy array of s256 filled with zeros inclusive
    for char in input_str:
        # loops through each character in the input string
        char_code = ord(char)

        if char_code <= 255:
            char_freq[char] = char_freq.get(char, 0) + 1

        return char_code


char_freq = {
    'a': 5,
    'b': 9,
    'c': 12,
    'd': 13,
    'e': 16,
    'f': 45
}


@dataclass
class HTListNode:
    def __init__(self, tree: 'HTree', next_node=None):
        self.tree = tree
        self.next_node = next_node

        tree: HTree
        self.next_node = next_node


@dataclass
class HTList:
    def __init__(self, head=None):
        self.head = head
        self.unsorted_list = []

    def append(self, tree: Union[HTree, HTLeaf]):
        new_node = HTListNode(tree)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node.next_node

    def display(self):
        current_node = self.head
        while current_node:
            current_node = current_node.next_node


def tree_list_insert(self, new_tree):
    new_node = HTListNode(new_tree)

    if not self.head:
        self.head = new_node
        return

    if tree_lt(new_tree, self.tree):
        new_node.next_node = self.head
        self.head = new_node
        return

    current = self.head
    while current.next_node and not tree_lt(new_tree, current.next_node.tree):
        current = current.next_node

    new_node.next_node = current.next_node
    current.next_node = new_node


def base_tree_list(occurrence):
    tree_list = HTList()

    for i in range(256):
        if occurrence[i] > 0:
            new_leaf = HTLeaf(chr(i), occurrence[i])
            tree_list.append(new_leaf)

    return tree_list


def initial_tree_sort(self, unsorted_list):
    sorted_list = HTList()

    for tree in unsorted_list:
        self.tree_list_insert(tree)

    return sorted_list


def append(self, tree: Union[HTree, HTLeaf]):
    new_node = HTListNode(tree)

    if not self.head:
        self.head = new_node
    else:
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node


def coalesce_once(ht_list: HTList):
    if not ht_list.head or not ht_list.head.next_node:
        raise ValueError("HTList must contain at least two nodes.")

    # get the first two nodes from the HTList
    first_node = ht_list.head
    second_node = ht_list.head.next_node

    # the new HNode will be created by combining the first and second nodes
    new_occurrence = first_node.tree.root.occurrence + second_node.tree.root.occurrence
    new_node = HNode(occurrence=new_occurrence, left=first_node.tree.root, right=second_node.tree.root)

    new_tree = HTree(root=new_node, left=None, right=None)

    new_node = HTListNode(tree=new_tree)

    # the head of HTList will be updated with the new node
    ht_list.head = new_node

    # insert the new node back into the HTlist
    current = ht_list.head
    while current.next_node and not tree_lt(new_tree.root, new_node.tree.root):
        current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    while ht_list.head.next_node and not tree_lt(ht_list.head.next_node.tree, new_tree.root):
        next_node = ht_list.head.next_node
        coalesce_once(ht_list)
        new_tree = ht_list.head.tree
        ht_list.head.next_node = next_node.next_node


def coalesce_all(ht_list: HTList):
    if not ht_list.head:
        raise ValueError("HTList must contain at least one node.")

    while ht_list.head.next_node:
        coalesce_once(ht_list)

    return ht_list.head.tree


def build_encoder_array(node, encoding_array, current_code=""):
    if node.character is not None:
        encoding_array[ord(node.character)] = current_code
        return
    if node.left:
        build_encoder_array(node.left, encoding_array, current_code + "0")
    if node.right:
        build_encoder_array(node.right, encoding_array, current_code + "1")


def encode_string_one(input_string, encoder_array):
    encoded_data = ""

    for char in input_string:
        encoding = encoder_array[ord(char)]
        if not encoding:
            raise ValueError(f"Character {char} not in encoder array.")
        encoded_data += encoding

    return encoded_data


def bits_to_char(bit_string):
    padded_bits = bit_string + "0" * (8 - len(bit_string) % 8)
    chars = []
    for i in range(0, len(padded_bits), 8):
        chunk = padded_bits[i:i + 8]
        decimal_value = int(chunk, 2)
        chars.append(chr(decimal_value))
    return "".join(chars)


def huffman_code_file(source_file, target_file, input_str):
    with open(source_file, "r") as f:
        input_string = f.read()

        huffman_tree = build_huffman_tree(cnt_freq(input_string), input_str)

        encoder_array = [""] * 256
        build_encoder_array(huffman_tree.root, encoder_array)

        encoded_data = encode_string_one(input_string, encoder_array)

    with open(target_file, "w") as f:
        byte_data = bytes(int(encoded_data[i:i + 8], 2) for i in range(0, len(encoded_data), 8))
        f.write(byte_data)


source_file = "/Volumes/Hesperides/proj_2/johnny-cash.txt"  # Replace with the path to your input text file
target_file = "encoded_output.bin"  # Replace with the desired output file path
# huffman_code_file(source_file, target_file)
print("File encoded and saved to:", target_file)


char_occurrences = {i: 0 for i in range(256)}  # Initialize all occurrences to 0

# Now update the occurrences for the specific characters
char_occurrences[65] = 3
char_occurrences[66] = 6
char_occurrences[67] = 1

# Input string for build_huffman_tree
input_str = 'A' * char_occurrences[65] + 'B' * char_occurrences[66] + 'C' * char_occurrences[67]

huffman_tree = build_huffman_tree(char_occurrences, input_str)

# Generate Huffman codes
huffman_codes = huffman_tree.generate_huffman_codes()

# Print Huffman codes
for char, code in huffman_codes.items():
    print(f"Character: {char}, Huffman Code: {code}")

