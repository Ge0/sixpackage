"""Just a dump script that exports a function expected to run for both
Python 2.x and 3.x
"""
import six


def my_universal_function():
    if six.PY2:
        return u'This is a unicode string'
    else:
        return 'This is a unicode string'
