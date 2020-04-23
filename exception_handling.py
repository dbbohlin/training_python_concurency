#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /exception_handling.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, threading, time, queue, sys, multiprocessing, traceback
from multiprocessing import Process

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('logger')

exception_queue = queue.Queue()


class MyProcess(Process):
    def __init__(self, *args, **kwargs):
        Process.__init__(self, *args, **kwargs)
        self._pconn, self._cconn = multiprocessing.Pipe()
        self._exception = None

    def run(self):
        try:
            Process.run(self)
            self._cconn.send(None)
        except Exception as e:
            tb = traceback.format_exc()
            self._cconn.send((e, tb))

    @property
    def exception(self):
        if self._pconn.poll():
            self._exception = self._pconn.recv()
        return self._exception


def exception_task():
    logger.debug('Starting Exception')
    raise Exception('throwing exception from exception_task')


def queueing_exception():
    logger.debug('Starting queue exception')
    try:
        raise Exception('throwing exception from exception queue')
    except Exception as _exc:
        logger.debug(f'Caught Exception: {_exc}')
        exception_queue.put(sys.exc_info())


def testing_thread_exception():
    _thread_1 = threading.Thread(name='thread 1', target=exception_task)
    try:
        _thread_1.start()
        _thread_1.join()
    except Exception as _exc:
        print(f'Found exception: {_exc}')


def testing_thread_exception_queue():
    _thread_1 = threading.Thread(name='queue thread 1', target=queueing_exception)
    _thread_1.start()
    _thread_1.join()
    if not exception_queue.empty():
        print(f'queued exception: {exception_queue.get(block=False)}')


def testing_multiprocessing_exception():
    _process = MyProcess(target=exception_task)
    _process.start()
    _process.join()

    if _process.exception:
        _exc, traceback = _process.exception
        print(f'Exception: {_exc}, traceback: {traceback}')


if __name__ == "__main__":
    _start = time.time()
    testing_thread_exception()
    _end = _start - time.time()
    print(f'Thread exception took {_end} seconds')
    _start = time.time()
    testing_thread_exception_queue()
    _end = _start - time.time()
    print(f'Thread exception queue took {_end} seconds\n\n')
    time.sleep(1)
    _start = time.time()
    testing_multiprocessing_exception()
    _end = _start - time.time()
    print(f'Multiprocessing exception took {_end} seconds')
