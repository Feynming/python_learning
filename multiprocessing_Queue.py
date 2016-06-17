from multiprocessing import Process, Queue

import os, time, random

#写进程执行的代码
def write(q):
	print("Process %s to write" % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

#读进程执行的代码	
def read(q):
	print("Process %s to read" % os.getpid())
	while(True):
		value = q.get(True)
		print('Get %s from queue...' % value)
		
if __name__ == "__main__":
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()