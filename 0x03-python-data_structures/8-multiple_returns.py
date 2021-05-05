#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuple_c = (0, 0)
        tuple_c = (len(sentence), sentence[0])
        return(tuple_c)
    return(0, None)
