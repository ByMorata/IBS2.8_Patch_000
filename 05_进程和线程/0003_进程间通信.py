from multiprocessing import Process, Pool, Queue
import os, io, time, random


def write_queue(quenu_00):
    quenu_01 = Queue()

    for index_00 in range(10):
        str_00 = random.random() * 10
        quenu_01.put(str_00)
        print("index: %s  => get %s" % (index_00, str_00), end=" ")

        str_01 = random.random()
        time.sleep(str_01)
        print(" %.2f s" % str_01)


def read_queue(quenu_00):
    quenu_01 = Queue()

    for index_00 in range(10):
        str_00 = random.random() * 10
        quenu_01.put(str_00)
        print("index: %s  => put %s" % (index_00, str_00),end=" ")
        str_01 = random.random()
        time.sleep(str_01)
        print(" %.2f s" % str_01)


if __name__ == '__main__':
    # 父进程创建队列
    queue_00 = Queue()
    process_00 = Process(target=write_queue, args=(queue_00,))
    process_01 = Process(target=read_queue, args=(queue_00,))

    process_00.start()
    process_01.start()

    process_00.join()
    process_01.terminate()
