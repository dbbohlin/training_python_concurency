#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /multiprocess_zombies.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, multiprocessing, time, psutil

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


def close_properly():
    _interations = [1000, 10001, 100002, 1000003, 1000004]
    _pool = multiprocessing.Pool(processes=3)
    try:
        _results = [_pool.apply(repeated_task, args=(x,)) for x in _interations]
    finally:
        _pool.close()
        _pool.join()
    print(f'Pool results: {_results}')


def testing_multiprocessing_pool_with_cleanup():
    _before_proc = []
    _after_proc = []
    for _proc in psutil.process_iter():
        _before_proc.append(_proc.name())
    close_properly()
    for _proc in psutil.process_iter():
         _after_proc.append(_proc.name())
    print(f'Differences: {len(_before_proc)} vs {len(_after_proc)}')


def create_zombies():
    _interations = [1000, 10001, 100002, 1000003, 1000004]
    _pool = multiprocessing.Pool(processes=3)
    _results = _pool.map(repeated_task, _interations)
    print(f'Pool map results: {_results}')


def testing_multiprocessing_pool_map_zombie():
    _before_proc = []
    _after_proc = []
    for _proc in psutil.process_iter():
        _before_proc.append(_proc.name())
    create_zombies()
    for _proc in psutil.process_iter():
        _after_proc.append(_proc.name())
    print(f'Differences: {len(_before_proc)} vs {len(_after_proc)}')


if __name__ == "__main__":
    _start = time.time()
    testing_multiprocessing_pool_with_cleanup()
    _end = _start - time.time()
    print(f'Multiprocessing with pool and cleanup took {_end} seconds')
    time.sleep(3)
    _start = time.time()
    testing_multiprocessing_pool_map_zombie()
    _end = _start - time.time()
    print(f'Multiprocessing with map with zombies took {_end} seconds')
