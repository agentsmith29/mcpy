from abc import ABC

import numpy as np
from numpy import ndarray

from mcpy import Uncertainty


class TypeAUncertainty(Uncertainty, ABC):
    def __init__(self, observations: ndarray, *args, **kwargs):
        self._observations: ndarray = observations
        self._n = len(self._observations)
        self._vnom = float(np.mean(self._observations))
        super().__init__(vnom=self._vnom, *args, **kwargs)

    @property
    def observations(self):
        return self._observations

    @property
    def n(self):
        return self._n
