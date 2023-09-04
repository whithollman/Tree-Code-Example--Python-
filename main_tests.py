import unittest
import numpy as np
from main import cnt_freq, HNode, HTLeaf, HTree, tree_lt, HTList, HTListNode, base_tree_list


class TestHNodeAndHLeaf(unittest.TestCase):

    def test_hnode_attributes(self):
        left_leaf = HTLeaf('a', 2)
        right_leaf = HTLeaf('b', 3)
        hnode = HNode(5, left_leaf, right_leaf)

        # testing attributes of the HNode instance
        self.assertEqual(hnode.occurrence, 5)
        self.assertEqual(hnode.left, left_leaf)
        self.assertEqual(hnode.right, right_leaf)

    def test_hleaf_attributes(self):
        # creates an HLeaf instance
        hleaf = HTLeaf('c', 4)

        self.assertEqual(hleaf.character, 'c')
        self.assertEqual(hleaf.occurrence, 4)

    def test_hnode_comparison(self):
        # different instance comparison
        hnode1 = HNode(5, None, None)
        hnode2 = HNode(8, None, None)

        # and use the lt_method to test the different comparisons
        self.assertTrue(hnode1 < hnode2)
        self.assertFalse(hnode2 < hnode1)

    def test_hleaf_comparison(self):
        # comparison of two difference occurrences
        hleaf1 = HTLeaf('d', 3)
        hleaf2 = HTLeaf('e', 6)

        # and using lt_method to test the comparison difference
        self.assertTrue(hleaf1 < hleaf2)
        self.assertFalse(hleaf2 < hleaf1)


class TestHuffmanFunctions(unittest.TestCase):

    def test_cnt_freq(self):
        input_str = "ddddddddddddddddccccccccbbbbaaff"
        character_counts = cnt_freq(input_str)
        expected_counts = np.array([0, 2, 4, 8, 16, 0, 2, 0] + [0] * 248)
        self.assertFalse(np.array_equal(character_counts, expected_counts))

    def test_huffman_tree(self):
        character_counts = np.array([0, 3, 2, 5, 1, 4] + [0] * 251)
        huffman_tree = HTree(character_counts)

    def test_tree_lt(self):
        tree1 = HTree(cnt_freq("khook"))
        tree2 = HTree(cnt_freq("khasseef"))
        self.assertTrue(tree_lt(tree1, tree2))

        tree1 = HTree(cnt_freq("badjens"))
        tree2 = HTree(cnt_freq("hapoo"))
        self.assertFalse(tree_lt(tree1, tree2))


class TestHTListNode(unittest.TestCase):
    def test_node_creation(self):
        tree = HTree(cnt_freq("khhok"))
        node = HTListNode(tree)
        self.assertEqual(node.tree, tree)
        self.assertIsNone(node.next_node)

    def test_appending_node(self):
        tree1 = HTree(cnt_freq("khoo"))
        tree2 = HTree(cnt_freq("Khookeh"))
        node1 = HTListNode(tree1)
        node2 = HTListNode(tree2)
        node1.next_node = node2
        self.assertIs(node1.next_node, node2)
        self.assertIs(node2.next_node, None)


class TestHTList(unittest.TestCase):
    def test_empty_list_creation(self):
        hlist = HTList()
        self.assertIsNone(hlist.head)

    def test_appending_nodes_to_list(self):
        hlist = HTList()
        tree1 = HTree(cnt_freq("khook"))
        tree2 = HTree(cnt_freq("khessafat"))
        hlist.append(tree1)
        hlist.append(tree2)
        self.assertEqual(hlist.head.tree, tree1)
        self.assertEqual(hlist.head.next_node.tree, tree2)


if __name__ == '__main__':
    unittest.main()
