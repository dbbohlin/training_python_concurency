#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_daemon.py
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


def testing_thread_daemon():
    thread_1 = threading.Thread(name='join thread 1', target=repeated_task, args=(1000,))
    thread_2 = threading.Thread(name='join thread 2', target=repeated_task, args=(100000,))
    daemon_thread = threading.Thread(name='daemon thread', target=repeated_task, args=(10000000,))
    daemon_thread.setDaemon(True)
    thread_1.start()
    thread_2.start()
    daemon_thread.start()
    thread_1.join()
    thread_2.join()
    # daemon_thread.join()


if __name__ == "__main__":
    start = time.time()
    testing_thread_daemon()
    end_join = start - time.time()
    print(f'Thread with join took {end_join} seconds')
