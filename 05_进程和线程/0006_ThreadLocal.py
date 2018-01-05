import threading, random, time

local_00 = threading.local()


def process_task():

    print(local_00.name)

def run_exec_task(name_00):
    local_00.name = name_00
    process_task()


if __name__ == '__main__':
    thread_00 = threading.Thread(target=run_exec_task, args=("Test_1",))
    thread_01 = threading.Thread(target=run_exec_task, args=("Test_2",))

    thread_00.start()
    thread_01.start()
    thread_00.join()
    thread_01.join()
