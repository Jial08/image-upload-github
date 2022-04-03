#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os


def notify(title, text):
    os.system("""
            osascript -e 'display notification "{}" with title "{}" sound name "Glass"'
            """.format(text, title))


def green(msg):
    """
    绿色提示
    :param msg:
    :return:
    """
    print('\033[32m {} \033[0m'.format(msg))


def yellow(msg):
    """
    黄色提示
    :param msg:
    :return:
    """
    print('\033[33m\033[01m {} \033[0m'.format(msg))


def red(msg):
    """
    红色提示
    :param msg:
    :return:
    """
    print('\033[31m\033[01m {} \033[0m'.format(msg))
