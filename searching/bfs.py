from collections import deque


def breath_first_search(graph,root):
    visited = []
    que = deque([root])
    visited.append(root)
 
    while que:
        print(f"visited={visited},que={que}")
        node = que.popleft()
        for neighbours in graph[node]:
            if neighbours not in visited:
                que.append(neighbours)
                visited.append(neighbours)
            print(f"visited:{visited},que:{que}")
    print(visited)

breath_first_search({0: [1, 2], 1: [2], 2: [3], 3: [1, 2]},0)