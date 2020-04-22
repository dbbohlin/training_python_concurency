#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_v_serial.py
 Created by dbohlin on 4/5/20 for project t_training_python_concurency

"""

import threading, time, logging, math

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('thread join')


def sinFunc(offset=1000, n=1000):
    logger.debug('Starting')
    result = []
    for i in range(n):
        result.append(math.sin(offset + i * i))
    logger.debug(f'Exiting')
    return result


def testing_thread():
    threads = []
    for i in range(0, 9):
        thread = threading.Thread(name=f'thread_{i}', target=sinFunc)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def testing_serial():
    for i in range(0, 9):
        sinFunc()


if __name__ == "__main__":
    start = time.time()
    testing_serial()
    end_serial = start - time.time()
    print(f'Running serial:  {end_serial} seconds')
    start = time.time()
    testing_thread()
    end_thread = start - time.time()
    print(f'Running thread: {end_thread} seconds')
