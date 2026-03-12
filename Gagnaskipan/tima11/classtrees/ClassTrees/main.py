import random
from binary_tree_abc import BinaryTree, Position
from binary_tree_linked import BinaryTreeLinked

def random_element() -> int:
    """
    Returns a random integer element in the range [1, 10)
    """
    return random.randrange(1, 10)


def random_non_empty_tree() -> BinaryTree:
    """
    Returns a randomly populated binary tree (of a minimum/maximum height).
    """
    def random_extend(tree: BinaryTree, pos: Position, max_height, height):
        if pos is None or height >= max_height:
            return
        if height == 0 or random.random() > 0.7:
            random_extend(tree, tree.add_left_child(pos, random_element()), max_height, height + 1)
        if height == 0 or random.random() > 0.7:
            random_extend(tree, tree.add_right_child(pos, random_element()), max_height, height + 1)

    tree = BinaryTreeLinked()
    tree.add_root(random_element())
    random_extend(tree, tree.root(), 5, 0)
    return tree


def pre_order(tree: BinaryTree, pos: Position, elems: list[object]):
    """
    Traversal of the binary tree, accumulating in a list a pre-order of its elements.
    """
    if pos is None:
        return
    
    curr = pos.handle

    elems.append(curr.element)

    if curr.left is not None:
        pre_order(tree, Position(curr.left), elems)

    if curr.right is not None:
        pre_order(tree, Position(curr.right), elems)
            

def post_order(tree: BinaryTree, pos: Position, elems: list[object]):
    """
    Traversal of the binary tree, accumulating in a list a post-order of its elements.
    """
    if pos is None:
        return
    
    curr = pos.handle

    if curr.left is not None:
        post_order(tree, Position(curr.left), elems)

    if curr.right is not None:
        post_order(tree, Position(curr.right), elems)
        
    elems.append(curr.element)

def in_order(tree: BinaryTree, pos: Position, elems: list[object]):
    """
    Traversal of the binary tree, accumulating in a list a in-order of its elements.
    """
    if pos is None:
        return 
    
    curr = pos.handle 

    if curr.left is not None:
        in_order(tree, Position(curr.left),elems)

    elems.append(curr.element)

    if curr.right is not None:
        in_order(tree, Position(curr.right), elems)

def count(tree: BinaryTree, pos: Position, element: object) -> int:
    """
    Counts how often element occurs in the tree.
    """
    if pos is None:
        return 0
    
    if tree.get_at(pos) == element:
        n = 1
    else:
        n = 0
    
    # curr = pos.handle
    # if curr.element == element:
        # return 1 + count(tree, Position(curr.left), element)

    # if curr.left is not None:
    n += count(tree, tree.left_child(pos), element)

    # if curr.right is not None:
    n += count(tree, tree.right_child(pos), element)

    return n
    

def elements_at_leaves(tree: BinaryTree, pos: Position, elems: list[object]):
    """
    Accumulates the elements at the leaves into a list (left-to-right).
    """

    if pos is None:
        return 
    
    curr = pos.handle 
    
    if curr.left is not None:
        elements_at_leaves(tree, Position(curr.left), elems)
    
    if curr.right is not None:
        elements_at_leaves(tree, Position(curr.right), elems)

    if curr.left is None and curr.right is None:
        elems.append(curr.element)

    return elems


random.seed(42)
for _ in range(5):
    print('-------------------------')
    btree = random_non_empty_tree()
    print(btree)
    elements = []
    pre_order(btree, btree.root(), elements)
    print('pre_order =', elements)
    elements.clear()
    post_order(btree, btree.root(), elements)
    print('post_order =', elements)
    elements.clear()
    in_order(btree, btree.root(), elements)
    print('in_order =', elements)
    elements.clear()
    elements_at_leaves(btree, btree.root(), elements)
    print('leaves =', elements)
    print('count(2) =', count(btree, btree.root(), 2))
