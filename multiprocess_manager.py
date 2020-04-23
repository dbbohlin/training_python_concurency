#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /multiprocess_manager.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, multiprocessing, time


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('logger')


def repeated_task(dict_value, interations=10000000):
    process_name = multiprocessing.current_process().name
    logger.debug(f'Starting {process_name}')
    x = 0
    while x < interations:
        x += 1
    logger.debug(f'Exiting, x = {x}')
    dict_value[process_name] = x
    return x


def insertion_task(element, elements):
    process_name = multiprocessing.current_process().name
    logger.debug(f'Starting insertion: {process_name}')
    if isinstance(elements, multiprocessing.managers.ListProxy):
        elements.append(element)
    else:
        for key, value in element.items():
            elements[key] = value
    logger.debug(f'Exiting, inserted: {element}')


def testing_multiprocessing_manager_result():
    _interations = [1000, 10001, 100002, 1000003, 1000004]
    _manager = multiprocessing.Manager()
    _shared_dict = _manager.dict()
    _workers = []
    for i in range(len(_interations)):
        _worker = multiprocessing.Process(name=f'worker{i}',
                                          target=repeated_task,
                                          args=(_shared_dict, _interations[i], ))
        _worker.start()
        _workers.append(_worker)
    for _worker in _workers:
        _worker.join()
    print(f'Manage shared dict: {_shared_dict}')


def testing_multiprocessing_manager_insert():
    _records = {'a': 1000, 'b': 10001, 'c': 100002, 'd': 1000003, 'e': 1000004}
    _manager = multiprocessing.Manager()
    _elements = _manager.list()
    _workers = []
    for value in _records.items():
        _worker = multiprocessing.Process(target=insertion_task,
                                          args=(value, _elements, ))
        _worker.start()
        _workers.append(_worker)
    for _worker in _workers:
        _worker.join()
    print(f'Updated elements: {_elements}')


def testing_multiprocessing_manager_extended():
    _records = {'a': 1000, 'b': 10001, 'c': 100002, 'd': 1000003, 'e': 1000004}
    _manager = multiprocessing.Manager()
    _elements = _manager.dict(_records)
    _workers = []
    _new_value = {'b': 1}
    for value in _records.items():
        _worker = multiprocessing.Process(target=insertion_task,
                                          args=(_new_value, _elements, ))
        _worker.start()
        _workers.append(_worker)
    for _worker in _workers:
        _worker.join()
    print(f'Updated elements: {_elements}')


if __name__ == "__main__":
    _start = time.time()
    testing_multiprocessing_manager_result()
    _end = _start - time.time()
    print(f'Multiprocessing with manager took {_end} seconds')
    _start = time.time()
    testing_multiprocessing_manager_insert()
    _end = _start - time.time()
    print(f'Multiprocessing manager extended took {_end} seconds')
    _start = time.time()
    testing_multiprocessing_manager_extended()
    _end = _start - time.time()
    print(f'Multiprocessing manager extended took {_end} seconds')

