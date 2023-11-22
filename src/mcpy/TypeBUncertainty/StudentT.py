import numpy as np
from scipy.stats import norm

from mcpy import Uncertainty


class StudentT(Uncertainty):


    def __init__(self, value: float, uexp: float, df: float, *args, **kwargs):
        super().__init__(value, *args, **kwargs)
        self._uexp = uexp  # Expanded uncertainty
        self._df = df  # Degrees of freedom
        self._ustd = self._calc_ustd(self._uexp)
        self._std = self._ustd * np.sqrt(self.df - 1)

    @property
    def df(self):
        return self._df

    @property
    def std(self):
        return self._std

    def _calc_ustd(self, expanded_uncertainty: float):
        """
            Calculation of the standard uncertainty according to
            GUM Supplement 1 (JCGM 101:2008), section 6.4.9, p. 25, Formular (13).
            for a Student-t distribution made from observations
        """
        return expanded_uncertainty / self.k

        if self._mcsamples is None:
            self._mcsamples = MCSamples(self.rand_t(N, self.df - 1, self.vnom, self.std))
        return self._mcsamples

    def __str__(self):
        st = f"StudentT({self:.2E}, {self.std:.2E}) [ustd = {self.ustd:.2E}, uexp({self.coverage:.3E}) = {self.uexp:.3E}]"
        if self.definition is None or self.definition == "":
            return st
        else:
            return f"{self.definition} = {st}]"

    def to_dict(self) -> dict:
        tup = super().to_dict()
        tup = {**tup, **{'uexp': self.uexp, 'df': self.df}}
        return tup

if __name__ == "__main__":
    uexp = ((40e-3 * 19e-3) / 100)
    df = 24
    studentt = StudentT(6.7e-3, uexp, 24)
    print(studentt)