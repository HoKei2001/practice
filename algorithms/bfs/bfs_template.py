"""
BFS (Breadth-First Search) Templates and Examples
BFS 使用队列(queue)实现，适用于寻找最短路径、层级遍历等场景
"""

from collections import deque
from typing import List, Optional, Set, Dict
import sys
import os
# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from data_structures.graph import TreeNode, Graph


# ========== Template 1: Basic BFS for Tree ==========
def bfs_tree_template(root: Optional[TreeNode]) -> List[int]:
    """
    Basic BFS template for binary tree traversal
    Time: O(n), Space: O(w) where w is max width of tree
    
    使用场景:
    - Level order traversal (层序遍历)
    - Find minimum depth (最小深度)
    - Find nodes at specific level
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)  # Process current node
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


# ========== Template 2: Level-by-Level BFS ==========
def bfs_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    BFS template for processing nodes level by level
    Time: O(n), Space: O(w)
    
    使用场景:
    - Level order traversal with level information
    - Zigzag level order
    - Find rightmost node at each level
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # Number of nodes at current level
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_nodes)
    
    return result


# ========== Template 3: BFS for Graph (with visited set) ==========
def bfs_graph_template(graph: Graph, start: int) -> List[int]:
    """
    BFS template for graph traversal
    Time: O(V + E), Space: O(V)
    
    使用场景:
    - Graph traversal
    - Connected components
    - Shortest path in unweighted graph
    """
    visited = set()
    result = []
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)  # Process current vertex
        
        # Visit all unvisited neighbors
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


# ========== Template 4: Shortest Path BFS ==========
def bfs_shortest_path(graph: Graph, start: int, target: int) -> int:
    """
    BFS template for finding shortest path in unweighted graph
    Time: O(V + E), Space: O(V)
    
    使用场景:
    - Shortest path in unweighted graph
    - Minimum steps problems
    - Word ladder problems
    """
    if start == target:
        return 0
    
    visited = set([start])
    queue = deque([(start, 0)])  # (node, distance)
    
    while queue:
        vertex, dist = queue.popleft()
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor == target:
                return dist + 1
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    
    return -1  # No path found


# ========== Template 5: Multi-Source BFS ==========
def bfs_multi_source(grid: List[List[int]], sources: List[tuple]) -> List[List[int]]:
    """
    BFS template starting from multiple sources simultaneously
    Time: O(m*n), Space: O(m*n) for m×n grid
    
    使用场景:
    - Rotting oranges problem
    - Distance to nearest 0
    - Multiple starting points
    """
    if not grid or not grid[0]:
        return []
    
    m, n = len(grid), len(grid[0])
    distances = [[-1] * n for _ in range(m)]
    queue = deque()
    
    # Initialize queue with all sources
    for r, c in sources:
        queue.append((r, c, 0))
        distances[r][c] = 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        row, col, dist = queue.popleft()
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check bounds and if not visited
            if (0 <= new_row < m and 0 <= new_col < n and 
                distances[new_row][new_col] == -1):
                distances[new_row][new_col] = dist + 1
                queue.append((new_row, new_col, dist + 1))
    
    return distances


# ========== Template 6: Bidirectional BFS ==========
def bfs_bidirectional(graph: Graph, start: int, target: int) -> int:
    """
    Bidirectional BFS for finding shortest path more efficiently
    Time: O(b^(d/2)), Space: O(b^(d/2)) where b is branching factor, d is depth
    
    使用场景:
    - Word ladder with large search space
    - Finding shortest transformation sequence
    """
    if start == target:
        return 0
    
    # Two frontiers growing from both ends
    front_start = {start}
    front_target = {target}
    visited = {start, target}
    distance = 0
    
    while front_start and front_target:
        distance += 1
        
        # Always expand the smaller frontier for efficiency
        if len(front_start) > len(front_target):
            front_start, front_target = front_target, front_start
        
        next_front = set()
        for vertex in front_start:
            for neighbor in graph.get_neighbors(vertex):
                if neighbor in front_target:
                    return distance
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_front.add(neighbor)
        
        front_start = next_front
    
    return -1  # No path found


# ========== Example Usage ==========
def example_usage():
    """Demonstrate how to use BFS templates"""
    
    # Example 1: Tree BFS
    print("=" * 50)
    print("Example 1: Tree BFS")
    tree = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
    print(f"Tree traversal: {bfs_tree_template(tree)}")
    print(f"Level order: {bfs_level_order(tree)}")
    
    # Example 2: Graph BFS
    print("\n" + "=" * 50)
    print("Example 2: Graph BFS")
    graph = Graph()
    graph.add_edges([[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]])
    print(f"Graph traversal from 0: {bfs_graph_template(graph, 0)}")
    print(f"Shortest path from 0 to 4: {bfs_shortest_path(graph, 0, 4)}")
    
    # Example 3: Multi-source BFS (grid)
    print("\n" + "=" * 50)
    print("Example 3: Multi-source BFS")
    grid = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    sources = [(1, 1)]  # Starting from center
    distances = bfs_multi_source(grid, sources)
    print("Distance from source (1,1):")
    for row in distances:
        print(row)


if __name__ == "__main__":
    example_usage()