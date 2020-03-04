import numpy as np
from numba import njit
import ray

@njit(fastmath=True)
def mz_centroid(_int_f, _mz_f):
    return ((_int_f/_int_f.sum()) * _mz_f).sum()


@ray.remote
def f():
    a = np.random.random(10)
    b = 123
    return mz_centroid(a, b)


ray.init(address='auto', redis_password='5241590000000000')
results = ray.get([f.remote() for i in range(4)])
print(results)