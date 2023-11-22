from abc import ABC

import mcpy.BaseType.UncertaintyDistributions as ud


class TypeBUncertainty(ud.Uncertainty, ABC):
    def __init__(self, vnom: float, *args, **kwargs):
        super().__init__(vnom, *args, **kwargs)

