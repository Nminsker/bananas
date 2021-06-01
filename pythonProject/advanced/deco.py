import sys


def with_output_to_out_txt(f):
    def wrapped_f(*args, **kw):
        old_target, sys.stdout = sys.stdout, open('output', 'w')
        try:
            return f(*args, **kw)
        finally:
            sys.stdout.close()
            sys.stdout = old_target
    return wrapped_f


@with_output_to_out_txt
def hello(name):
    print("Hello {0}".format(name))


def with_output_to(file_name):
    def wrap(f):
        def wrapped_f(*args, **kw):
            old_target, sys.stdout = sys.stdout, open(file_name, 'w')
            try:
                return f(*args, **kw)
            finally:
                sys.stdout.close()
                sys.stdout = old_target
        return wrapped_f
    return wrap


@with_output_to("out.txt")
def hello2(s):
    print(s)
