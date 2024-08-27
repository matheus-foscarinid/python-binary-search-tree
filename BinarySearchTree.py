from BinarySearchTreeADT import BinarySearchTreeADT

class Node:
  def __init__(self, key: object, value: object) -> None:
    self.key = key
    self.value = value
    self.left: Node = None
    self.right: Node = None

  def __str__(self) -> str:
    return str(self.key)

  def next(self, other_key: object) -> Node:
    return self.left if other_key < self.key else self.right

class LinkedBinarySearchTree(BinarySearchTreeADT):
  def count_internal(self) -> int:
    # special case that checks the root
    # If the tree is empty or it has no children
    if self._root is None or (self._root.left is None and self._root.right is None):
      return 0

    def __count_internal(self, node: Node) -> int:
      # if the node is None, return 0
      if node is None:
        return 0

      # if the node is a leaf, return 0
      if node.left is None and node.right is None:
        return 0

      left_count = __count_internal(node.left)
      right_count = __count_internal(node.right)

      # if the node is not a leaf, return 1 because it is an internal node
      # plus the left and right counts
      return 1 + left_count + right_count

    left_count = __count_internal(_root.left)
    right_count = __count_internal(self._root.right)

    # return the sum of the left and right counts
    return left_count + right_count

  def degree(self, key: Node) -> int: ...
  def height(self, key: Node) -> int: ...
  def level(self, key: Node) -> int: ...
  def ancestor(self, key: Node) -> str: ...