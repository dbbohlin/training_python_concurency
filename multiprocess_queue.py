#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /multiprocess_queue.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, multiprocessing, time
from multiprocessing import Queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )
logger = logging.getLogger('logger')


def repeated_task(work_queue):
    x = 0
    logger.debug('Starting')
    while not work_queue.empty():
        try:
            _work = work_queue.get(timeout=1)
            logger.debug(f'got work: {_work}')
        except Exception as _exc:
            logger.debug(f'Exception caught, x = {x}, Exception: {_exc}')
            return x / 100
        y = 0
        while y < _work:
            x += 1
            y += 1
        logger.debug(f'Finished work, x = {x}')
    logger.debug(f'Exiting, x = {x}')
    return x / 100


def testing_multiprocessing_queue():
    _interations = [1000, 10001, 100002, 1000003, 1000004]
    _queue = Queue()
    for _ in _interations:
        _queue.put_nowait(_)
    _worker = multiprocessing.Process(target=repeated_task, args=(_queue,))
    _worker.start()
    _worker.join()


def testing_multiprocessing_queue_multiple():
    _interations = [1000, 10001, 100002, 13, 104, 1005, 1006, 1007, 1000008, 1000009]
    _interations_sup = [20010, 20000011, 20000012, 20013, 200015]
    _queue = Queue()
    for _ in _interations:
        _queue.put_nowait(_)
    _worker1 = multiprocessing.Process(target=repeated_task, args=(_queue,))
    _worker2 = multiprocessing.Process(target=repeated_task, args=(_queue,))
    _worker1.start()
    _worker2.start()
    for _ in _interations_sup:
        _queue.put_nowait(_)
    _worker1.join()
    _worker2.join()


if __name__ == "__main__":
    _start = time.time()
    testing_multiprocessing_queue()
    _end = _start - time.time()
    print(f'Completed threaded queue: {_end}\n\n')
    time.sleep(5)
    _start = time.time()
    testing_multiprocessing_queue_multiple()
    _end = _start - time.time()
    print(f'Completed threaded queue multiple workers: {_end}\n\n')
