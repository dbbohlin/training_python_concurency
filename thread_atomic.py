#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_atomic.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, threading, time
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('logger')


def testing_imutable_tuple():
    _tuple = (0, 1, 2, 3)
    try:
        _tuple[0] = 4
    except Exception as exc:
        print(f'Trying to assign to tuple: {exc}')


def testing_imutable_String():
    _string = "testing string"
    try:
        _string[0] = '4'
    except Exception as exc:
        print(f'Trying to assign to string: {exc}')


mutex = Lock()


def repeated_task(interations=10000000):
    mutex.acquire()
    logger.debug('Starting')
    try:
        x = 0
        while x < interations:
            x += 1
    finally:
        mutex.release()
    logger.debug(f'Exiting, x = {x}')


def testing_thread_mutex():
    _interations = [1000, 10001, 100002, 1000003, 1000004]
    with ThreadPoolExecutor(max_workers=3) as executer:
        _results = executer.map(repeated_task, _interations)
        for _result in _results:
            print(f'Result: {_result}')


if __name__ == "__main__":
    testing_imutable_String()
    testing_imutable_tuple()
    _start = time.time()
    testing_thread_mutex()
    _end = _start - time.time()
    print(f'Thread with mutex took {_end} seconds')
