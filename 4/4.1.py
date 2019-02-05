# -----------------------------------------------------------------------------|
def main():
    """

    """

    # Parse input
    n = int(input())
    destination = int(input())

    graph = [[] for _ in range(n)]

    for i in range(n):
        graph[i] = [int(x) for x in input().split() if x != 'None']

    # print(bfs(destination, graph))
    # print(dfs(destination, graph))
    print(dfs_iterative(destination, graph))
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def dfs_iterative(destination: int, graph: list) -> bool:
    """

    """

    stack = [0]
    visited = [False for _ in range(len(graph))]
    visited[0] = True

    while stack:
        current = stack.pop()
        if current == destination:
            return True

        for neighbour in graph[current]:
            if not visited[neighbour]:
                visited[neighbour] = True
                stack.append(neighbour)

    return False
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def dfs(destination: int, graph: list) -> bool:
    """

    """

    visited = [False for _ in range(len(graph))]
    visited[0] = True

    return _dfs(destination, graph, visited, 0)
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def _dfs(destination: int, graph: list, visited: list, current: int) -> bool:
    """

    """
    if current == destination:
        return True

    for neighbour in graph[current]:
        if not visited[neighbour]:
            visited[neighbour] = True
            if _dfs(destination, graph, visited, neighbour):
                return True
# -----------------------------------------------------------------------------|


# -----------------------------------------------------------------------------|
def bfs(destination: int, graph: list) -> bool:
    """

    """

    queue = [0]
    visited = [False for _ in range(len(graph))]
    visited[0] = True

    while queue:
        current = queue.pop(0)
        if current == destination:
            return True

        for neighbour in graph[current]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

    return False
# -----------------------------------------------------------------------------|


if __name__ == '__main__':
    main()
