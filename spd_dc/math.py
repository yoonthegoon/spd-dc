from collections import defaultdict
from math import sqrt
from typing import Self


class Pmf(defaultdict[int, float]):
    """Probability Mass Function"""

    def __init__(self, *args) -> None:
        super().__init__(float)
        if args:
            self.update(*args)
        self.normalize()

    def __repr__(self) -> str:
        cmf = defaultdict(float)
        acc = 0
        for x, p in sorted(self.items()):
            acc += p
            cmf[x] += acc

        def percentiles(percentiles: list[float], tolerance: float = 1e-9) -> list[int]:
            result = []
            percentiles = sorted(percentiles)
            for x, c in sorted(cmf.items()):
                if c >= percentiles[0] - tolerance:
                    result.append(x)
                    percentiles.pop(0)
                if len(percentiles) == 0:
                    break
            return result

        q1, median, q3 = percentiles([0.25, 0.5, 0.75])
        return f"{self.__class__.__name__}(min={self.min}, q1={q1}, median={median}, q3={q3}, max={self.max})"

    def __add__(self, other: "Pmf") -> "Pmf":
        if not isinstance(other, Pmf):
            raise TypeError(
                f"unsupported operand type(s) for +: 'Pmf' and '{type(other)}'"
            )
        if not (self.is_normal and other.is_normal):
            self.normalize()
            other.normalize()
            # raise ValueError("cannot add non-normal distributions")

        result = Pmf()

        for x, px in self.items():
            for y, py in reversed(other.items()):
                result[x + y] += px * py

        return result.normalize()

    def __sub__(self, other: "Pmf") -> "Pmf":
        if not isinstance(other, Pmf):
            raise TypeError(
                f"unsupported operand type(s) for -: 'Pmf' and '{type(other)}'"
            )
        if not (self.is_normal and other.is_normal):
            self.normalize()
            other.normalize()
            # raise ValueError("cannot subtract non-normal distributions")

        result = Pmf()

        for x, px in self.items():
            for y, py in reversed(other.items()):
                result[x - y] += px * py

        return result.normalize()

    def __mul__(self, other: float) -> "Pmf":
        if not isinstance(other, float):
            raise TypeError(
                f"unsupported operand type(s) for *: 'Pmf' and '{type(other)}'"
            )

        result = self.copy()

        for x in result:
            result[x] *= other

        return result

    def clamped(self, a: int | None = None, b: int | None = None) -> "Pmf":
        result = self.copy()
        for x, p in self.items():
            if a is not None and x < a:
                result[a] += p
                del result[x]
            elif b is not None and x > b:
                result[b] += p
                del result[x]
        return result

    def copy(self) -> "Pmf":
        return type(self)(self)

    def normalize(self) -> Self:
        total = self.total
        for x in self:
            self[x] /= total
        # if not self.is_normal:
        #     try:
        #         return self.normalize()
        #     except RecursionError:
        #         return self
        return self

    @property
    def is_normal(self) -> bool:
        return True if self.total == 1.0 else False

    @property
    def max(self) -> int:
        return max(self)

    @property
    def mean(self) -> float:
        return sum(x * p for x, p in self.items())

    @property
    def min(self) -> int:
        return min(self)

    @property
    def std_dev(self) -> float:
        return sqrt(self.variance)

    @property
    def total(self) -> float:
        return sum(self.values())

    @property
    def variance(self) -> float:
        total = self.total
        mean = self.mean
        return sum(p * (x - mean) ** 2 for x, p in self.items())


class Dud(Pmf):
    """Discrete Uniform Distribution"""

    def __init__(self, a: int, b: int) -> None:
        super().__init__({x: 1 for x in range(a, b + 1)})

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(a={self.min}, b={self.max})"
