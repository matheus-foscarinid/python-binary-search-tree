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


if __name__ == '__main__':
    unittest.main()