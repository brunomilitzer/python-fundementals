import queue

q = queue.Queue()
q.put(400)
q.put(100)
q.put(500)
q.put(50)

while not q.empty():
    print(q.get(), end=' ')

print()

lq = queue.LifoQueue()
lq.put(400)
lq.put(100)
lq.put(500)
lq.put(50)

while not lq.empty():
    print(lq.get(), end=' ')


print()

pq = queue.PriorityQueue()
pq.put(400)
pq.put(100)
pq.put(500)
pq.put(50)

while not pq.empty():
    print(pq.get(), end=' ')


print()

tpq = queue.PriorityQueue()
tpq.put((400, "Vanessa"))
tpq.put((100, "Bruno"))
tpq.put((500, "Tales"))
tpq.put((50, "José"))

while not tpq.empty():
    print(tpq.get()[1], end=' ')