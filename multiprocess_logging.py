#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright David Bohlin (C) 2020
""" /multiprocess_logging.py
 Created by dbohlin on 4/20/20 for project t_training_python_concurency

"""

import logging, multiprocessing, time, sys
from pathlib import Path
from multiprocessing_logging import install_mp_handler

app_dir = Path(__file__).absolute().parent
sys.path.append(app_dir)
log_dir = Path(Path(app_dir) / 'logs')
log_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
logger = logging.getLogger('logger')

file_logger = logging.getLogger('file logger')
hdlr = logging.FileHandler(f'{str(log_dir)}/basic.log')
formatter = logging.Formatter('(%(threadName)-9s) %(message)s')
hdlr.setFormatter(formatter)
file_logger.addHandler(hdlr)
file_logger.setLevel(logging.DEBUG)


def repeated_task(interations=10):
    logger.debug('Starting')
    x = 0
    while x < interations:
        x += 1
    time.sleep(1)
    logger.debug(f'Exiting, x = {x}')
    return x


def worker_file_logging(interations=10):
    _process_name = multiprocessing.current_process().name
    file_logger.debug(f'{_process_name} Starting')
    x = 0
    while x < interations:
        x += 1
    time.sleep(1)
    file_logger.debug(f'{_process_name} Exiting, x = {x}')
    return x


def worker_file_internal_logging_bad(interations=10):
    _file_logger = logging.getLogger('internal file logger')
    _hdlr = logging.FileHandler(f'{str(log_dir)}/bad.log')
    _formatter = logging.Formatter('(%(threadName)-9s) %(message)s')
    _hdlr.setFormatter(_formatter)
    _file_logger.addHandler(hdlr)
    _file_logger.info('Starting')
    x = 0
    while x < interations:
        x += 1
    time.sleep(1)
    _file_logger.info(f'Exiting, x = {x}')
    return x


def worker_file_internal_logging_stderr(interations=10):
    _process_name = multiprocessing.current_process().name
    multiprocessing.log_to_stderr()
    _file_logger = multiprocessing.get_logger()
    _file_logger.info('Starting')
    x = 0
    while x < interations:
        x += 1
    time.sleep(1)
    _file_logger.info(f'Exiting, x = {x}')
    return x


def testing_multiprocessing_basic_logging():
    _interations = [10, 11, 12, 13, 14]
    _workers = []
    for i in range(len(_interations)):
        _worker = multiprocessing.Process(name=f'worker{i}',
                                          target=repeated_task,
                                          args=(_interations[i],))
        _worker.start()
        _workers.append(_worker)
    print('Running proceeses with basic logging')


def testing_multiprocessing_file_logging():
    _interations = [10, 11, 12, 13, 14]
    _workers = []
    for i in range(len(_interations)):
        _worker = multiprocessing.Process(name=f'worker{i}',
                                          target=worker_file_logging,
                                          args=(_interations[i],))
        _worker.start()
        _workers.append(_worker)
    print('Running proceeses with basic logging')


def testing_multiprocessing_bad_file_logging():
    _interations = [10, 11, 12, 13, 14]
    _workers = []
    for i in range(len(_interations)):
        _worker = multiprocessing.Process(name=f'worker{i}',
                                          target=worker_file_internal_logging_bad,
                                          args=(_interations[i],))
        _worker.start()
        _workers.append(_worker)
    print('Running proceeses with basic logging')


def testing_multiprocessing_stderr_logging():
    _interations = [10, 11, 12, 13, 14]
    _workers = []
    for i in range(len(_interations)):
        _worker = multiprocessing.Process(name=f'worker{i}',
                                          target=worker_file_internal_logging_stderr,
                                          args=(_interations[i],))
        _worker.start()
        _workers.append(_worker)
    print('Running proceeses with basic logging')


if __name__ == "__main__":
    _start = time.time()
    testing_multiprocessing_basic_logging()
    _end = _start - time.time()
    print(f'Multiprocessing basic log took {_end} seconds')
    _start = time.time()
    testing_multiprocessing_file_logging()
    _end = _start - time.time()
    print(f'Multiprocessing file log took {_end} seconds')
    _start = time.time()
    testing_multiprocessing_bad_file_logging()
    _end = _start - time.time()
    print(f'Multiprocessing bad file log took {_end} seconds')
    time.sleep(2)
    print('\n\n')
    _start = time.time()
    testing_multiprocessing_stderr_logging()
    _end = _start - time.time()
    print(f'Multiprocessing stderr log took {_end} seconds')
