import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, update=False, step_delay=1):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap(array):
    n = len(array)
    nodes = [Node(array[i]) for i in range(n)]

    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]

    return nodes[0] if nodes else None


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def generate_shades(num_shades):
    base_color = (18, 150, 240)  # #1296F0 in RGB
    step = 255 // max(num_shades, 1)
    shades = [(min(base_color[0] + i * step, 255), 
               min(base_color[1] + i * step, 255), 
               min(base_color[2] + i * step, 255)) for i in range(num_shades)]
    return [rgb_to_hex(shade) for shade in shades]

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def depth_first_traversal(root):
    if root is None:
        return

    stack = [root]
    total_nodes = count_nodes(root)
    shades = generate_shades(total_nodes)

    index = 0
    while stack:
        node = stack.pop()
        node.color = shades[index]
        index += 1
        draw_tree(root, update=True)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def breadth_first_traversal(root):
    if root is None:
        return

    queue = deque([root])
    total_nodes = count_nodes(root)
    shades = generate_shades(total_nodes)

    index = 0
    while queue:
        node = queue.popleft()
        node.color = shades[index]
        index += 1
        draw_tree(root, update=True)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

heap_array = [10, 20, 15, 30, 40, 50, 100]
root = build_heap(heap_array)
draw_tree(root)

print("DFT:")
depth_first_traversal(root)

# Reset the tree colors
root = build_heap(heap_array)

print("BFT:")
breadth_first_traversal(root)
