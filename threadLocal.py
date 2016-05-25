import threading
#api
threadLocal_student = threading.local()
def process_student():
	std = threadLocal_student.student
	print('Hello %s in %s' % (std, threading.current_thread().name))
def procees_thread(name):
	threadLocal_student.student = name
	process_student()

t1 = threading.Thread(target=procees_thread, args=('Alice',), name='Thread-Alice')
t2 = threading.Thread(target=procees_thread, args=('Feynming',), name='Thread-Feynming') 
t1.start()
t2.start()
t1.join()
t2.join()