graph = {'A': set(['B', 'C']),
         'B': set(['A', 'C', 'D', 'E']),
         'C': set(['A', 'B', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set()}

def dfs(graph, start, end):
    seen = set()

    def dfs_r(v, path):
        seen.add(v)
        if v == end:
            return path
        for w in graph[v]:
            if w not in seen:
                pt = dfs_r(w, path + [w])
                if pt:
                    return pt
        return []

    return dfs_r(start, [start])

def dfs_iterative(graph, start, end):
    seen = set()
    stack = [(start, [start])]

    while len(stack) > 0:
        v, path = stack.pop()
        seen.add(v) 
        if v == end:
            return path

        for w in graph[v]:
            if w not in seen:
                stack.append((w, path + [w]))
    return []

if __name__ == '__main__':
    assert dfs(graph, 'A', 'D') in [['A', 'C', 'F', 'E', 'B', 'D'],
                                    ['A', 'B', 'D'],
                                    ['A', 'C', 'B', 'D']]
    assert dfs(graph, 'A', 'G') == []

    assert dfs_iterative(graph, 'A', 'D') in [['A', 'C', 'F', 'E', 'B', 'D'],
                                              ['A', 'B', 'D'],
                                              ['A', 'C', 'B', 'D']]
    assert dfs_iterative(graph, 'A', 'G') == []

    print 'path rec: ', dfs(graph, 'A', 'D')
    #print 'path: ', dfs(graph, 'A', 'X')
    print 'path iter: ', dfs_iterative(graph, 'A', 'D')
