from BinarySearchTreeADT import BinarySearchTreeADT

class Node:
  def __init__(self, key: object, value: object) -> None:
    self.key = key
    self.value = value
    self.left: Node = None
    self.right: Node = None

  def __str__(self) -> str:
    return str(self.key)

  def next(self, other_key: object) -> 'Node':
    return self.left if other_key < self.key else self.right

class BinarySearchTree(BinarySearchTreeADT):
  def __init__(self) -> None:
    self._root: Node = None

  def insert(self, key: object, value: object) -> None:
    def insert(current: Node, key: object, value: object) -> Node:
      if current is None:
        return Node(key, value)
      elif key > current.key:
        current.right = insert(current.right, key, value)
      elif key < current.key:
        current.left = insert(current.left, key, value)
      return current

    self._root = insert(self._root, key, value)

  def __find_node(self, node: Node, key: object) -> Node:
    if node is None or node.key == key:
      return node
    # if the key is less than the node's key, search the left subtree
    # because the left subtree contains the keys that are smaller
    if node.key > key:
      return self.__find_node(node.left, key)
    # else search the right subtree because the right subtree contains
    # the keys that are greater
    else:
      return self.__find_node(node.right, key)

  def count_internal(self) -> int:
    def count_internal(node: Node) -> int:
      # if the node is None, return 0
      if node is None:
        return 0

      # if the node is a leaf, return 0
      if node.left is None and node.right is None:
        return 0

      left_count = count_internal(node.left)
      right_count = count_internal(node.right)

      # if the node is not a leaf, return 1 because it is an internal node
      # plus the left and right counts
      return 1 + left_count + right_count

    # special case that checks the root
    # if the tree is empty or it has no children
    if self._root is None or (self._root.left is None and self._root.right is None):
      return 0

    left_count = count_internal(self._root.left)
    right_count = count_internal(self._root.right)

    # return the sum of the left and right counts
    return left_count + right_count

  def degree(self, key: object) -> int:
    def degree(node: Node) -> int:
      # if the node is None, return -1
      if node is None:
        return -1

      # if the node has no children, return 0
      if node.left is None and node.right is None:
        return 0

      # if the node has two children, return 2
      if node.left is not None and node.right is not None:
        return 2

      # if the node has only one child, return 1
      return 1

    # first find the node with the given key
    node = self.__find_node(self._root, key)
    # then return the degree of the node using the private helper function
    return degree(node)

  def height(self, key: object) -> int:
    def height(node: Node) -> int:
      # if the node is None, return -1
      # it's easier because the height of a leaf is 0 and the height of None is -1
      # so we can return -1 for None and 0 for a leaf, because -1 + 1 = 0
      if node is None:
        return -1

      left_height = height(node.left)
      right_height = height(node.right)

      # return the maximum height of the left and right subtrees
      return 1 + max(left_height, right_height)

    # first find the node with the given key
    node = self.__find_node(self._root, key)
    # then return the height of the node using the private helper function
    return height(node)

if __name__ == "__main__":
    # creating a simple BST, usefull for testing :)
    bst = BinarySearchTree()
    bst.insert(10, 10)
    bst.insert(5, 5)
    bst.insert(15, 15)
    bst.insert(2, 2)
    bst.insert(7, 7)
    bst.insert(20, 20)
    bst.insert(19, 19)
    bst.insert(21, 21)

    print(bst.count_internal())