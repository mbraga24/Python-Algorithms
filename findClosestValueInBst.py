# /////////////////////////////////
          # RECURSIVELY
# /////////////////////////////////

# AVERAGE CASE:
# Time Complexity: O(log(n))
#   The same reason most methods in a BST are O(log(n)) because we will be eliminating on average 
#   half the tree every time we explore a node. 
# Space Complexity: O(log(n))
  # If we implement this algorithm recursively we will be calling the helper function multiple times
  # as we look into each value. That means we will be adding multiple frames on the call stack and 
  # using up extra memory.

# WORST CASE:
  # Time Complexity: O(n)
  #   The reason why it's O(n) is because if we have a tree that has one branch, we can't really
  #   take advantage of the BST property because we never really eliminate part of the tree.
  #   For example:
  #     Given the target: 40
  #     Given the tree: 10 -> 13 -> 18 -> 22 -> 35 -> 45
  #   The worst case scenario is that we will go down the entire tree and never eliminate half the tree.

  # Space Complexity: O(n)
    # That's also gonna be O(n) because we will be calling the recursive function on every node, in the worst case.

def findClosestValueInBst(tree, target):
  return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
  if tree is None:
    return closest
  if abs(target - closest) > abs(target - tree.value):
    closest = tree.value
  if target < tree.value:
    return findClosestValueInBstHelper(tree.left, target, closest)
  elif target > tree.value:
    return findClosestValueInBstHelper(tree.right, target, closest)
  else:
    return closest

# /////////////////////////////////
        # ITERATIVELY
# /////////////////////////////////

# AVERAGE CASE:
# Time Complexity: O(log(n))
  #   The same reason most methods in a BST are O(log(n)) because we will be eliminating on average 
  #   half the tree every time we explore a node. 
# Space Complexity: O(1)
  # We're not using up frames in the call stack and calling on a helper function multiple times. 
  # It will simply be constant space complexity.

# WORST CASE:
  # Time Complexity: O(n)
    #   The reason why it's O(n) is because if we have a tree that has one branch, we can't really
    #   take advantage of the BST property because we never really eliminate part of the tree.
    #   For example:
    #     Given the target: 40
    #     Given the tree: 10 -> 13 -> 18 -> 22 -> 35 -> 45
    #   The worst case scenario is that we will go down the entire tree and never eliminate half the tree.

  # Space Complexity: O(1)
    # We're not using up frames in the call stack and calling on a helper function multiple times. 
    # It will simply be constant space complexity.

def findClosestValueInBst(tree, target):
  currentNode = tree
  closest = tree.value
  while currentNode is not None:
    if abs(target - closest) > abs(target - currentNode.value):
      closest = currentNode.value
    if target < currentNode.value:
      currentNode = currentNode.left
    elif target > currentNode.value:
      currentNode = currentNode.right
    else:
      break
  return closest






