from collections import deque

print("==================================================")
print("     ASSESSMENT 3.3: DATA STRUCTURE TRAVERSALS      ")
print("               APELYIDO: ROSALITA                 ")
print("==================================================")

# ==========================================
# 1. LINEAR DATA STRUCTURE (Array Traversal)
# ==========================================
linear_data = ["151", "84", "71", "95", "62", "49", "32", "15", "2", "101"]

print("\n--- LINEAR DATA STRUCTURE ---")
print("Original Array:", linear_data)

# Left to Right Traversal
left_to_right = []
for item in linear_data:
    left_to_right.append(item)
print("Traversal (Left to Right):", " -> ".join(left_to_right))

# Right to Left Traversal
right_to_left = []
for item in reversed(linear_data):
    right_to_left.append(item)
print("Traversal (Right to Left):", " -> ".join(right_to_left))


# ==========================================
# 2. NON-LINEAR: BINARY TREE (ROSALITA)
# ==========================================
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Pagbuo ng Binary Tree mula sa mga titik ng ROSALITA
root = TreeNode("R")
root.left = TreeNode("O")
root.right = TreeNode("S")
root.left.left = TreeNode("A")
root.left.right = TreeNode("L")
root.right.left = TreeNode("I")
root.right.right = TreeNode("T")
root.left.left.left = TreeNode("A")

# Binary Tree BFS (Breadth-First Search)
def bfs_tree(node):
    if not node:
        return []
    queue = deque([node])
    result = []
    while queue:
        curr = queue.popleft()
        result.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return result

# Binary Tree DFS (Depth-First Search - Pre-order)
def dfs_tree(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        dfs_tree(node.left, result)
        dfs_tree(node.right, result)
    return result

print("\n--- NON-LINEAR: BINARY TREE ---")
print("Binary Tree BFS (Level-Order):", " -> ".join(bfs_tree(root)))
print("Binary Tree DFS (Pre-Order):", " -> ".join(dfs_tree(root)))


# ==========================================
# 3. NON-LINEAR: GRAPH (ROSALITA)
# ==========================================
graph = {
    "R": ["O", "S"],
    "O": ["R", "A", "L"],
    "S": ["R", "I", "T"],
    "A": ["O", "L"],
    "L": ["O", "A"],
    "I": ["S", "T"],
    "T": ["S", "I"]
}

# Graph BFS
def bfs_graph(graph_map, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    while queue:
        curr = queue.popleft()
        result.append(curr)
        for neighbor in graph_map.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

# Graph DFS
def dfs_graph(graph_map, curr, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    visited.add(curr)
    result.append(curr)
    for neighbor in graph_map.get(curr, []):
        if neighbor not in visited:
            dfs_graph(graph_map, neighbor, visited, result)
    return result

print("\n--- NON-LINEAR: GRAPH ---")
print("Graph BFS:", " -> ".join(bfs_graph(graph, "R")))
print("Graph DFS:", " -> ".join(dfs_graph(graph, "R")))
print("==================================================")
