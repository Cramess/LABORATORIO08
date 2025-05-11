#Challenge 2: Tree Serialization

from collections import deque 
# Definición de un nodo del árbol binario
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho
class BinaryTree:
    def __init__(self):
        self.root = None  # Raíz del árbol
    def build_tree_from_list(self, values):
        if not values or values[0] is None:
            return  # Árbol vacío
        self.root = TreeNode(values[0])  # Crear la raíz
        queue = deque([self.root])  # Cola para mantener nodos a procesar
        i = 1  # Índice de lista de valores
        # Recorremos la lista y asignamos hijos a cada nodo
        while queue and i < len(values):
            node = queue.popleft()  # Tomar el nodo actual
            # Procesar hijo izquierdo
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            # Procesar hijo derecho
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
# Serializa un árbol binario a una cadena de texto
def serialize(root):
    if not root:
        return ""  # Árbol vacío
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))  # Guardamos el valor del nodo
            queue.append(node.left)      # Añadir hijo izquierdo a la cola
            queue.append(node.right)     # Añadir hijo derecho a la cola
        else:
            result.append("#")  # Marcador para nodos nulos
    return ",".join(result)  # Unimos todos los valores en una cadena

# Deserializa una cadena a un árbol binario
def deserialize(data):
    if not data:
        return None  # Cadena vacía = árbol vacío

    nodes = data.split(",")  # Separamos la cadena en valores
    root = TreeNode(int(nodes[0]))  # Crear raíz
    queue = deque([root])  # Cola para construir los hijos
    i = 1  # Índice en la lista de nodos

    while queue:
        node = queue.popleft()

        # Reconstruir hijo izquierdo si no es nulo
        if nodes[i] != "#":
            node.left = TreeNode(int(nodes[i]))
            queue.append(node.left)
        i += 1

        # Reconstruir hijo derecho si no es nulo
        if i < len(nodes) and nodes[i] != "#":
            node.right = TreeNode(int(nodes[i]))
            queue.append(node.right)
        i += 1

    return root  # Devolvemos la raíz del árbol reconstruido

# Pruebas para verificar que serializar y deserializar funciona correctamente
def test_serialize_deserialize():
    """Test the serialize and deserialize functions. 💾"""
    # Test Case 1: Normal binary tree 🌳
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    
    # Test Case 2: Empty tree 🈳
    tree2 = BinaryTree()
    
    # Test Case 3: Single node tree 🌱
    tree3 = BinaryTree()
    tree3.build_tree_from_list([42])
    
    # Test Case 4: Left-skewed tree 📐⬅️
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, None, 3, None, None, None, 4])
    
    # Test Case 5: Right-skewed tree 📐➡️
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4])
    
    # Your implementation of serialize and deserialize should go here 🛠️
    # serialized1 = serialize(tree1.root)
    # deserialized1 = deserialize(serialized1)
    # ... and so on


    for i, tree in enumerate([tree1, tree2, tree3, tree4, tree5], start=1):
        serialized = serialize(tree.root)  # Convertir árbol a texto
        deserialized = deserialize(serialized)  # Reconstruir árbol
        re_serialized = serialize(deserialized)  # Volver a serializar para comparar
        print(f"Tree {i} Serialized: {serialized}")
        print(f"Tree {i} Re-Serialized After Deserialization: {re_serialized}")
        assert serialized == re_serialized  # Asegura que el árbol es igual tras ida y vuelta

# Ejecutar pruebas solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    test_serialize_deserialize()
