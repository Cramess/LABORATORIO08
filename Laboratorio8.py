#Challenge 3: Lowest Common Ancestor

def lowest_common_ancestor(node, p, q):
    if not node:
        return None
    if node.value == p or node.value == q:
        return node                     # Si encontramos uno de los nodos, lo devolvemos
    left = lowest_common_ancestor(node.left, p, q)
    right = lowest_common_ancestor(node.right, p, q)
    if left and right:
        return node                     # Si uno está a la izquierda y otro a la derecha
    return left if left else right      # Retornamos el que no sea None

#Challenge 4: Vertical Order Traversal


from collections import defaultdict, deque
def vertical_order_traversal(root):
    if not root:
        return []
    column_table = defaultdict(list)
    queue = deque([(root, 0)])          # (nodo, posición horizontal)
    while queue:
        node, col = queue.popleft()
        if node:
            column_table[col].append(node.value)
            queue.append((node.left, col - 1))   # Izquierda: columna -1
            queue.append((node.right, col + 1))  # Derecha: columna +1
    return [column_table[x] for x in sorted(column_table)]



#Challenge 5: Tree Pruning

def prune_tree(node, target):
    if not node:
        return None
    node.left = prune_tree(node.left, target)    # Procesamos izquierda
    node.right = prune_tree(node.right, target)  # Procesamos derecha
    if node.value != target and not node.left and not node.right:
        return None                               # Si no es target y no tiene hijos, lo eliminamos
    return node



class ExpressionNode:
    def _init_(self, value):
        self.value = value     # Valor del nodo (puede ser número u operador)
        self.left = None       # Hijo izquierdo (operando izquierdo)
        self.right = None      # Hijo derecho (operando derecho)

def build_expression_tree(postfix):
    stack = []                            # Usamos una pila para construir el árbol
    for token in postfix:                 # Recorremos cada símbolo de la expresión
        node = ExpressionNode(token)      # Creamos un nuevo nodo con el token actual
        if token in "+-*/":               # Si el token es un operador
            node.right = stack.pop()      # Extraemos el último valor como hijo derecho
            node.left = stack.pop()       # Extraemos el anterior como hijo izquierdo
        # Si es número, se queda sin hijos
        stack.append(node)                # Añadimos el nodo al stack
    return stack[-1] if stack else None   # El último nodo en la pila es la raíz del árbol

def evaluate_expression(node):
    if not node.left and not node.right:
        return float(node.value)          # Si es hoja (número), lo convertimos a float

    # Evaluamos recursivamente los hijos izquierdo y derecho
    left_val = evaluate_expression(node.left)
    right_val = evaluate_expression(node.right)

    # Realizamos la operación correspondiente según el operador
    if node.value == '+':
        return left_val + right_val       # Suma
    elif node.value == '-':
        return left_val - right_val       # Resta
    elif node.value == '*':
        return left_val * right_val       # Multiplicación
    elif node.value == '/':
        return left_val / right_val       # División

