# Tree techniques

- Trees are commonly used to represent hierarchical data, e.g. file systems, JSON, and HTML documents.
- Tries which is an advanced tree used for efficiently storing and searching strings.
- You should be very familiar with writing pre-order, in-order, and post-order traversal recursively.

## Corner cases
1. Empty tree
2. Single node
3. Two nodes
4. Very skewed tree (like a linked list)

## Common routines
Be familiar with the following routines because many tree questions make use of one or more of these routines in the solution:

1. Insert value
2. Delete value
3. Count number of nodes in tree
4. Whether a value is in the tree
5. Calculate height of the tree
6. Binary search tree
    - Determine if it is a binary search tree
    - Get maximum value
    - Get minimum value

## Techniques
### Use recursion
- Recursion is the most common approach for traversing trees. When you notice that the subtree problem can be used to solve the entire problem, try using recursion.
- When using recursion, always remember to check for the base case, usually where the node is null.
- Sometimes it is possible that your recursive function needs to return two values.
### Traversing by level
- When you are asked to traverse a tree by level, use breadth-first search.
### Summation of nodes
- If the question involves summation of nodes along the way, be sure to check whether nodes can be negative.
