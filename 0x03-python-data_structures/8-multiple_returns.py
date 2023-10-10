#!/usr/bin/python3
def multiple_returns(sentence):
    i = 0
    first_char = ""
    if not sentence:
        first_char = None
    else:
        first_char = sentence[0]
        for w in sentence:
            i += 1
    sent = i, first_char
    return sent
