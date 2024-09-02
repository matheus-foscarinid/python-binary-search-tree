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


if __name__ == '__main__':
    unittest.main()