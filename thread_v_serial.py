#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_v_serial.py
 Created by dbohlin on 4/5/20 for project t_training_python_concurency

"""

import threading, time, logging, math

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('logger')


def sin_function(offset=1000, n=1000):
    logger.debug('Starting')
    _result = []
    for i in range(n):
        _result.append(math.sin(offset + i * i))
    logger.debug(f'Exiting')
    return _result


def testing_thread():
    _threads = []
    for i in range(0, 9):
        _thread = threading.Thread(name=f'thread_{i}', target=sin_function)
        _threads.append(_thread)
        _thread.start()
    for _thread in _threads:
        _thread.join()


def testing_serial():
    for i in range(0, 9):
        sin_function()


if __name__ == "__main__":
    _start = time.time()
    testing_serial()
    _end = _start - time.time()
    print(f'Running serial:  {_end} seconds')
    _start = time.time()
    testing_thread()
    _end = _start - time.time()
    print(f'Running thread: {_end} seconds')
