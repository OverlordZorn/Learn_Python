import queue
x = queue.LifoQueue()

for y in 5, 19, -2, 12:
    x.put(y)

while not x.empty():
    print(x.get())