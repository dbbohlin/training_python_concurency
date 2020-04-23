#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_lock.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, threading, time
from threading import Lock

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('logger')


class Increment():
    def __init__(self):
        self.x = 0

    def increment(self, value=1):
        self.x += value


class LockingIncrement():
    def __init__(self):
        self.x = 0
        self.lock = Lock()

    def increment(self, value=1):
        with self.lock:
            self.x += value


increment_obj = Increment()
locking_increment_obj = LockingIncrement()


def incrementer(increment=100000):
    for i in range(increment):
        increment_obj.increment()


def incrementer_with_lock(increment=100000):
    for i in range(increment):
        locking_increment_obj.increment()


def testing_thread_without_lock():
    _threads = []
    for i in range(2):
        _new_thread = threading.Thread(name=f'thread{i}', target=incrementer, args=(100000,))
        _new_thread.start()
        _threads.append(_new_thread)

    for _thread in _threads:
        _thread.join()
    print(f'Incrementing without locks, Incrementer value: {increment_obj.x}')


def testing_thread_with_lock():
    _threads = []
    for i in range(2):
        _new_thread = threading.Thread(name=f'lock_thread{i}', target=incrementer_with_lock, args=(100000,))
        _new_thread.start()
        _threads.append(_new_thread)

    for _thread in _threads:
        _thread.join()
    print(f'Incrementing with locks, Incrementer value: {locking_increment_obj.x}')


if __name__ == "__main__":
    for i in range(100000):
        increment_obj.increment()
    print(f'Incrementing by itself Incrementer value: {increment_obj.x}')
    testing_thread_without_lock()
    testing_thread_with_lock()
