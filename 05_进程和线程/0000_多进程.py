from  multiprocessing import Process
import os
import time

def run_proc(name, take):
    print('Run child process %s (%s) %s...' % (name, take, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', "Hello"))
    print('Child process will start.')
    p.start()
    print('Child process has started.')
    p.join()
    print('Child process end.')
