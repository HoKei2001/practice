"""
DFS (Depth-First Search) Templates and Examples
DFS 使用栈(stack)或递归实现，适用于路径搜索、回溯、组合等场景
"""

from typing import List, Optional, Set
import sys
import os
# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from data_structures.graph import TreeNode, Graph


# ========== Template 1: Recursive DFS for Tree ==========
def dfs_tree_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Recursive DFS template for tree traversal (preorder)
    Time: O(n), Space: O(h) where h is height of tree
    
    使用场景:
    - Tree traversal (preorder, inorder, postorder)
    - Path sum problems
    - Tree diameter/height
    """
    result = []
    
    def dfs(node: Optional[TreeNode]):
        if not node:
            return
        
        result.append(node.val)  # Preorder: process before children
        dfs(node.left)           # Traverse left subtree
        # result.append(node.val)  # Inorder: process between children
        dfs(node.right)          # Traverse right subtree
        # result.append(node.val)  # Postorder: process after children
    
    dfs(root)
    return result


# ========== Template 2: Iterative DFS for Tree (using stack) ==========
def dfs_tree_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Iterative DFS template using explicit stack
    Time: O(n), Space: O(h)
    
    使用场景:
    - When recursion depth might be too large
    - Need more control over traversal
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Add right first so left is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


# ========== Template 3: DFS for Graph with Visited Set ==========
def dfs_graph_recursive(graph: Graph, start: int) -> List[int]:
    """
    Recursive DFS template for graph traversal
    Time: O(V + E), Space: O(V)
    
    使用场景:
    - Graph traversal
    - Detect cycles
    - Topological sort
    """
    visited = set()
    result = []
    
    def dfs(vertex: int):
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs(neighbor)
    
    dfs(start)
    return result


# ========== Template 4: DFS Path Finding ==========
def dfs_find_path(root: Optional[TreeNode], target: int) -> List[int]:
    """
    DFS template for finding path to target in tree
    Time: O(n), Space: O(h)
    
    使用场景:
    - Find path to specific node
    - Root to leaf paths
    - Path sum problems
    """
    def dfs(node: Optional[TreeNode], path: List[int]) -> bool:
        if not node:
            return False
        
        path.append(node.val)
        
        if node.val == target:
            return True
        
        if dfs(node.left, path) or dfs(node.right, path):
            return True
        
        path.pop()  # Backtrack
        return False
    
    result = []
    dfs(root, result)
    return result


# ========== Template 5: DFS with Backtracking (Grid) ==========
def dfs_grid_backtrack(grid: List[List[int]], start: tuple, target: tuple) -> List[tuple]:
    """
    DFS template for grid traversal with backtracking
    Time: O(4^(m*n)) worst case, Space: O(m*n)
    
    使用场景:
    - Maze solving
    - Word search in grid
    - Island problems
    """
    if not grid or not grid[0]:
        return []
    
    m, n = len(grid), len(grid[0])
    path = []
    visited = set()
    
    def dfs(row: int, col: int) -> bool:
        # Base cases
        if (row, col) == target:
            path.append((row, col))
            return True
        
        if (row < 0 or row >= m or col < 0 or col >= n or
            grid[row][col] == 1 or (row, col) in visited):
            return False
        
        # Mark as visited and add to path
        visited.add((row, col))
        path.append((row, col))
        
        # Explore 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            if dfs(row + dr, col + dc):
                return True
        
        # Backtrack
        path.pop()
        # Note: keeping visited to avoid revisiting in same path
        return False
    
    dfs(start[0], start[1])
    return path


# ========== Template 6: DFS for All Paths ==========
def dfs_all_paths(root: Optional[TreeNode]) -> List[List[int]]:
    """
    DFS template for finding all root-to-leaf paths
    Time: O(n*h), Space: O(h) for recursion
    
    使用场景:
    - All root-to-leaf paths
    - Path sum variants
    - Binary tree paths
    """
    if not root:
        return []
    
    result = []
    
    def dfs(node: Optional[TreeNode], path: List[int]):
        if not node:
            return
        
        path.append(node.val)
        
        # Leaf node - save current path
        if not node.left and not node.right:
            result.append(path[:])  # Make a copy
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        
        path.pop()  # Backtrack
    
    dfs(root, [])
    return result


# ========== Template 7: DFS for Combinations/Permutations ==========
def dfs_combinations(nums: List[int], k: int) -> List[List[int]]:
    """
    DFS template for generating combinations
    Time: O(C(n,k)), Space: O(k)
    
    使用场景:
    - Subsets
    - Combinations
    - Letter combinations
    """
    result = []
    
    def dfs(start: int, path: List[int]):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)  # i+1 to avoid duplicates
            path.pop()  # Backtrack
    
    dfs(0, [])
    return result


def dfs_permutations(nums: List[int]) -> List[List[int]]:
    """
    DFS template for generating permutations
    Time: O(n!), Space: O(n)
    
    使用场景:
    - Permutations
    - N-Queens
    - Sudoku solver
    """
    result = []
    
    def dfs(path: List[int], remaining: Set[int]):
        if not remaining:
            result.append(path[:])
            return
        
        for num in list(remaining):
            path.append(num)
            remaining.remove(num)
            dfs(path, remaining)
            remaining.add(num)  # Backtrack
            path.pop()
    
    dfs([], set(nums))
    return result


# ========== Template 8: DFS with Memoization ==========
def dfs_with_memo(grid: List[List[int]]) -> int:
    """
    DFS template with memoization for optimization
    Time: O(m*n), Space: O(m*n)
    
    使用场景:
    - Longest increasing path
    - Unique paths with obstacles
    - Dynamic programming on trees/graphs
    """
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    memo = {}
    
    def dfs(row: int, col: int) -> int:
        # Check memo
        if (row, col) in memo:
            return memo[(row, col)]
        
        # Base case
        if row < 0 or row >= m or col < 0 or col >= n:
            return 0
        
        # Calculate result
        result = 1  # Current cell
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < m and 0 <= new_col < n and 
                grid[new_row][new_col] > grid[row][col]):
                result = max(result, 1 + dfs(new_row, new_col))
        
        # Save to memo
        memo[(row, col)] = result
        return result
    
    max_path = 0
    for i in range(m):
        for j in range(n):
            max_path = max(max_path, dfs(i, j))
    
    return max_path


# ========== Example Usage ==========
def example_usage():
    """Demonstrate how to use DFS templates"""
    
    # Example 1: Tree DFS
    print("=" * 50)
    print("Example 1: Tree DFS")
    tree = TreeNode.from_list([1, 2, 3, 4, 5, None, 6])
    print(f"Recursive DFS: {dfs_tree_recursive(tree)}")
    print(f"Iterative DFS: {dfs_tree_iterative(tree)}")
    print(f"All paths: {dfs_all_paths(tree)}")
    print(f"Path to 5: {dfs_find_path(tree, 5)}")
    
    # Example 2: Graph DFS
    print("\n" + "=" * 50)
    print("Example 2: Graph DFS")
    graph = Graph()
    graph.add_edges([[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]])
    print(f"Graph DFS from 0: {dfs_graph_recursive(graph, 0)}")
    
    # Example 3: Grid DFS with backtracking
    print("\n" + "=" * 50)
    print("Example 3: Grid DFS (find path)")
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    path = dfs_grid_backtrack(grid, (0, 0), (2, 2))
    print(f"Path from (0,0) to (2,2): {path}")
    
    # Example 4: Combinations and Permutations
    print("\n" + "=" * 50)
    print("Example 4: Combinations and Permutations")
    nums = [1, 2, 3]
    print(f"Combinations of size 2: {dfs_combinations(nums, 2)}")
    print(f"All permutations: {dfs_permutations(nums)}")
    
    # Example 5: DFS with memoization
    print("\n" + "=" * 50)
    print("Example 5: DFS with Memoization")
    grid_memo = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    print(f"Longest increasing path: {dfs_with_memo(grid_memo)}")


if __name__ == "__main__":
    example_usage()