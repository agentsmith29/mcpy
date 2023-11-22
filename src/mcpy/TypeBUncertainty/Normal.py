import logging
import math
import numpy as np


from mcpy.BaseType.MCSamples import MCSamples
from mcpy.BaseType.UIBaseClass import UIBase
from mcpy.BaseType.UncertaintyDistributions import Uncertainty


class Normal(Uncertainty):

    def __init__(self, value: float, uexp: float, coverage: float = None, k: float = None, *args, **kwargs):
        super().__init__(value, coverage=coverage, k=k, *args, **kwargs)
        self.type = self.TYPE_B
        self.distribution = self.NORMAL

        self._uexp = uexp  # Expanded uncertainty
        self._ustd = self._calc_ustd(self._uexp)
        self._std = self._ustd

        self._ui = NormalUI(self)

    @property
    def ui(self) -> UIBase:
        return self._ui

    @property
    def std(self):
        return self._std

    def mc_sample(self, N=None) -> MCSamples:
        if self._mcsamples is None:
            self._mcsamples = MCSamples(self.rand_n(N, float(self), self.std), k=self.k)
        return self._mcsamples

    def _calc_ustd(self, expanded_uncertainty: float):
        """
            Calculation of the standard uncertainty according to
            GUM Supplement 1 (JCGM 101:2008), section 6.4.9, p. 25, Formular (13).
            for a Student-t distribution made from observations
        """
        return expanded_uncertainty / self.k

    def to_dict(self) -> dict:
        tup = super().to_dict()
        tup = {**tup, **{'uexp': self.uexp, 'coverage': self.coverage}}
        return tup

    def __str__(self):
        st = f"Normal({float(self):.2E}, {self.std:.2E}) [ustd = {self.ustd:.2E}, uexp({self.coverage:.3E}) = {self.uexp:.3E}]"
        if self.definition is None or self.definition == "":
            return st
        else:
            return f"{self.definition} = {st}]"



class NormalUI(UIBase):
    def __init__(self, parent: Normal, logger=None):
        if logger is None:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logger

        super().__init__(parent, self.logger)

        self.value = self.parent.value
        self.std = self.parent.std

    # ==================================================================================================================
    # UI Element Functions
    # ==================================================================================================================
    def _plot_points(self):
        x = np.linspace(self.value - 3 * self.std, self.value + 3 * self.std, 1000)
        y = (1 / (self.std * math.sqrt(2 * math.pi))) * np.exp(-0.5 * ((x - self.value) / self.std) ** 2)
        # Norm y to 1
        y = y / np.max(y)
        return x, y

    def _set_axis(self, ax):

        # Adapt the axis text, so it just shows the mean and the standard deviation
        ax.set_xticks([self.value - self.parent.k * self.std,
                       self.value - self.std,
                       self.value,
                       self.value + self.std,
                       self.value + self.parent.k * self.std])

        ax.set_xticklabels([f'{self.parent.k * self.std:.2E}',
                            f'{ self.std:.2E}',
                            0,
                            f'{self.std:.2E}',
                            f'{self.parent.k * self.std:.2E}'], fontsize=8)
        ax.text(1, -0.12, "+%g" % self.value, transform=ax.transAxes, horizontalalignment='right', fontsize=9)

    def _show_confidence_interval(self, ax):
        ax.axvline(self.value - self.std, color='red', linestyle='--')
        ax.axvline(self.value + self.std, color='red', linestyle='--')
        ax.text(self.value - self.std, 1, f' $\sigma$', color='red')

        ax.axvline(self.value - self.parent.k * self.std, color='orange')
        ax.axvline(self.value + self.parent.k * self.std, color='orange')
        ax.text(self.value - self.parent.k * self.std, 1, f' {self.parent.coverage * 100:.0f}% CI', color='orange')

    def _set_labels(self, ax):
        ax.set_xlabel('X')
        ax.set_ylabel('Probability Density')
        ax.set_title(f'Normal: $\mu$={self.value}, $\sigma$={self.std:.2E}')

    def generate_ui(self):
        print("Generating UI")
        # Import the necessary widgets
        from PySide6 import QtWidgets, QtCore
        # Create a new grid layout
        layout = QtWidgets.QGridLayout()

        # Create a label textfield buddy
        lbl_value = QtWidgets.QLabel(f"Value [{self.parent.unit}]")
        txt_value = QtWidgets.QLineEdit(f"{self.value}")
        lbl_value.setBuddy(txt_value)
        # Add to the layout
        layout.addWidget(lbl_value, 0, 0)
        layout.addWidget(txt_value, 0, 1, 1, 3)

        lbl_std = QtWidgets.QLabel(f"Standard Deviation [{self.parent.unit}]")
        txt_std = QtWidgets.QLineEdit(f"{self.std:.2E}")
        lbl_std.setBuddy(txt_std)
        layout.addWidget(lbl_std, 1, 0)
        layout.addWidget(txt_std, 1, 1, 1, 3)

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
        txt_uexp = QtWidgets.QLineEdit(f"{self.parent.uexp}")
        lbl_uexp.setBuddy(txt_uexp)
        layout.addWidget(lbl_uexp, 5, 0)
        layout.addWidget(txt_uexp, 5, 1, 1, 3)
        print(f"UI generated {layout}")
        return layout


if __name__ == "__main__":
    uexp = ((40e-3 * 19e-3) / 100)
    normal = Normal(6.7e-3, uexp, 3)
    print(normal)
