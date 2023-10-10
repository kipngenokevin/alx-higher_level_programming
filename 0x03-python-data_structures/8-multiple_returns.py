#!/usr/bin/python3
def multiple_returns(sentence):
    i = 0
    for w in sentence:
        i += 1
    sent = i, sentence[0]
    return sent
