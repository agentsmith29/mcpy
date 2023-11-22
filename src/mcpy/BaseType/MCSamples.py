import numpy as np
from scipy.stats import norm
#import mcpy.BaseType.UncertaintyDistributions as ud


class MCSamples(np.ndarray):
    def __new__(cls, input_array,
                coverage: float = None, k: float = None,
                unit: str = "",
                definition: str = None,
                description: str = None):
        obj = np.asarray(input_array).view(cls)
        obj._mean = np.mean(input_array)
        obj._std = np.std(input_array)

        obj._unit = unit
        obj._definition = definition
        obj._description = description
        #
        if coverage is None and k is not None:
            obj._k = k
            obj._coverage = 1 - norm.pdf(k)
        elif coverage is not None and k is None:
            obj._coverage = coverage
            obj._k = norm.ppf(obj._coverage)
        else:
            raise ValueError("Either coverage or k must be specified")

        obj.layout = None
        obj.figure = None
        obj.canvas = None

        return obj

    @property
    def N(self):
        return len(self)

    @property
    def coverage(self):
        return self._coverage

    @coverage.setter
    def coverage(self, value):
        self._coverage = value
        self._k = norm.ppf(self._coverage)

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, value):
        self._k = value
        self._coverage = 1 - norm.pdf(self._k)


    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

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


    def rand(self, N):
       return self

    def plot(self):
        #self.logger.debug("Generating plot for normal distribution")

        try:
            # import the necessary widgets
            from PySide6 import QtWidgets, QtCore
            from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
            from matplotlib.figure import Figure
            from matplotlib import pyplot as plt
            from matplotlib.ticker import ScalarFormatter

        except ImportError as e:
            self.logger.error("Unable to import necessary modules for generating plot")
            raise e
        plt.rcParams.update({'font.size': 8})

        if self.layout is None:
            self.layout = QtWidgets.QVBoxLayout()

        if self.figure is None:
            self.figure = plt.figure(figsize=(3, 10))

        if self.canvas is None:
            self.canvas = FigureCanvas(self.figure)

        self.layout.addWidget(self.canvas)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        #plt.title(self.__class__.__name__)
        ax.hist(np.array(self), bins=100)
        self.canvas.draw()
        return self.layout

    @property
    def std(self):
        return self._std

    @property
    def mean(self):
        return self._mean


    @property
    def uncertainty(self):
        from mcpy.BaseType.UncertaintyDistributions import Uncertainty
        return Uncertainty(
            float(self.mean),
            ustd=float(self.std),
            coverage=self.coverage,
            unit=self.unit,
            definition=self.definition,
            description=self.description
        )

    def __array_finalize__(self, obj):
        if obj is None:
            return
        # self.unit = getattr(obj, 'unit', None)
        # self.definition = getattr(obj, 'definition', None)
        # self.description = getattr(obj, 'description', None)
        # self.coverage = getattr(obj, '_coverage', None)
        # self._mean = getattr(obj, '_mean', None)
        # self._std = getattr(obj, '_std', None)
        # self.k = getattr(obj, '_k', None)
        super().__array_finalize__(obj)

    #def std(self, axis=None, dtype=None, out=None, ddof=0, keepdims=False, *args, **kwargs):
    #   print("std called")
    #    return super().std(axis, dtype, out, ddof, keepdims, *args, **kwargs)

    # def __array_wrap__(self, out_arr, context=None):
    #     # Ensure the output is wrapped as an MCSamples instance
    #     return np.ndarray.__array_wrap__(self, out_arr, context)
    #
    # def __getitem__(self, index):
    #     result = super().__getitem__(index)
    #     if isinstance(result, np.ndarray):
    #         return MCSamples(result, unit=self.unit, definition=self.definition,description=self.description,
    #                          coverage=self.coverage)
    #     return result

    def __add__(self, other):
        if isinstance(other, float):
            result = super().__add__(other)
        else:
            result = np.array(super().__add__(np.array(other)))
        return MCSamples(result, unit=self.unit, definition=self.definition, description=self.description,
                             coverage=self.coverage)

    def __sub__(self, other):
        if isinstance(other, float):
            result = super().__sub__(other)
        else:
            result = np.array(super().__sub__(np.array(other)))
        return MCSamples(result, unit=self.unit, definition=self.definition, description=self.description,
                         coverage=self.coverage)
    #
    def __mul__(self, other):
        if isinstance(other, float):
            result = super().__mul__(other)
        else:
            result = np.array(super().__mul__(np.array(other)))
        return MCSamples(result, unit=self.unit, definition=self.definition, description=self.description,
                         coverage=self.coverage)
    #
    def __truediv__(self, other):
        if isinstance(other, float):
            result = super().__truediv__(other)
        else:
            result = np.array(super().__truediv__(np.array(other)))
        return MCSamples(result, unit=self.unit, definition=self.definition, description=self.description,
                         coverage=self.coverage)

    def __repr__(self):
        #if self.unit is not None:
        #    #return f"MCSamples({super().__repr__()}, unit={self.unit})"
        #else:
        #    return super().__repr__()
        return f"MCSamples"#({self.mean:.3E}, ustd {self.uncertainty.ustd:.3E}, N={len(self)})"

    def __str__(self):
        return f"MCSamples({self.uncertainty.value:.3E}, ustd {self.uncertainty.ustd:.3E}, N={len(self)})"

    def __float__(self) -> float:
        if isinstance(self, MCSamples):
            return float(self.mean)

class MCSamplesUI():
    pass

if __name__ == "__main__":
    np1 = np.array([1, 2, 3, 4, 5])
    R21 = MCSamples([1, 2, 3, 4, 5])
    print(f"R21 : {R21}")
    np2 = np.array([5, 2, 6, 1, 9])
    R22 = MCSamples([5, 2, 6, 1, 9])
    print(f"R22: {R22}")
    R2 = R21 + R22
    print(f"R2: {R2}")
    R2.plot(N)

    RZ = ud.Uncertainty(105e-3)
    print(f"R2: {RZ}")
    # Test adding a MC sample with an distribution
    #R1 = (float(R2) + float(RZ))#
    #R1 = (R2 + RZ)#
    #print(f"R1: {R1}")