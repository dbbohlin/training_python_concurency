#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /thread_atomic.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, threading, time
from threading import Lock

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('thread join')


def testing_imutable_tuple():
    _tuple = (0, 1, 2, 3)
    try:
        _tuple[0] = 4
    except Exception as exc:
        print(f'Trying to assign to tuple: {exc}')


def testing_imutable_String():
    _string = "testing string"
    try:
        _string[0] = '4'
    except Exception as exc:
        print(f'Trying to assign to string: {exc}')

    
def testing_thread_atomic():
    pass


if __name__ == "__main__":
    testing_imutable_String()
    testing_imutable_tuple()
