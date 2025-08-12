"""
BFS Practice Problems with Solutions
These are common LeetCode problems that use BFS
"""

from collections import deque
from typing import List, Optional
import sys
import os
# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_structures.graph import TreeNode, create_binary_tree


class BFSProblems:
    """Collection of BFS practice problems"""
    
    # ========== Problem 1: Binary Tree Level Order Traversal ==========
    # LeetCode 102: https://leetcode.com/problems/binary-tree-level-order-traversal/
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, return the level order traversal 
        of its nodes' values (i.e., from left to right, level by level).
        
        Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]
        
        Time: O(n), Space: O(n)
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result
    
    # ========== Problem 2: Minimum Depth of Binary Tree ==========
    # LeetCode 111: https://leetcode.com/problems/minimum-depth-of-binary-tree/
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given a binary tree, find its minimum depth.
        The minimum depth is the number of nodes along the shortest path 
        from the root node down to the nearest leaf node.
        
        Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: 2
        
        Time: O(n), Space: O(n)
        """
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # First leaf node we encounter has minimum depth
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0
    
    # ========== Problem 3: Rotting Oranges ==========
    # LeetCode 994: https://leetcode.com/problems/rotting-oranges/
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        You are given an m x n grid where:
        - 0 represents an empty cell
        - 1 represents a fresh orange
        - 2 represents a rotten orange
        
        Every minute, fresh oranges adjacent to rotten oranges become rotten.
        Return the minimum number of minutes until no cell has a fresh orange.
        If impossible, return -1.
        
        Example:
        Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4
        
        Time: O(m*n), Space: O(m*n)
        """
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Find all rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_time = 0
        
        while queue:
            row, col, time = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < m and 0 <= new_col < n and 
                    grid[new_row][new_col] == 1):
                    grid[new_row][new_col] = 2
                    fresh_count -= 1
                    max_time = max(max_time, time + 1)
                    queue.append((new_row, new_col, time + 1))
        
        return max_time if fresh_count == 0 else -1
    
    # ========== Problem 4: Word Ladder ==========
    # LeetCode 127: https://leetcode.com/problems/word-ladder/
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Given two words beginWord and endWord, and a dictionary wordList,
        return the shortest transformation sequence length from beginWord to endWord.
        
        Example:
        Input: beginWord = "hit", endWord = "cog", 
               wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5
        Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog"
        
        Time: O(M²×N), Space: O(M²×N) where M is word length, N is number of words
        """
        if endWord not in wordList:
            return 0
        
        # Build adjacency list with generic states
        from collections import defaultdict
        neighbors = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)
        
        # BFS
        visited = set([beginWord])
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, level = queue.popleft()
            
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                
                for neighbor in neighbors[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        
        return 0
    
    # ========== Problem 5: 01 Matrix ==========
    # LeetCode 542: https://leetcode.com/problems/01-matrix/
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Given an m x n binary matrix mat, return the distance of the nearest 0 
        for each cell. The distance between two adjacent cells is 1.
        
        Example:
        Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
        Output: [[0,0,0],[0,1,0],[1,2,1]]
        
        Time: O(m*n), Space: O(m*n)
        """
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        distances = [[float('inf')] * n for _ in range(m)]
        queue = deque()
        
        # Start BFS from all 0s
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distances[i][j] = 0
                    queue.append((i, j))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            row, col = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < m and 0 <= new_col < n and 
                    distances[new_row][new_col] > distances[row][col] + 1):
                    distances[new_row][new_col] = distances[row][col] + 1
                    queue.append((new_row, new_col))
        
        return distances
    
    # ========== Problem 6: Open the Lock ==========
    # LeetCode 752: https://leetcode.com/problems/open-the-lock/
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        You have a lock with 4 circular wheels, each with digits '0'-'9'.
        Starting from "0000", return minimum turns to reach target, avoiding deadends.
        Return -1 if impossible.
        
        Example:
        Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
        Output: 6
        
        Time: O(10^4), Space: O(10^4)
        """
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if "0000" == target:
            return 0
        
        def get_neighbors(code: str) -> List[str]:
            neighbors = []
            for i in range(4):
                digit = int(code[i])
                # Turn up
                up = code[:i] + str((digit + 1) % 10) + code[i+1:]
                neighbors.append(up)
                # Turn down
                down = code[:i] + str((digit - 1) % 10) + code[i+1:]
                neighbors.append(down)
            return neighbors
        
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        while queue:
            code, steps = queue.popleft()
            
            for neighbor in get_neighbors(code):
                if neighbor == target:
                    return steps + 1
                
                if neighbor not in dead and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return -1


def test_bfs_problems():
    """Test BFS problems with examples"""
    problems = BFSProblems()
    
    print("=" * 60)
    print("Testing BFS Problems")
    print("=" * 60)
    
    # Test 1: Level Order Traversal
    print("\n1. Binary Tree Level Order Traversal")
    tree = create_binary_tree([3, 9, 20, None, None, 15, 7])
    result = problems.levelOrder(tree)
    print(f"   Input: [3,9,20,null,null,15,7]")
    print(f"   Output: {result}")
    print(f"   Expected: [[3], [9, 20], [15, 7]]")
    
    # Test 2: Minimum Depth
    print("\n2. Minimum Depth of Binary Tree")
    tree = create_binary_tree([3, 9, 20, None, None, 15, 7])
    result = problems.minDepth(tree)
    print(f"   Input: [3,9,20,null,null,15,7]")
    print(f"   Output: {result}")
    print(f"   Expected: 2")
    
    # Test 3: Rotting Oranges
    print("\n3. Rotting Oranges")
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    result = problems.orangesRotting(grid)
    print(f"   Input: {[[2, 1, 1], [1, 1, 0], [0, 1, 1]]}")
    print(f"   Output: {result}")
    print(f"   Expected: 4")
    
    # Test 4: Word Ladder
    print("\n4. Word Ladder")
    result = problems.ladderLength("hit", "cog", 
                                  ["hot", "dot", "dog", "lot", "log", "cog"])
    print(f"   Begin: 'hit', End: 'cog'")
    print(f"   Output: {result}")
    print(f"   Expected: 5")
    
    # Test 5: 01 Matrix
    print("\n5. 01 Matrix")
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    result = problems.updateMatrix(mat)
    print(f"   Input: {[[0, 0, 0], [0, 1, 0], [1, 1, 1]]}")
    print(f"   Output: {result}")
    print(f"   Expected: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]")
    
    # Test 6: Open the Lock
    print("\n6. Open the Lock")
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    result = problems.openLock(deadends, "0202")
    print(f"   Target: '0202'")
    print(f"   Output: {result}")
    print(f"   Expected: 6")


if __name__ == "__main__":
    test_bfs_problems()