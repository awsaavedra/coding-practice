"""
Root: The node in a nonempty tree who has no parent (top of tree)
Parent-child relationship:
  1. A child has only one parent (unique)
  2. A parent can have >= 1 children and has a limit set on the tree type
    i.e. a BST parent can only have 2 descendants
Leaves: leaves without any children with a parent
Siblings: Two nodes that are children of the same parent
Ancestor: should be obvious
"""
class BinaryTree:
  def __init__(self):
    self = null