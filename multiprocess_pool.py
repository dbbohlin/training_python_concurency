#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /multiprocess_pool.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, multiprocessing, time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('logger')


def repeated_task(interations=10000000):
    logger.debug('Starting')
    x = 0
    while x < interations:
        x += 1
    logger.debug(f'Exiting, x = {x}')
    return x


def testing_multiprocessing_process():
    _interations = [1000, 10001, 100002, 1000003, 1000004]
    _workers = []
    for i in range(len(_interations)):
        _worker = multiprocessing.Process(name=f'worker{i}',
                                          target=repeated_task,
                                          args=(_interations[i],))
        _worker.start()
        _workers.append(_worker)
    for _worker in _workers:
        _worker.join()


def testing_multiprocessing_pool():
    _interations = [1000, 10001, 100002, 1000003, 1000004]
    _pool = multiprocessing.Pool(processes=3)
    _results = [_pool.apply(repeated_task, args=(x,)) for x in _interations]
    print(f'Pool results: {_results}')


def testing_multiprocessing_pool_map():
    _interations = [1000, 10001, 100002, 1000003, 1000004]
    _pool = multiprocessing.Pool(processes=3)
    _results = _pool.map(repeated_task, _interations)
    print(f'Pool map results: {_results}')


if __name__ == "__main__":
    _start = time.time()
    testing_multiprocessing_process()
    _end = _start - time.time()
    print(f'Multiprocessing process took {_end} seconds')
    _start = time.time()
    testing_multiprocessing_pool()
    _end = _start - time.time()
    print(f'Multiprocessing with pool took {_end} seconds')
    _start = time.time()
    testing_multiprocessing_pool_map()
    _end = _start - time.time()
    print(f'Multiprocessing with map took {_end} seconds')
