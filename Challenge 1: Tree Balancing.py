#Challenge 1: Tree Balancing

class TreeNode:
    def __init__(self, val):
        self.val = val            # Valor del nodo
        self.left = None          # Hijo izquierdo
        self.right = None         # Hijo derecho
class BinarySearchTree:
    def __init__(self):
        self.root = None          # Raíz del árbol
    def insert(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)          # Crea un nuevo nodo si está vacío
            if val < node.val:
                node.left = _insert(node.left, val)   # Inserta a la izquierda
            else:
                node.right = _insert(node.right, val) # Inserta a la derecha
            return node
        self.root = _insert(self.root, val)   # Inicia desde la raíz
    def inorder(self):
        def _inorder(node):
            return _inorder(node.left) + [node] + _inorder(node.right) if node else []
        return _inorder(self.root)            # Devuelve los nodos en orden (ascendente)

def balance_bst(bst):
    """Balancea un BST sin cambiar el orden inorder."""
    nodes = bst.inorder()                     # Lista ordenada de nodos

    def build_balanced(start, end):
        if start > end:
            return None
        mid = (start + end) // 2              # Punto medio para balancear
        node = nodes[mid]
        node.left = build_balanced(start, mid - 1)   # Subárbol izquierdo
        node.right = build_balanced(mid + 1, end)    # Subárbol derecho
        return node
    new_bst = BinarySearchTree()
    new_bst.root = build_balanced(0, len(nodes) - 1)
    return new_bst

def test_balance_bst():
    """Test the balance_bst function. ⚖️"""
    # Test Case 1: Already balanced tree 🌳
    bst1 = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst1.insert(val)
    
    # Test Case 2: Right-skewed tree 📐➡️
    bst2 = BinarySearchTree()
    for val in [1, 2, 3, 4, 5]:
        bst2.insert(val)
    
    # Test Case 3: Left-skewed tree 📐⬅️
    bst3 = BinarySearchTree()
    for val in [5, 4, 3, 2, 1]:
        bst3.insert(val)
    
    # Test Case 4: Empty tree 🈳
    bst4 = BinarySearchTree()
    
    # Test Case 5: Single node tree 🌱
    bst5 = BinarySearchTree()
    bst5.insert(42)
    
    # Your implementation of balance_bst should go here 🛠️
    # balanced1 = balance_bst(bst1)
    # balanced2 = balance_bst(bst2)
    # ... and so on
    for i, bst in enumerate([bst1, bst2, bst3, bst4, bst5], start=1):
        balanced = balance_bst(bst)           # Balancea el árbol
        inorder_vals = [node.val for node in balanced.inorder()]  # Extrae valores
        print(f"Balanced BST {i} Inorder: {inorder_vals}")        # Imprime el resultado
if __name__ == "__main__":
    test_balance_bst()
