#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_deadlock.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, threading, time
from threading import Lock

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('logger')


class DeadLockIncrement():
    def __init__(self):
        self.x = 0
        self.lock = Lock()

    def add(self, value=1):
        with self.lock:
            self.x += value

    def increment_no_deadlock(self, value=1):
        with self.lock:
            self.x = value
        self.add(value)
        return self.x

    def increment(self, value=1):
        with self.lock:
            self.x += value
            self.add(value)
        return self.x


deadlock = DeadLockIncrement()

if __name__ == "__main__":
    deadlock.increment_no_deadlock()
    print(f'This works Dead Lock value: {deadlock.x}')
    deadlock.increment()
    print(f'We will never get here for Dead Lock value: {deadlock.x}')
