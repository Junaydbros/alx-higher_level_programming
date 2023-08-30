#!/usr/bin/python3

from sys import stderr

def safe_function(fct, *args):
    try:
        answer = fct(*args)
        return answer
    except Exception as e:
        print("Exception: {}".format(str(e)), file=stderr)
        return None
