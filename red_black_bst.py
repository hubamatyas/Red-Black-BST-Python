class Node():
    def __init__(self, key, value, colour):
        self.right = None
        self.left = None
        self.key = key
        self.value = value
        self.colour = colour

class RedBlackBST():
    def __init__(self):
        self.RED = True
        self.BLACK = False
        self.root = None

    def is_red(self, node):
        if node is None:
            return False

        return node.colour is self.RED

    def is_empty(self):
        return self.root is None

    def look_up(self, key):
        return self.get(self.root, key)

    def get(self, node, key):
        if node is not None:
            if key < node.key:
                return self.get(node.left, key)
            elif key > node.key:
                return self.get(node.right, key)
            else:
                return node.key
                
        return "Key doesn't exist"     

    def insert(self, key, value):
        self.root = self.put(self.root, key, value)
        self.root.colour = self.BLACK

    def put(self, node, key, value):
        if node is None:
            return Node(key, value, self.RED)

        if key < node.key:
            node.left = self.put(node.left, key, value)
        elif key > node.key:
            node.right = self.put(node.right, key, value)
        else:
            node.value = value

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colours(node)

        return node

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.colour = node.colour
        node.colour = self.RED
        
        return x

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.colour = node.colour
        node.colour = self.RED

        return x

    def flip_colours(self, node):
        node.colour = not node.colour
        node.left.colour = not node.left.colour
        node.right.colour = not node.right.colour
    
    def min(self, node):
        if self.is_empty():
            return "BST is empty"

        if node.left is None:
            return node
        else:
            return self.min(node.left)

    def max(self, node):
        if self.is_empty():
            return "BST is empty"

        if node.right is None:
            return node
        else:
            return self.max(node.right)      
    
    def floor(self, node, key):
        if node is None:
            return None

        if key <= node.key:
            return self.floor(node.left, key)
        else:
            threshold = self.floor(node.right, key)

        if threshold is not None:
            return threshold
        else:
            return node.key
    
    def ceiling(self, node, key):
        if node is None:
            return None

        if key >= node.key:
            return self.ceiling(node.right, key)
        else:
            threshold = self.ceiling(node.left, key)

        if threshold is not None:
            return threshold
        else:
            return node.key

    def get_range(self, low, high):
        range_list = []
        self.range(range_list, self.root, low, high)
        return range_list

    def range(self, list, node, low, high):
        if node is None:
            return
        
        if low < node.key:
            self.range(list, node.left, low, high)
        if low <= node.key and high >= node.key:
            list.append(node.key)
        if high > node.key:
            self.range(list, node.right, low, high)