#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_join.py
 Created by dbohlin on 4/12/20 for project t_training_python_concurency

"""

import logging, threading, time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('logger')


def repeated_task(interations=10000000):
    logger.debug('Starting')
    x = 0
    while x < interations:
        x += 1
    logger.debug(f'Exiting, x = {x}')


def testing_thread_join(interations=10000000):
    _thread_1 = threading.Thread(name='join thread 1', target=repeated_task, args=(interations,))
    _thread_2 = threading.Thread(name='join thread 2', target=repeated_task, args=(interations,))
    _thread_1.start()
    _thread_2.start()
    _thread_1.join()
    _thread_2.join()


def testing_thread_no_join(interations=10000000):
    _thread_1 = threading.Thread(name='no join thread 1', target=repeated_task, args=(interations,))
    _thread_2 = threading.Thread(name='no join thread 2', target=repeated_task, args=(interations,))
    _thread_1.start()
    _thread_2.start()



if __name__ == "__main__":
    _start = time.time()
    testing_thread_no_join()
    _end = _start - time.time()
    print(f'Thread no join took {_end} seconds')
    _start = time.time()
    testing_thread_join()
    _end = _start - time.time()
    print(f'Thread with join took {_end} seconds')
