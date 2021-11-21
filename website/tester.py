import queue
spiderQueue = queue.Queue(maxsize = 0)
for i in range(10):
	spiderQueue.put(i)
item = spiderQueue.get()
print(spiderQueue.qsize())
spiderQueue.task_done()
spiderQueue.join()

