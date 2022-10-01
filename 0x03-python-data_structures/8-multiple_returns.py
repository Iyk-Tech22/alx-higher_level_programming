#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        first_letter = sentence[0]
        tuples = length, first_letter
        return (tuples)
    else:
        tuples = (0, None)
        return (tuples)
