#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_pooling.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, time
import concurrent.futures as futures
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )
logger = logging.getLogger('logger')


def repeated_task(interations=1000):
    logger.debug('Starting')
    x = 0
    while x < interations:
        x += 1
    logger.debug(f'Exiting, x = {x}')
    return x / 100


def testing_thread_pool():
    _executer = ThreadPoolExecutor(max_workers=3)
    _future_tasks = _executer.submit(repeated_task, (10000000))
    print(f'Task complete: {_future_tasks.done()}')
    time.sleep(2)
    print(f'Task complete again: {_future_tasks.done()}')
    print(f'Tasks result: {_future_tasks.result()}')


def testing_thread_pool_with_values():
    _interations = [1000, 10001, 100002, 1000003, 1000004]
    with ThreadPoolExecutor(max_workers=3) as executer:
        _future_tasks = {executer.submit(repeated_task, interation):
                             interation for interation in _interations}
        for _future in futures.as_completed(_future_tasks):
            _interation = _future_tasks[_future]
            try:
                data = _future.result()
            except Exception as _exc:
                print('%r generated an exception: %s' % (_interation, _exc))
            else:
                print(f'future: {_future}, interation: {_interation}, result: {data}')


def testing_thread_map():
    _interations = [1000, 10001, 100002, 1000003, 1000004]
    with ThreadPoolExecutor(max_workers=3) as executer:
        _results = executer.map(repeated_task, _interations)
        for _result in _results:
            print(f'Result: {_result}')


if __name__ == "__main__":
    _start = time.time()
    testing_thread_pool()
    _end = _start - time.time()
    print(f'Thread pool took {_end} seconds\n\n')
    _start = time.time()
    testing_thread_pool_with_values()
    _end = _start - time.time()
    print(f'Completed threaded pools with values: {_end}\n\n')
    _start = time.time()
    testing_thread_map()
    _end = _start - time.time()
    print(f'Completed threaded pools with map: {_end}\n\n')
