import queue
x = queue.PriorityQueue()
for y in 5, 19, -2, 12:
    x.put(y)
while not x.empty():
    print(x.get())
