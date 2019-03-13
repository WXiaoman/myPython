# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def now():
#     print("ok")
#
# now()

import time
import functools

def clock(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        t0 = time.time()
        result = fn(*args,**kw)
        #print('{s} executed in {t} seconds'.format(s=fn.__name__,t=time.time()-t0))
        print('%s executed in %.4f seconds' % (fn.__name__, time.time()-t0))
        return result
    return wrapper

@clock
def multi(x, y):
    time.sleep(0.5)
    return x * y

multi(3, 5)

# 测试
@clock
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@clock
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
