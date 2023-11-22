import logging
import math

import numpy as np
import pandas as pd
from numpy import ndarray

import mcpy
from mcpy.BaseType.MCSamples import MCSamples
from mcpy.BaseType.UIBaseClass import UIBase
from mcpy.userinterface.DataFrameViewer import DataFrameViewer


class DirectObservations(mcpy.Uncertainty):

    def __init__(self, observations: ndarray, method: str = "Direct", unc_eval: str = "Experimental",
                 **kwargs):
        arg_value = float(np.mean(observations))
        super().__init__(arg_value, **kwargs)
        self.type = self.TYPE_A
        self.distribution = self.DIRECT_OBSERVATION

        self._observations = observations
        self._n = len(self._observations)
        self._method = method
        self._unc_eval = unc_eval

        self._std = float(np.std(self._observations, ddof=1))
        self._ustd = self._calc_ustd(self.std)
        self._uexp = self._calc_uexp(self._ustd)

        self._ui: UIBase = DirectObservationsUI(self)

    @property
    def n(self):
        return self._n

    @property
    def method(self):
        return self._method

    @property
    def unc_eval(self):
        return self._unc_eval

    @property
    def std(self):
        return self._std

    @property
    def coverage(self):
        return self._coverage

    @coverage.setter
    def coverage(self, value):
        self._coverage = value

    def _calc_ustd(self, standard_deviation: float):
        """
            Calculation of the standard uncertainty according to
            GUM Supplement 1 (JCGM 101:2008), section 6.4.9, p. 25, Formular (13).
            for a Student-t distribution made from observations
        """
        return np.sqrt((self._n - 1) / (self._n - 3)) * standard_deviation / np.sqrt(self._n)

    def as_dataframe(self):
        return pd.DataFrame(data={
            'Definition': self.definition,
            'Value': self.vnom,
            'Standard Deviation': self.std,
            'Standard Uncertainty': self.ustd,
            'Expanded Uncertainty': self.uexp,
            "Distribution": "Student-t"
        }, index=[0])

    def mc_sample(self, N):
        """
        Generate N samples for a MC analysis
        """
        if self._mcsamples is None:
            self._mcsamples = MCSamples(self.rand_t(N, self.n, float(self), self.std))
        return self._mcsamples

    def to_dict(self) -> tuple:
        tup = self._get_params()
        tup = {**tup, **{'observations': self.observations, 'method': self.method, 'unc_eval': self.unc_eval}}
        return (self.__class__.__name__, tup)

    def __str__(self):
        st = f"Obs({float(self):.2E}, {self.std:.2E}) [ustd = {self.ustd:.2E}, uexp({self.coverage}) = {self.uexp:.2E}]"

        if self.definition is None or self.definition == "":
            return st
        else:
            return f"{self.definition} = {st}"

    def __repr__(self):
        return str(self)


class DirectObservationsUI(UIBase):
    def __init__(self, parent: DirectObservations, logger=None):
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
        return x, y

    def _set_axis(self, ax):
        # Adapt the axis text, so it just shows the mean and the standard deviation
        ax.set_xticks([self.value - self.parent.k * self.std,
                       self.value - self.std,
                       self.value,
                       self.value + self.std,
                       self.value + self.parent.k * self.std])

        ax.set_xticklabels([f'{self.value - self.parent.k * self.std:.2E}',
                            f'{self.value - self.std:.2E}',
                            f'{self.value:.2E}',
                            f'{self.value + self.std:.2E}',
                            f'{self.value + self.parent.k * self.std:.2E}'], fontsize=8)

    def _show_confidence_interval(self, ax):
        ax.axvline(self.value - self.std, color='red', linestyle='--')
        ax.axvline(self.value + self.std, color='red', linestyle='--')

        ax.axvline(self.value - self.parent.k * self.std, color='orange')
        ax.axvline(self.value + self.parent.k * self.std, color='orange')
        # Add a text to the plot
        ax.text(self.value - self.parent.k * self.std, 0.1, f' {self.parent.coverage * 100:.0f}% CI', color='red')

    def _set_labels(self, ax):
        ax.set_xlabel('$x$')
        ax.set_ylabel('Probability Density (PDF)')
        ax.set_title(f'Normal: $\mu$={self.value:.5E}, $\sigma$={self.std:.3E}', fontsize=10)


    def generate_ui(self):
        print("Generating UI")
        # import the necessary widgets
        from PySide6 import QtWidgets, QtCore
        # Create a new grid layout
        layout = QtWidgets.QGridLayout()

        lbl_num_of_obs = QtWidgets.QLabel("Number of Observations")
        txt_num_of_obs = QtWidgets.QLineEdit(str(self.parent.n))
        lbl_num_of_obs.setBuddy(txt_num_of_obs)
        layout.addWidget(lbl_num_of_obs, 0, 0)
        layout.addWidget(txt_num_of_obs, 0, 1, 1, 2)
        btn_data = QtWidgets.QPushButton("Data")
        layout.addWidget(btn_data, 0, 3)

        self.obs_viewer = DataFrameViewer(self.parent._observations)
        btn_data.clicked.connect(self.obs_viewer.show)

        # Add a line in between
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        layout.addWidget(line, 1, 0, 1, 4)

        # Create a label textfield buddy
        lbl_value = QtWidgets.QLabel(f"Value [{self.parent.unit}]")
        txt_value = QtWidgets.QLineEdit(str(self.value))
        lbl_value.setBuddy(txt_value)

        # Add to the layout
        layout.addWidget(lbl_value, 2, 0)
        layout.addWidget(txt_value, 2, 1, 1, 3)

        lbl_std = QtWidgets.QLabel(f"Standard Deviation [{self.parent.unit}]")
        txt_std = QtWidgets.QLineEdit(f"{self.std:.2E}")
        lbl_std.setBuddy(txt_std)
        layout.addWidget(lbl_std, 3, 0)
        layout.addWidget(txt_std, 3, 1, 1, 3)

        lbl_usd = QtWidgets.QLabel(f"Standard Uncertainty [{self.parent.unit}]")
        txt_usd = QtWidgets.QLineEdit(f"{self.parent.ustd:.2E}")
        lbl_usd.setBuddy(txt_usd)
        layout.addWidget(lbl_usd, 4, 0)
        layout.addWidget(txt_usd, 4, 1, 1, 3)

        # Add a line in between
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        layout.addWidget(line, 5, 0, 1, 4)

        lbl_coverage = QtWidgets.QLabel("Coverage [%]")
        txt_coverage = QtWidgets.QLineEdit(f"{self.parent.coverage * 100:.2f}")
        lbl_coverage.setBuddy(txt_coverage)
        lbl_k = QtWidgets.QLabel("Coverage Factor")
        txt_k = QtWidgets.QLineEdit(str(self.parent.k))
        lbl_k.setBuddy(txt_k)
        layout.addWidget(lbl_coverage, 6, 0)
        layout.addWidget(txt_coverage, 6, 1)
        layout.addWidget(lbl_k, 6, 2)
        layout.addWidget(txt_k, 6, 3)

        lbl_uexp = QtWidgets.QLabel("Expanded Uncertainty")
        txt_uexp = QtWidgets.QLineEdit(f"{self.parent.uexp:.2E}")
        lbl_uexp.setBuddy(txt_uexp)
        layout.addWidget(lbl_uexp, 7, 0)
        layout.addWidget(txt_uexp, 7, 1, 1, 3)

        print(f"UI generated {layout}")
        return layout

if __name__ == "__main__":
    obs = [1, 2, 3, 4, 5, 6]
    from_obs = DirectObservations(obs)

    print(from_obs)
