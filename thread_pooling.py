#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_pooling.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, threading, time
import concurrent.futures as futures
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('thread join')


def repeated_task(interations=1000):
    logger.debug('Starting')
    x = 0
    while x < interations:
        x += 1
    logger.debug(f'Exiting, x = {x}')
    return x/100


def testing_thread_pool():
    executer = ThreadPoolExecutor(max_workers=3)
    future_tasks = executer.submit(repeated_task, (10000000))
    print(f'Task complete: {future_tasks.done()}')
    time.sleep(2)
    print(f'Task complete again: {future_tasks.done()}')
    print(f'Tasks result: {future_tasks.result()}')


def testing_thread_pool_with_values():
    interations = [1000,10001,100002,1000003, 1000004]
    with ThreadPoolExecutor(max_workers=3) as executer:
        future_tasks = {executer.submit(repeated_task, interation):
                            interation for interation in interations}
        for future in futures.as_completed(future_tasks):
            interation = future_tasks[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (interation, exc))
            else:
                print(f'future: {future}, interation: {interation}, result: {data}')


def testing_thread_map():
    interations = [1000,10001,100002,1000003, 1000004]
    with ThreadPoolExecutor(max_workers=3) as executer:
        results = executer.map(repeated_task, interations)
        for result in results:
            print(f'Result: {result}')


if __name__ == "__main__":
    start = time.time()
    testing_thread_pool()
    end_time = start - time.time()
    print(f'Thread pool took {end_time} seconds\n\n')
    start = time.time()
    testing_thread_pool_with_values()
    end_time = start - time.time()
    print(f'Completed threaded pools with values: {end_time}\n\n')
    start = time.time()
    testing_thread_map()
    end_time = start - time.time()
    print(f'Completed threaded pools with map: {end_time}\n\n')
