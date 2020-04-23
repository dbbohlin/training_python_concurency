#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_asyncio.py
 Created by dbohlin on 4/12/20 for project t_training_python_concurency

"""

import logging, asyncio, time, threading

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('logger')


async def repeated_task(interations=100, delay=1):
    logger.debug('Starting')
    x = 0
    while x < interations:
        x += 1
    await asyncio.sleep(delay)
    logger.debug(f'Exiting, x = {x}')


def repeated_thread(interations=100, delay=1):
    logger.debug('Starting')
    x = 0
    while x < interations:
        x += 1
    time.sleep(delay)
    logger.debug(f'Exiting, x = {x}')


async def testing_asyncio():
    logger.debug(f'asyncio function started')
    await asyncio.gather(*[repeated_task(i*200, i) for i in range(5)])
    logger.debug(f'asyncio function ended')


def testing_thread():
    logger.debug(f'thread function started')
    _threads = []
    for i in range(5):
        _thread = threading.Thread(name=f'thread_{i}', target=repeated_thread, args=[i*200, i])
        _threads.append(_thread)
        _thread.start()
    for _thread in _threads:
        _thread.join()
    logger.debug(f'thread function ended')


if __name__ == '__main__':
    _start = time.time()
    asyncio.run(testing_asyncio()) # Event Loop
    _end = _start - time.time()
    print(f'Running asyncio:  {_end} seconds')
    _start = time.time()
    testing_thread()
    _end = _start - time.time()
    print(f'Running thread:  {_end} seconds')
