import os
import sys
import pathlib
import os
sys.path.append('./src')
print(os.getcwd())

import mcpy

from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication()

    # from_obs = DirectObservations([ 0.20064, 0.2019, 0.19771, 0.20089, 0.20024, 0.19878, 0.19946,
    #         0.20024, 0.2035, 0.20248, 0.19879, 0.20307, 0.20065, 0.20007,
    #         0.20055, 0.19979, 0.19985, 0.20152, 0.20144, 0.20133, 0.20067, 0.19878,
    #         0.20078, 0.20174, 0.2006], k=3)
    # ui = UncertaintyWidget(from_obs)

    # uexp = ((40e-3 * 19e-3) / 100)
    # normal = mcpy.Normal(6.7e-3, uexp, 3)
    # ui = UncertaintyWidget(normal)

    R1 = 100
    a1 = 5e-3
    R1_l = R1 - a1
    R1_u = R1 + a1
    rect1 = mcpy.Rectangular(R1, a1, k=2)
    rect1.mc_sample(200000)
    ui = mcpy.UncertaintyWidget(rect1)

    ui.show()
    sys.exit(app.exec())
