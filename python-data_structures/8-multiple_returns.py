#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple of length of sentence and first character (or None if empty)."""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
