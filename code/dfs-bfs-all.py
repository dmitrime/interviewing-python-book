graph = {'A': set(['B', 'C']),
         'B': set(['A', 'C', 'D', 'E']),
         'C': set(['A', 'B', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set()}


def dfs_all(graph, start, end):
    paths = []

    def dfs_r(v, path):
        if v == end:
            paths.append(path)
        else:
            # skip the neighbours already in the path
            for w in graph[v] - set(path):
                dfs_r(w, path + [w])

    dfs_r(start, [start])
    return paths

def bfs_all(g, start, end):
    q = [(start, [start])]
    paths = []

    while len(q) > 0:
        v, pt = q.pop(0)
        if v == end:
            paths.append(pt)
        else:
            for u in g[v] - set(pt):
                q.append((u, pt + [u]))
    return paths


if __name__ == '__main__':
    print 'DFS all paths: ', dfs_all(graph, 'A', 'F')
    assert len(dfs_all(graph, 'A', 'F')) == 4
    assert len(dfs_all(graph, 'A', 'G')) == 0

    print 'BFS all paths: ', dfs_all(graph, 'A', 'F')
    assert len(bfs_all(graph, 'A', 'F')) == 4
    assert len(bfs_all(graph, 'A', 'G')) == 0
