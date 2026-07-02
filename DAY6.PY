#TREES AND BINARY TREES
#MAXIMUM DEPTH OF BINARY TREE
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


leaf_15 = TreeNode(15)
leaf_7 = TreeNode(7)
node_20 = TreeNode(20, leaf_15, leaf_7)
node_9 = TreeNode(9)
tree_root = TreeNode(3, node_9, node_20)


output = Solution().maxDepth(tree_root)



#Invert the binary tree
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  
            return root
        self.invertTree(root.left)  
        self.invertTree(root.right) 
        
        # Swap the nodes
        root.left, root.right = root.right, root.left 
        return root 
def print_tree(root: Optional[TreeNode]) -> str:
    if not root:
        return "[]"
    result: List[str] = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current:
            result.append(str(current.val))
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append("null")
    
    while result and result[-1] == "null":
        result.pop()
    return "[" + ",".join(result) + "]"



if __name__ == "__main__":
    
    input_root = TreeNode(4)
    input_root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    input_root.right = TreeNode(7, TreeNode(6), TreeNode(9))

    print("--- Before Inversion ---")
    print(f"Tree Array Format: {print_tree(input_root)}")
    
    # Run the Solution
    sol = Solution()
    output_root = sol.invertTree(input_root)

    print("\n--- After Inversion ---")
    print(f"Tree Array Format: {print_tree(output_root)}")
