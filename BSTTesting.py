import unittest

from BinarySearchTree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.insert(10, 10)
        self.bst.insert(5, 5)
        self.bst.insert(15, 15)
        self.bst.insert(3, 3)
        self.bst.insert(7, 7)
        self.bst.insert(12, 12)
        self.bst.insert(18, 18)

    def test_search(self):
        self.assertEqual(self.bst.search(10), 10)
        self.assertEqual(self.bst.search(5), 5)
        self.assertEqual(self.bst.search(15), 15)
        self.assertEqual(self.bst.search(3), 3)
        self.assertEqual(self.bst.search(7), 7)
        self.assertEqual(self.bst.search(12), 12)
        self.assertEqual(self.bst.search(18), 18)
        self.assertEqual(self.bst.search(100), None)

    def test_delete(self):
        # leaf
        self.assertTrue(self.bst.delete(3)) 
        self.assertIsNone(self.bst.search(3))

        # node with one child
        self.assertTrue(self.bst.delete(5))
        self.assertIsNone(self.bst.search(5))

        # node with two children
        self.assertTrue(self.bst.delete(10))
        self.assertIsNone(self.bst.search(10))

        # node not found
        self.assertFalse(self.bst.delete(100))

    def test_clear(self):
        self.bst.clear()
        self.assertTrue(self.bst.is_empty())

    def test_is_empty(self):
        self.assertFalse(self.bst.is_empty())
        self.bst.clear()
        self.assertTrue(self.bst.is_empty())

    def test_str(self):
        # just check if the string representation is not empty 
        self.assertNotEqual(str(self.bst), '[empty]')
        self.bst.clear()
        # after clearing the tree, the string representation should be '[empty]'
        self.assertEqual(str(self.bst), '[empty]')

    def test_count_internal(self):
        # check if the bst has 2 internal nodes 
        self.assertEqual(self.bst.count_internal(), 2)

        # test with an empty tree
        self.bst.clear()
        self.assertEqual(self.bst.count_internal(), 0)

        # test with just root and a leaf
        self.bst.insert(10, 10)
        self.bst.insert(5, 5)
        self.assertEqual(self.bst.count_internal(), 0)

        # add another node to have 1 internal node
        self.bst.insert(3, 3)
        self.assertEqual(self.bst.count_internal(), 1)

    def test_degree(self):
        # with 2 children 
        self.assertEqual(self.bst.degree(10), 2)
        self.assertEqual(self.bst.degree(5), 2)
        self.assertEqual(self.bst.degree(15), 2)

        # leaf nodes
        self.assertEqual(self.bst.degree(3), 0)
        self.assertEqual(self.bst.degree(7), 0)
        self.assertEqual(self.bst.degree(12), 0)
        self.assertEqual(self.bst.degree(18), 0)

        # node with one child
        # we need to insert first because i did not remember to add 
        # this case with just one child in the setUp method :(
        self.bst.insert(8, 8)
        self.bst.insert(2, 2)
        self.assertEqual(self.bst.degree(7), 1)
        self.assertEqual(self.bst.degree(3), 1)

        # not found
        self.assertEqual(self.bst.degree(100), -1)

    def test_height(self):
        self.assertEqual(self.bst.height(10), 2)

        self.assertEqual(self.bst.height(5), 1)
        self.assertEqual(self.bst.height(15), 1)

        self.assertEqual(self.bst.height(3), 0)
        self.assertEqual(self.bst.height(7), 0)
        self.assertEqual(self.bst.height(12), 0)
        self.assertEqual(self.bst.height(18), 0)

        self.assertEqual(self.bst.height(100), -1)

    def test_level(self):
        self.assertEqual(self.bst.level(10), 0)

        self.assertEqual(self.bst.level(5), 1)
        self.assertEqual(self.bst.level(15), 1)

        self.assertEqual(self.bst.level(3), 2)
        self.assertEqual(self.bst.level(7), 2)
        self.assertEqual(self.bst.level(12), 2)
        self.assertEqual(self.bst.level(18), 2)

        self.assertEqual(self.bst.level(100), -1)

    def test_ancestor(self):
        self.assertEqual(self.bst.ancestor(10), '10')

        self.assertEqual(self.bst.ancestor(5), '10 5')
        self.assertEqual(self.bst.ancestor(15), '10 15')

        self.assertEqual(self.bst.ancestor(3), '10 5 3')
        self.assertEqual(self.bst.ancestor(7), '10 5 7')
        self.assertEqual(self.bst.ancestor(12), '10 15 12')
        self.assertEqual(self.bst.ancestor(18), '10 15 18')
        
        self.assertEqual(self.bst.ancestor(100), None)

if __name__ == '__main__':
    unittest.main()