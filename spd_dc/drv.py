from collections import defaultdict

from numpy import arange, dtype, float64, full, int64, ndarray
from numpy import negative as np_negative
from scipy.signal import convolve
from scipy.stats import rv_discrete

Drv = rv_discrete
Pk = ndarray[tuple[int], dtype[float64]]
Xk = ndarray[tuple[int], dtype[int64]]


def add(lhs: Drv, rhs: Drv) -> Drv:
    lhs_xk, rhs_xk = map(get_xk, (lhs, rhs))

    lhs_pk = get_pk(lhs, lhs_xk)
    rhs_pk = get_pk(rhs, rhs_xk)

    xk = arange(lhs.a + rhs.a, lhs.b + rhs.b + 1, dtype=int64)
    pk = convolve(lhs_pk, rhs_pk)

    return Drv(values=(xk, pk))


def add_probabilities(drv: Drv, xk: list[int], pk: list[float]) -> Drv:
    drv_xk = get_xk(drv)
    drv_pk = get_pk(drv, drv_xk) * (1 - sum(pk))
    dd = defaultdict(float, zip(drv_xk, drv_pk))
    for x, p in zip(xk, pk):
        dd[x] += p
    new_xk = list(dd.keys())
    new_pk = list(dd.values())
    return Drv(values=(new_xk, new_pk))


def clamp(drv: Drv, a: int | None = None, b: int | None = None) -> Drv:
    xk = get_xk(drv)
    pk = get_pk(drv, xk)

    dd = defaultdict(float)

    for x, p in zip(xk, pk):
        if a is not None and x < a:
            dd[a] += p
        elif b is not None and x > b:
            dd[b] += p
        else:
            dd[x] += p

    new_xk = list(dd.keys())
    new_pk = list(dd.values())

    return Drv(values=(new_xk, new_pk))


def constant(x: int) -> Drv:
    return Drv(values=(x, 1.0))


def get_pk(drv: Drv, xk: Xk) -> Pk:
    return drv.pmf(xk)  # noqa Expected type 'ndarray[tuple[Any, ...], dtype[float64]]', got 'float | float64' instead


def get_xk(drv: Drv) -> Xk:
    if drv.a is None or drv.b is None:
        raise ValueError
    return arange(drv.a, drv.b + 1, dtype=int64)


def negative(drv: Drv) -> Drv:
    xk = get_xk(drv)
    pk = get_pk(drv, xk)
    return Drv(a=-drv.b, values=(np_negative(xk), pk))


def sub(lhs: Drv, rhs: Drv) -> Drv:
    return add(lhs, negative(rhs))


def uniform(a: int, b: int) -> Drv:
    xk = arange(a, b + 1, dtype=int64)
    pk = full(xk.shape, 1 / xk.size)
    return Drv(values=(xk, pk))
