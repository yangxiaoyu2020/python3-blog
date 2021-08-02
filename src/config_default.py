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
        'user': 'root',
        'db': 'blog',
        'password': '*******'
        #   取个好名字以后
    },
    'session': {
        'secret': 'Awesome'
    }
}
