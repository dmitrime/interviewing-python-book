graph = {'A': set(['B', 'C']),
         'B': set(['A', 'C', 'D', 'E']),
         'C': set(['A', 'B', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set()}

def bfs(graph, start, end):
    q = [(start, [start])]
    seen = set([start])
    while len(q) > 0:
        x, path = q.pop(0) # take from the front
        for el in graph[x]:
            if el == end:
                return path + [el]
            if el not in seen:
                q.append((el, path + [el]))
                seen.add(el)
    return []

if __name__ == '__main__':
    print 'shortest path: ', bfs(graph, 'A', 'D')
    
    assert bfs(graph, 'A', 'D') == ['A', 'B', 'D']
    assert bfs(graph, 'A', 'G') == []
