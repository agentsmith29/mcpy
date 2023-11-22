import logging

import numpy as np

from mcpy import Uncertainty
from mcpy.BaseType.MCSamples import MCSamples
from mcpy.BaseType.UIBaseClass import UIBase


class Rectangular(Uncertainty):

    def __init__(self, value: float, hlim: float, *args, **kwargs):
        """
            Defines a rectangular distribution where an input value is distributed equally over a certain range.
            Arguments:
                vnom (float): Input Value
                hlim (float): The half span between limits (a, b) of the variability of the quantity
                (Halfwidth of Limits field)
            Keyword Arguemtns:
                definition (str):
                unit (str):
                description (str):
        """
        super().__init__(value, *args, **kwargs)
        self.type = self.TYPE_B
        self.distribution = self.RECTANGULAR

        self._hlim = hlim  # Halfwidth of Limits
        self._a = float(self) - self.hlim
        self._b = float(self) + self.hlim
        self._ustd = self._calc_ustd(self._hlim)
        self._uexp = self._calc_uexp(self._ustd)

        self._ui = RectangularUI(self, self.logger)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def hlim(self):
        return self._hlim

    def _calc_ustd(self, hlim: float):
        """
            Calculation of the standard uncertainty according to
            GUM Supplement 1 (JCGM 101:2008), section 6.4.2, p. 19
            for a rectangular distribution
        """
        return hlim / np.sqrt(3)

    def mc_sample(self, N=None) -> MCSamples:
        print(f"Generating {N} samples for {self}")
        if self._mcsamples is None:
            self._mcsamples = MCSamples(self.rand_r(N, self.a, self.b), k=self.k)
        return self._mcsamples

    def to_dict(self) -> dict:
        tup = super().to_dict()
        tup = {**tup, **{'hlim': self.hlim, 'a': self.a, 'b': self.b}}
        return tup

    def generate_plot(self):
        print("Generating Plot")

        # import the necessary widgets
        from PySide6.QtWidgets import QVBoxLayout
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib import pyplot as plt

        layout = QVBoxLayout()

        figure = plt.figure()
        canvas = FigureCanvas(figure)
        layout.addWidget(canvas)

        # Clear the existing plot and plot the new data
        figure.clear()
        ax = figure.add_subplot(111)
        a = self.a
        b = self.b
        # Add vertical lines
        ax.plot([a, a], [0, 1 / (b - a)], 'r')
        ax.plot([b, b], [0, 1 / (b - a)], 'r')

        # Add horizontal line
        ax.plot([a, b], [0, 1 / (self.parent.b - self.parent.a)], 'r')
        # Draw vertical lines at a and b
        # ax.axvline(self.a, color='r', linestyle='--', label='Lower Bound (a)')
        # ax.axvline(self.b, color='g', linestyle='--', label='Upper Bound (b)')

        ax.set_xlabel('X')
        ax.set_ylabel('Probability Density')
        ax.set_title(f'Rectangular')
        canvas.draw()

        return layout

    def __str__(self):
        st = f"Rect({self.a:.2E}, {self.b:.2E}) [ustd = {self.ustd:.2E}, uexp({self.coverage}) = {self.uexp:.2E}]"

        if self.definition is None or self.definition == "":
            return st
        else:
            return f"{self.definition} = {st}"



class RectangularUI(UIBase):
    def __init__(self, parent: Rectangular, logger=None):
        if logger is None:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logger

        super().__init__(parent, self.logger)

    # ==================================================================================================================
    # UI Element Functions
    # ==================================================================================================================
    def _plot_points(self):
        # Generate data points for the rectangular distribution
        # plot a rectangle with height h and width a but leave the bottom side open
        x = [self.parent.value - self.parent.hlim * 1.5, self.parent.value - self.parent.hlim,
             self.parent.value - self.parent.hlim,
             self.parent.value + self.parent.hlim, self.parent.value + self.parent.hlim,
             self.parent.value + self.parent.hlim * 1.5]
        y = [0, 0, 1, 1, 0, 0]
        # Concat the data points
        return x, y

    def _set_axis(self, ax):
        pass
        # # Adapt the axis text, so it just shows the mean and the standard deviation
        # ax.set_xticks([self.value - self.parent.k * self.std,
        #                self.value - self.std,
        #                self.value,
        #                self.value + self.std,
        #                self.value + self.parent.k * self.std])
        #
        # ax.set_xticklabels([f'{self.parent.k * self.std:.2E}',
        #                     f'{ self.std:.2E}',
        #                     0,
        #                     f'{self.std:.2E}',
        #                     f'{self.parent.k * self.std:.2E}'], fontsize=8)
        # ax.text(1, -0.12, "+%g" % self.value, transform=ax.transAxes, horizontalalignment='right', fontsize=9)

    def _show_confidence_interval(self, ax):
        pass
        ax.axvline(self.parent.value, color='red', linestyle='--')
        ax.text(self.parent.value, 0.9, f' $\mu$', color='red')
        # Draw an arrow between the mean and the confidence interval
        ax.annotate("", xy=(self.parent.value - self.parent.hlim, 0.5), xytext=(self.parent.value, 0.5),
                    arrowprops=dict(arrowstyle="<->", color='orange'))
        # Add a text
        ax.text(self.parent.value - self.parent.hlim / 2, 0.45, f' $a$', color='orange', horizontalalignment='center')

    def _set_labels(self, ax):
        ax.set_xlabel('$x$')
        ax.set_ylabel('Probability Density ($PDF$)')
        ax.set_title(f'Rectangular: $\mu$ = {self.parent.value}, $a$={self.parent.a}')

    def generate_ui(self):
        print("Generating UI")
        # Import the necessary widgets
        from PySide6 import QtWidgets
        # Create a new grid layout
        layout = QtWidgets.QGridLayout()

        # Create a label textfield buddy
        lbl_value = QtWidgets.QLabel(f"Value [{self.parent.unit}]")
        txt_value = QtWidgets.QLineEdit(f"{self.parent.value}")
        lbl_value.setBuddy(txt_value)
        # Add to the layout
        layout.addWidget(lbl_value, 0, 0)
        layout.addWidget(txt_value, 0, 1, 1, 3)

        lbl_hlim = QtWidgets.QLabel(f"Halfwidth of Limits [{self.parent.unit}]")
        txt_hlim = QtWidgets.QLineEdit(f"{self.parent.hlim:.2E}")
        lbl_hlim.setBuddy(txt_hlim)
        layout.addWidget(lbl_hlim, 1, 0)
        layout.addWidget(txt_hlim, 1, 1)

        lbl_limits = QtWidgets.QLabel(f"Limits  [{self.parent.unit}]")
        txt_limits = QtWidgets.QLineEdit(f"({self.parent.a:.2f}, {self.parent.b:.2f})")
        lbl_limits.setBuddy(txt_limits)
        layout.addWidget(lbl_limits, 1, 2)
        layout.addWidget(txt_limits, 1, 3)

        lbl_usd = QtWidgets.QLabel(f"Standard Uncertainty [{self.parent.unit}]")
        txt_usd = QtWidgets.QLineEdit(f"{self.parent.ustd:.2E}")
        lbl_usd.setBuddy(txt_usd)
        layout.addWidget(lbl_usd, 2, 0)
        layout.addWidget(txt_usd, 2, 1, 1, 3)

        # Add a line in between
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        layout.addWidget(line, 3, 0, 1, 4)

        lbl_coverage = QtWidgets.QLabel("Coverage [%]")
        txt_coverage = QtWidgets.QLineEdit(f"{self.parent.coverage * 100:.2f}")
        lbl_coverage.setBuddy(txt_coverage)
        lbl_k = QtWidgets.QLabel("Coverage Factor")
        txt_k = QtWidgets.QLineEdit(f"{self.parent.k}")
        lbl_k.setBuddy(txt_k)
        layout.addWidget(lbl_coverage, 4, 0)
        layout.addWidget(txt_coverage, 4, 1)
        layout.addWidget(lbl_k, 4, 2)
        layout.addWidget(txt_k, 4, 3)

        lbl_uexp = QtWidgets.QLabel("Expanded Uncertainty")
        txt_uexp = QtWidgets.QLineEdit(f"{self.parent.uexp:.2E}")
        lbl_uexp.setBuddy(txt_uexp)
        layout.addWidget(lbl_uexp, 5, 0)
        layout.addWidget(txt_uexp, 5, 1, 1, 3)
        print(f"UI generated {layout}")
        return layout


if __name__ == "__main__":
    R1 = 100
    a1 = 5e-3
    R1_l = R1 - a1
    R1_u = R1 + a1

    rect1 = Rectangular(R1, a1)
    print(rect1)
