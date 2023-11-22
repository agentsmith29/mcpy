import logging
import sqlite3
from abc import abstractmethod
from typing import Dict, Any

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.arrays import ExtensionScalarOpsMixin, ExtensionArray
from pandas.core.dtypes.base import register_extension_dtype, ExtensionDtype
from pandas.core.dtypes.dtypes import PandasExtensionDtype
from scipy.stats import norm


#import mcpy
from mcpy.BaseType.UIBaseClass import UIBase


class Uncertainty:
    NORMAL = "Normal"
    RECTANGULAR = "Rectangular"
    TRIANGULAR = "Triangular"
    UNIFORM = "Uniform"
    DIRECT_OBSERVATION = "Direct Observation"

    TYPE_A = "Type A"
    TYPE_B = "Type B"


    NONE = "None"

    LIST_TYPE_B = [NORMAL, RECTANGULAR, TRIANGULAR, UNIFORM, NONE]
    LIST_TYPE = [TYPE_A, TYPE_B]

    def __init__(self, value: float,
                 coverage: float = None, k: float = None,
                 unit: str = "1", definition: str = None, description: str = None, ustd: float = 0,
                 *args, **kwargs):

        self.logger = logging.getLogger(__name__)

        self.type = self.NONE
        self.distribution = self.NONE

        # self.__new__(value)
        self._value = value
        self._unit = unit
        self._definition = definition
        self._description = description

        if coverage is None and k is not None:
            self._k = k
            self._coverage = 1-norm.pdf(k)
        elif coverage is not None and k is None:
            self._coverage = coverage
            self._k = norm.ppf(self._coverage)
        elif coverage is None and k is None:
            self.logger.warning(f"No coverage or k value was given. Using default coverage of 0.95. k = {k}")
            self._coverage = 0.95
            self._k = norm.ppf(self._coverage)

        self._ustd = ustd
        self._uexp = self._calc_uexp(self._ustd)

        self._mcsamples = None
        # return obj

        self._ui = UIBase(self, self.logger)

    @property
    def ui(self) -> UIBase:
        return self._ui
    # ==================================================================================================================
    # Properties
    # ==================================================================================================================
    @property
    def value(self):
        return self._value

    @property
    def coverage(self):
        return self._coverage

    @property
    def k(self):
        return self._k

    @property
    def unit(self):
        return self._unit

    @property
    def ustd(self):
        if self._ustd is None:
            raise NotImplementedError("The standard uncertainty has not been implemented!")
        return self._ustd

    @property
    def uexp(self):
        if self._uexp is None:
            raise NotImplementedError("The expanded uncertainty has not been implemented!")
        return self._uexp

    # ==================================================================================================================
    # Properties & Setters
    # ==================================================================================================================
    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, value):
        self._definition = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    # ==================================================================================================================
    # Calculations
    # ==================================================================================================================
    def _calc_uexp(self, standard_uncertainty):
        """
            Calculation of the expanded uncertainty according to
            GUM
        """
        if standard_uncertainty is None:
            return None
        return self.k * standard_uncertainty

    def _calc_std(self, *args, **kwargs):
        raise NotImplementedError

    # ==================================================================================================================
    # Uncertainty distribution functions
    # ==================================================================================================================
    def rand_t(self, N, n, mu, sigma):
        """
            Draw samples from a standard Student's t distribution with `n-1` degrees
            of freedom for mean of n measurements of variable
            distributed normally with expectation `std` and standard deviation
            `sigma`.
            @arg N: Number of samples to draw
            @arg n: Number of measurement samples (degrees of freedom = n-1)
            @arg mu: expectation
            @arg sigma: standard deviation
            @return probability distribution
        """
        nu = n - 1
        return mu + np.random.standard_t(nu, N) * (sigma / np.sqrt(n))

    def rand_n(self, N, mu, sigma):
        """
            Normally distributed samples with expectation `mu` and standard
            deviation `sigma`.
            @arg N: Number of samples to draw
            @arg mu: expectation
            @arg sigma: standard deviation
            @return probability distribution
        """
        return mu + np.random.standard_normal(N) * sigma

    def rand_r(self, N, a, b):
        """
            Rectangularly distributed samples in the interval [a,b]
            @arg N: Number of samples to draw
            @arg a: lower bound
            @arg b: upper bound
            @return probability distribution
        """
        return a + np.random.random(N) * (b - a)

    def rand_trap(self, N, a, b, d):
        """
            Rectangularly distributed samples in the interval [a,b]
            @arg N: Number of samples to draw
            @arg a: lower bound
            @arg b: upper bound
            @arg d: upper bound
            @return probability distribution
        """
        return a + ((b - a) / 2) * ((1 + d) * np.random.random(N) + (1 - d) * np.random.random(N))

    # ==================================================================================================================
    #
    # ==================================================================================================================
    def mc_sample(self, N=None):
        if N is None and self._mcsamples is not None:
            return self._mcsamples
        elif N is not None and self._mcsamples is None:
            self._mcsamples = mcpy.MCSamples(np.zeros(N) + float(self))
        else:
            raise ValueError("N is None and no samples have been generated yet!")
        return self._mcsamples

    def _get_params(self) -> dict:
        return {'value': float(self),
                'coverage': self.coverage if self.coverage is not None else "NaN",
                'unit': self.unit if self.unit is not None else "NaN",
                'definition': self.definition if self.definition is not None else "NaN",
                'description': self.description if self.description is not None else "NaN",
                'type': self.type if self.type is not None else "NaN",
                'distribution': self.distribution if self.distribution is not None else "NaN"
                }

    def to_dict(self) -> dict:
        tup = self._get_params()
        if tup is None:
            tup = "NaN"
        tup = {**tup}
        return tup

    @classmethod
    def from_dict(cls, tup):
        if tup['distribution'] == "Normal":
            return mcpy.Normal(**tup)
        elif tup['distribution'] == "StudentT":
            return mcpy.StudentT(**tup)
        elif tup['distribution'] == "Rectangular":
            return mcpy.Rectangular(**tup)
        elif tup['distribution'] == "Triangular":
            return mcpy.Triangular(**tup)
        elif tup['distribution'] == "Trapezoidal":
            return mcpy.Trapezoidal(**tup)
        else:
            raise ValueError(f"Unknown type {tup['type']}!")

    #def generate_ui(self) -> 'QGridLayout':
    #    raise NotImplementedError("The uncertainty UI interface has not been implemented!")

    # ==================================================================================================================
    #
    # ==================================================================================================================
    def __float__(self):
        # return str(self.as_dataframe())
        return float(self.value)

    def __int__(self):
        # return str(self.as_dataframe())
        return int(self.value)

    def __repr__(self):
        # return str(self.as_dataframe())
        #return f"{np.round(self, 3)} +- {np.round(self.uexp, 3)}"
        return str(self)

    def __str__(self):
        # return str(self.as_dataframe())
        return f"{np.round(float(self), 3)} +- {np.round(self.uexp, 3)}"


if __name__ == "__main__":
    # pd.api.extensions.register_extension_dtype(UncertaintyDtype)
    N = 1000000

    R1 = 10
    a1 = 5e-3
    rect1 = mcpy.Rectangular(R1, a1)
    rect2 = mcpy.Triangular(R1, a1)
    result1 = rect1.mc_sample(N) + rect2.mc_sample(N) + mcpy.Uncertainty(2).mc_sample(N)
    result2 = float(rect1) + float(rect2) + 2
    print(result1)
    print(result2)
