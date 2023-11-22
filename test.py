import pandas as pd
from scipy.stats import norm

class Uncertainty:
    def __init__(self, value: float, coverage: float = 0.95, unit: str = "", definition: str = None,
                 description: str = None, ustd: float = 0):
        self._value = value
        self._unit = unit
        self._definition = definition
        self._description = description
        self._coverage = coverage
        self._k = norm.ppf(self._coverage)
        self._ustd = ustd
        self._uexp = self._calc_uexp(self._ustd)
        self._mcsamples = None

    def __float__(self):
        return self._value

    def _calc_uexp(self, ustd):
        # Calculate uncertainty expression based on ustd
        return self._value * ustd

    def

# Create a DataFrame with a column of Uncertainty instances
data = [
    Uncertainty(1.23),
    Uncertainty(4.56),
    Uncertainty(7.89)
]

df = pd.DataFrame({'Column1': data})

# Check the data type of the DataFrame column
print(df)
df = Uncertainty(1.23) + Uncertainty(4.56)
print(df)
