from decimal import Decimal
class BaseFloat:
    def __init__(self, vnom: float, unit: str = ""):
        self._vnom: float = vnom
        self._unit: str = unit if unit is not None else ""

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

    @property
    def vnom(self):
        return self._vnom

    @vnom.setter
    def vnom(self, value):
        self._vnom = value

    def __float__(self):
        return float(self.vnom)

    def __int__(self):
        return int(self.vnom)

    def __str__(self):
        return f"{self.vnom} {self._unit}".strip()
