import asyncio, threading

@asyncio.coroutine
def hello():
	print("hello world %s" % threading.currentThread())
	#看做io操作（异步操作需要在coroutine中通过yield from完成）
	r = yield from asyncio.sleep(1)
	print("hello again %s" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()





