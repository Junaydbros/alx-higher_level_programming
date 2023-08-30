#!/usr/bin/python3

def multiple_returns(sentence):
    tupleLen = len(sentence)

    if tupleLen == 0:
        char1 = None
    else:
        char1 = sentence[0]
    return (tupleLen, char1)
