from multiprocessing import Pool
import os, time, random


def long_task_exec(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print("Parent Process %s" % os.getpid());

    pool_00 = Pool(8)

    for index_00 in range(8):
        pool_00.apply_async(long_task_exec, args=(index_00,))

    print("Waiting for all subprocess done...")
    pool_00.close()
    pool_00.join()
    print("all done...")
