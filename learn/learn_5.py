#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import random
import json
from multiprocessing import Process, Pool
import subprocess

# IO

# with open('./test.txt', 'r', encoding='gbk', errors='ignore') as f:
#     for line in f.readlines():
#         print(line.strip())
#
# with open('./test.txt', 'w') as f:
#     f.write('TO ME, YOU ARE PERFECT!')


# for f in os.listdir('.'):
#     if os.path.isfile(f) and os.path.splitext(f)[1] == '.py':
#         print(os.path.abspath(f))

# 多进程


def run_task(task):
    print('Run task %s (%s)...' % (task, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (task, (end - start)))


# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(8)
#     for i in range(5):
#         p.apply_async(run_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)

