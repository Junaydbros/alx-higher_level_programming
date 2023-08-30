#!/usr/bin/python3

from sys import stderr
def safe_function(fct, *args):
    try:
        answer = fct(*args)
        return answer
    except Exception as err:
        print("Exception: {}".format(str(err)), file=stderr)
        return None
