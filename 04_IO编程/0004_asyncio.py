import asyncio


@asyncio.coroutine
def hello():
    print("Hello World!")
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(10)
    print("Hello Again")


# 获取Eventloop:
loop = asyncio.get_event_loop()
# 执行conroutine():
loop.run_until_complete(hello())
loop.close()
