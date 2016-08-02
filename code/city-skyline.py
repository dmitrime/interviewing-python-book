from collections import defaultdict
import bisect

# ~150ms
def skyline(buildings):
    # dict of events grouped by x-position
    events = defaultdict(list)
    for x1, x2, height in buildings:
        events[x1].append((height, True))  # start event
        events[x2].append((height, False)) # end event

    # priority queue and result-list
    pq, points = [], []
    # scan sorted events left to right
    for pos, levents in sorted(events.items()):
        for (height, start) in levents:
            if start:
                # for start event, insert into priority queue
                bisect.insort(pq, height)
            else:
                # for end event, remove height
                pq.pop(bisect.bisect_left(pq, height))

        # make sure last point is not same height
        max_height = pq[-1] if len(pq) > 0 else 0
        if len(points) == 0 or points[-1][1] != max_height:
            points.append((pos, max_height))

    return points

# ~160ms
#def skyline(buildings):
        #events = [] #defaultdict(list)
        #for x1, x2, h in buildings:
            #events.append((x1, h, True))
            #events.append((x2, h, False))
        #events = sorted(events)

        #pq, points = [], []
        #i = 0
        #while i < len(events):
            #pos, j = events[i][0], i
            #while j < len(events) and events[j][0] == pos:
                #_, height, start = events[j]
                #if start:
                    #bisect.insort(pq, height)
                #else:
                    #pq.pop(bisect.bisect_left(pq, height))
                #j += 1
            #i = j

            #m = pq[-1] if len(pq) > 0 else 0
            #if len(points) == 0 or points[-1][1] != m:
                #points.append((pos, m))

        #return points


if __name__ == '__main__':
    print skyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
    print skyline([[0, 2, 3], [2, 5, 3]])
    print skyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]])

    assert skyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]) == \
        [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]

    assert skyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]]) == \
        [(1, 3), (2, 0)]
