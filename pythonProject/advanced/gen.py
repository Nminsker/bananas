from textwrap import wrap


def reformat(stream):
    for par in stream:
        yield par + '\n'
