#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_asyncio.py
 Created by dbohlin on 4/12/20 for project t_training_python_concurency

"""

import logging, asyncio, time, threading

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('thread join')


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
    threads = []
    for i in range(5):
        thread = threading.Thread(name=f'thread_{i}', target=repeated_thread, args=[i*200, i])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    logger.debug(f'thread function ended')


if __name__ == '__main__':
    start = time.time()
    asyncio.run(testing_asyncio()) # Event Loop
    end_asyncio = start - time.time()
    print(f'Running asyncio:  {end_asyncio} seconds')
    start = time.time()
    testing_thread()
    end_thread = start - time.time()
    print(f'Running thread:  {end_thread} seconds')
