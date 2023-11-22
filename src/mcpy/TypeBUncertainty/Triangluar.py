from mcpy import Uncertainty
from mcpy.BaseType.MCSamples import MCSamples
from mcpy.UncertaintyTypes.TypeBUncertainty import TypeBUncertainty


class Triangular(Uncertainty):
    def __init__(self, value: float, hlim: float, *args, **kwargs):
        super().__init__(value, *args, **kwargs)
        self._mcsamples = None
        self._hlim = hlim  # Halfwidth of Limits
        self._a = float(self) - self.hlim
        self._b = float(self) + self.hlim
        self._ustd = self._calc_ustd(self.a, self.b)
        self._uexp = self._calc_uexp(self._ustd)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def hlim(self):
        return self._hlim

    def _calc_ustd(self, a: float, b: float):
        """
            Calculation of the standard uncertainty according to
            GUM Supplement 1 (JCGM 101:2008), section 6.4.5.3, p. 23
            for a trapezoidal distribution
        """
        return ((b - a) ** 2 / 24)

    def mc_sample(self, N) -> MCSamples:
        if self._mcsamples is None:
            self._mcsamples = MCSamples(self.rand_trap(N, self.a, self.b, 0))
        return self._mcsamples

    def to_dict(self) -> dict:
        tup = super().to_dict()
        tup = {**tup, **{'hlim': self.hlim}}
        return tup

    def __str__(self):
        st = f"Triangular({self.a:.2E}, {self.b:.2E}) [ustd = {self.ustd:.2E}, uexp({self.coverage}) = {self.uexp:.2E}]"

        if self.definition is None or self.definition == "":
            return st
        else:
            return f"{self.definition} = {st}"

if __name__ == "__main__":
    R1 = 100
    a1 = 5e-3
    R1_l = R1 - a1
    R1_u = R1 + a1

    trapez = Triangular(R1, a1)
    print(trapez)