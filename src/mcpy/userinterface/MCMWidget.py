from PySide6.QtWidgets import QWidget

from mcpy.BaseType import MCSamples
from mcpy.userinterface.Ui_MCControlWidget import Ui_MCControlWindow


class MonteCarloWidget(QWidget):
    # Init the UI file
    def __init__(self, mc_samples: MCSamples = None, parent=None, logger=None):
        super().__init__()
        self._ui = Ui_MCControlWindow()
        self._ui.setupUi(self)
        self._mc_samples: MCSamples = None

        if mc_samples is not None:
            self.mc_samples: MCSamples = mc_samples
            self._update_ui()
        else:
            self._ui.text_samples_n.setText("No MCM sampled data!")

    @property
    def mc_samples(self) -> MCSamples:
        return self._mc_samples

    @mc_samples.setter
    def mc_samples(self, value: MCSamples):
        self._mc_samples = value
        self._update_ui()

    def _update_ui(self):
        self._ui.text_samples_n.setText(f"{self.mc_samples.N}")
        self._ui.txt_mean.setText(f"{self.mc_samples.mean:.3E}")
        self._ui.txt_std.setText(f"{self.mc_samples.std:.3E}")
        self._ui.txt_cov.setText(f"{self.mc_samples.coverage*100:.3f}%")
        self._ui.txt_cov_factor.setText(f"{self.mc_samples.k}")
        self._ui.txt_unit.setText(f"{self.mc_samples.unit}")

        self._ui.grd_plot_area.addLayout(self.mc_samples.plot(), 0, 0)
