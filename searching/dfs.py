def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        visited.append(node)
        for neighbours in graph[node]:
            if neighbours not in visited and neighbours not in stack:
                stack.append(neighbours)
        print(f"visited:{visited},stack:{stack}")
    print(visited)

dfs({0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [2, 3]}, 0)