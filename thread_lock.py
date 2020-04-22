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
logger = logging.getLogger('thread join')


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


_increment = Increment()
_locking_increment = LockingIncrement()


def incrementer(increment=100000):
    for i in range(increment):
        _increment.increment()


def incrementer_with_lock(increment=100000):
    for i in range(increment):
        _locking_increment.increment()


def testing_thread_without_lock():
    threads = []
    for i in range(2):
        new_thread = threading.Thread(name=f'thread{i}', target=incrementer, args=(100000,))
        new_thread.start()
        threads.append(new_thread)

    for thread in threads:
        thread.join()
    print(f'Incrementing without locks, Incrementer value: {_increment.x}')


def testing_thread_with_lock():
    threads = []
    for i in range(2):
        new_thread = threading.Thread(name=f'lock_thread{i}', target=incrementer_with_lock, args=(100000,))
        new_thread.start()
        threads.append(new_thread)

    for thread in threads:
        thread.join()
    print(f'Incrementing with locks, Incrementer value: {_locking_increment.x}')


if __name__ == "__main__":
    for i in range(100000):
        _increment.increment()
    print(f'Incrementing by itself Incrementer value: {_increment.x}')
    testing_thread_without_lock()
    testing_thread_with_lock()
