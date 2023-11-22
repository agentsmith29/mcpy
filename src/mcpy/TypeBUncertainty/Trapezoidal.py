from mcpy import Uncertainty
from mcpy.BaseType.MCSamples import MCSamples


class Trapezoidal(Uncertainty):
    def __init__(self, value: float, hlim: float, d: float, *args, **kwargs):
        """
            Defines a trapezoidal distribution where an input value is distributed equally over a certain range.
            Arguments:
                vnom (float): Input Value
                hlim (float): The half span between limits (a, b) of the variability of the quantity
                (Halfwidth of Limits field)
                sfac (float): The shape factor beta (0 to 1) determines the width of the section over which the
                distribution is even, compared to the total width. All distributions between rectangular (b = 1)
                and triangular distribution (b = 0) are possible
            Keyword Arguemtns:
                definition (str):
                unit (str):
                description (str):
        """
        super().__init__(value, *args, **kwargs)
        self._hlim = hlim  # Halfwidth of Limits
        self._a = float(self) - self.hlim
        self._b = float(self) + self.hlim
        if 0 <= d <= 1:
            self._d = d  # Shapefactor
        else:
            raise ValueError(f"The shapefactor (beta) must be between 0 and 1 (given {d}).")
        self._ustd = self._calc_ustd(float(self), self.hlim)
        self._uexp = self._calc_uexp(self._ustd)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = value


    @property
    def hlim(self):
        return self._hlim

    @hlim.setter
    def hlim(self, value):
        self._hlim = value

    def _calc_ustd(self, a: float, b: float):
        """
            Calculation of the standard uncertainty according to
            GUM Supplement 1 (JCGM 101:2008), section 6.4.4, p. 22
            for a trapezoidal distribution
        """
        return ((b - a) ** 2 / 24) * (1 + self.d ** 2)

    def mc_sample(self, N) -> MCSamples:
        if self._mcsamples is None:
            self._mcsamples = MCSamples(self.rand_trap(N, self.a, self.b, self.d))
        return self._mcsamples

    def to_dict(self) -> dict:
        tup = super().to_dict()
        tup = {**tup, **{'hlim': self.hlim, 'd': self.d}}
        return tup

    def __str__(self):
        st = f"Trap({self.a:.2E}, {self.b:.2E}, {self.d:.3E}) [ustd = {self.ustd:.2E}, uexp({self.coverage}) = {self.uexp:.2E}]"

        if self.definition is None or self.definition == "":
            return st
        else:
            return f"{self.definition} = {st}"

if __name__ == "__main__":
    R1 = 100
    a1 = 5e-3
    R1_l = R1 - a1
    R1_u = R1 + a1

    trapez = Trapezoidal(R1, a1, 0.8)
    print(trapez)