#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Default configurations.
"""

__author__ = 'Francis yang'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'src',
        'password': 'src',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
