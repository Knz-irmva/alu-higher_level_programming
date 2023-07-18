#!/usr/bin/python3
#8-multiple_returns.py

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first = None
    else:
        first = sentence[0]
    return length, first
