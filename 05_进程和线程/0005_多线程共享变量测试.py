import threading, time, random

balance = 0

lock_00 = threading.RLock()

def run_exec_task(n):
    global balance

    balance = int(balance + n)
    balance = int(balance - n)

def loop_charge_it(index_01):
    for index_00 in range(1000000):
        lock_00.acquire()
        lock_00.acquire()
        run_exec_task(index_01)
        lock_00.release()
        lock_00.release()

if __name__ == '__main__':
    time_00 = time.time()
    thread_00 = threading.Thread(target=loop_charge_it, args=(3,))
    thread_01 = threading.Thread(target=loop_charge_it, args=(2,))

    thread_00.start()
    thread_01.start()
    thread_00.join()
    thread_01.join()

    time_01 = time.time()

    print("用时 %.5fs计算完毕,得到的数值为: %s" % (time_01 - time_00, balance))
