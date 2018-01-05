import threading, random, os, time

def thread_loop(name):
    print("now get name is %s ." % name)
    print("the new thread is %s" % threading.current_thread().name)
    index_00 = 0
    while index_00 < 5:
        print("thread %s => %s" % (threading.current_thread().name, index_00))
        time.sleep(random.random() * 1)
        index_00 += 1

    print("Thread is %s => %d" % (threading.current_thread().name, index_01))

if __name__ == '__main__':
    print("Current Thread is %s , It is running..." % threading.current_thread().getName())
    print("Changed The %s's name , now the new name is" % threading.current_thread().getName(), end=" ")
    threading.current_thread().setName("JasonThread")
    print("%s , it is also running..." % threading.current_thread().getName())

    index_01 = 100
    name = "Jason Morata."
    thread_00 = threading.Thread(target=thread_loop, name="Thread_001", args=(name,))
    thread_01 = threading.Thread(target=thread_loop, name="Thread_002", args=(name,))
    thread_00.start()
    thread_01.start()
    thread_00.join()
    thread_01.join()
    print('thread %s ended.' % threading.current_thread().name)
