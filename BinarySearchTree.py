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

# Grupo 3
# Nomes: Matheus Foscarini Dias, Enzo Boadas e Mirágini Victória Silveira Malgarizi
class BinarySearchTree(BinarySearchTreeADT):
  def __init__(self) -> None:
    self._root: Node = None

  def __str__(self) -> str:
    return '[empty]' if self.is_empty() else self._str_tree()

  def _str_tree(self) -> str:
    def _str_tree(current: Node, is_right: bool, tree: str, ident: str) -> str:
      if current.right:
        tree = _str_tree(current.right, True, tree, ident + (' ' * 8 if is_right else ' |' + ' ' * 6))

      tree += ident + (' /' if is_right else ' \\') + "----- " + str(current) + '\n'
      if current.left:
        tree = _str_tree(current.left, False, tree, ident + (' |' + ' ' * 6 if is_right else ' ' * 8))
      return tree

    tree: str = ''
    if self._root.right:
      tree = _str_tree(self._root.right, True, tree, '')
    tree += str(self._root) + '\n'
    if self._root.left:
      tree = _str_tree(self._root.left, False, tree, '')
    return tree

  def clear(self) -> None:
    self._root = None

  def is_empty(self) -> bool:
    return self._root is None

  def search(self, key: object) -> object:
    def search(current: Node, key: object) -> object:
      if current is None:
        return None
      elif key == current.key:
        return current.value
      return search(current.next(key), key)

    return search(self._root, key)

  def delete(self, key: object) -> bool:
    return self._delete_by_copying(key)

  def _get_parent(self, key: object) -> Node:
    parent: Node = None
    current: Node = self._root
    while current and key != current.key:
      parent = current
      current = current.next(key)
    return parent, current

  def _delete_by_copying(self, key: object) -> bool:
    parent: Node; current: Node
    parent, current = self._get_parent(key)
    if current is None:
      return False
    # Case 3
    elif current.left and current.right:
      at_the_right: Node = current.left
      while at_the_right.right:
        at_the_right = at_the_right.right
      self._delete_by_copying(at_the_right.key)
      current.key, current.value = at_the_right.key, at_the_right.value
    # Case 1/2
    else:
      next_node: Node = current.left or current.right
      if current == self._root:
        self._root = next_node
      elif current == parent.left:
        parent.left = next_node
      else:
        parent.right = next_node
    return True

  def _delete_by_merging(self, key: object) -> bool:
    parent: Node; current: Node
    parent, current = self._get_parent(key)
    if current is None:
      return False
    # Case 3
    elif current.left and current.right:
      at_the_right: Node = current.left
      while at_the_right.right:
        at_the_right = at_the_right.right
      at_the_right.right = current.right

      if current == self._root:
        self._root = current.left
      elif parent.left == current:
        parent.left = current.left
      else:
        parent.right = current.left
    # Case 1/2
    else:
      next_node: Node = current.left or current.right
      if current == self._root:
        self._root = next_node
      elif current == parent.left:
        parent.left = next_node
      else:
        parent.right = next_node
    return True

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

  def _find_node(self, node: Node, key: object) -> Node:
    if node is None or node.key == key:
      return node
    # if the key is less than the node's key, search the left subtree
    # because the left subtree contains the keys that are smaller
    if node.key > key:
      return self._find_node(node.left, key)
    # else search the right subtree because the right subtree contains
    # the keys that are greater
    else:
      return self._find_node(node.right, key)

  def pre_order_traversal(self) -> None:
    def pre_order_traversal(current: Node) -> None:
      if current:
        print(current.key, end=' ')
        pre_order_traversal(current.left)
        pre_order_traversal(current.right)

    pre_order_traversal(self._root)

  def in_order_traversal(self) -> None:
    def in_order_traversal(current: Node) -> None:
      if current:
        in_order_traversal(current.left)
        print(current.key, end=' ')
        in_order_traversal(current.right)
    in_order_traversal(self._root)

  def post_order_traversal(self) -> None:
    def post_order_traversal(current: Node) -> None:
      if current:
        post_order_traversal(current.left)
        post_order_traversal(current.right)
        print(current.key, end=' ')
    post_order_traversal(self._root)

  def level_order_traversal(self) -> None:
    if self._root:
      queue = [self._root]
      while queue:
        current: Node = queue.pop(0)
        print(current.key, end=' ')
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

  def count_internal(self) -> int:
    def count_internal(node: Node) -> int:
      if node is None:
        return 0

      # if the node is a leaf
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

    return left_count + right_count

  def degree(self, key: object) -> int:
    def degree(node: Node) -> int:
      # if there is no node, return -1
      if node is None:
        return -1

      # if the node has no children, return 0
      if node.left is None and node.right is None:
        return 0

      # if the node has two children, return 2
      if node.left is not None and node.right is not None:
        return 2

      # and if the node has only one child, return 1
      return 1

    # first find the node with the given key
    node = self._find_node(self._root, key)
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
    node = self._find_node(self._root, key)
    # then return the height of the node using the private helper function
    return height(node)

  def level(self, key: object) -> int:
    def level(key: object, node: Node, curr_level: int) -> int:
      # if there's no node to search, return -1
      if node is None:
        return -1

      # if the key is equal, the node is found, return the current level 
      if node.key == key:
        return curr_level

      # search the left and right subtrees adding 1 to the current level
      left_level = level(key, node.left, curr_level + 1)
      right_level = level(key, node.right, curr_level + 1)

      return max(left_level, right_level)

    return level(key, self._root, 0)


  def ancestor(self, key: object) -> str:
    def ancestor(key: object, node: Node, path: str) -> str:
      # if there's no node to search, return an empty string
      # don't return the current path because the path can't lead to the key
      if node is None:
        return ""

      new_path = path + ' ' + str(node)
      # if the key is found, return the path
      if node.key == key:
        # remove spaces from the beginning and end of the string
        # because the path starts with a space
        return new_path.strip()

      left_path = ancestor(key, node.left, new_path)
      right_path = ancestor(key, node.right, new_path)

      # if the key is found in the left subtree, return the left path
      # both sizes can't contain the key because the key is unique
      if left_path:
        return left_path
      elif right_path:
        return right_path
      else:
        return None

    return ancestor(key, self._root, "")