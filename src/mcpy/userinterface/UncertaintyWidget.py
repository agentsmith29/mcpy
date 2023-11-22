from PySide6.QtWidgets import QWidget, QGridLayout, QTextEdit

from mcpy import Uncertainty
from mcpy.userinterface.MCMWidget import MonteCarloWidget
from mcpy.userinterface.Ui_UncertaintyControlWidget import Ui_UncertaintyControlWidget


class UncertaintyWidget(QWidget):
    # Init the UI file
    def __init__(self, uncertainty: Uncertainty = None, parent=None, logger=None):
        super().__init__()
        self._ui = Ui_UncertaintyControlWidget()
        self._ui.setupUi(self)

        if uncertainty is not None:
            self._uncertainty = uncertainty
            self._update_ui()

        self.mcm_window = MonteCarloWidget()



    def _update_ui(self):
        self.layout: QGridLayout = self.uncertainty.ui.generate_ui()

        self._ui.grd_unc_info.addLayout(self.layout)
        self._ui.cb_distribution.addItems(self.uncertainty.LIST_TYPE_B)
        self._ui.cb_distribution.setCurrentText(self.uncertainty.distribution)
        self._ui.cb_type.addItems(self.uncertainty.LIST_TYPE)
        self._ui.cb_type.setCurrentText(self.uncertainty.type)

        self._ui.text_unit.setText(self.uncertainty.unit)
        self._ui.txt_definition.setText(self.uncertainty.definition)
        self._ui.text_description.setPlainText(self.uncertainty.description)

        self._ui.grd_plot_area.addLayout(self.uncertainty.ui.generate_plot(), 0, 0)
        self._ui.tabWidget.setCurrentIndex(0)

        self._ui.btn_open_mcm.clicked.connect(self._on_open_mcm_clicked)
        # .setLayout(self.layout)

    def _on_open_mcm_clicked(self):
        self.mcm_window.mc_samples = self.uncertainty.mc_sample()
        self.mcm_window.show()

    @property
    def uncertainty(self):
        return self._uncertainty

    @uncertainty.setter
    def uncertainty(self, value):
        self._uncertainty = value
        self._update_ui()
