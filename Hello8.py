import datetime
import functools


def log(text = ''):
    def decorator(fn):
        @functools.wraps(fn)
        def func(*args, **kw):
            print('%s executed in %s ms' % (fn.__name__, datetime.now()))
            return fn(*args, **kw)
        return func
    return decorator

@log()
def f1():
    print('end call %s' % datetime.now())

@log('execute')
def f2():
    print('end call %s' % datetime.now())

f1()
f2()
print(f1.__name__)