#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_join.py
 Created by dbohlin on 4/12/20 for project t_training_python_concurency

"""

import logging, threading, time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('thread join')


def repeated_task(interations=10000000):
    logger.debug('Starting')
    x = 0
    while x < interations:
        x += 1
    logger.debug(f'Exiting, x = {x}')


def testing_thread_join(interations=10000000):
    thread_1 = threading.Thread(name='join thread 1', target=repeated_task, args=(interations,))
    thread_2 = threading.Thread(name='join thread 2', target=repeated_task, args=(interations,))
    # thread_1.setDaemon(True)
    # thread_2.setDaemon(True)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()


def testing_thread_no_join(interations=10000000):
    thread_1 = threading.Thread(name='no join thread 1', target=repeated_task, args=(interations,))
    thread_2 = threading.Thread(name='no join thread 2', target=repeated_task, args=(interations,))
    # thread_1.setDaemon(True)
    # thread_2.setDaemon(True)
    thread_1.start()
    thread_2.start()



if __name__ == "__main__":
    start = time.time()
    testing_thread_no_join()
    end_no_join = start - time.time()
    print(f'Thread no join took {end_no_join} seconds')
    start = time.time()
    testing_thread_join()
    end_join = start - time.time()
    print(f'Thread with join took {end_join} seconds')
