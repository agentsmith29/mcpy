import os
import unittest

from scipy.stats import norm

from mcpy.TypeBUncertainty.Normal import Normal
from mcpy.TypeBUncertainty.Rectangular import Rectangular


class TestNormalDistribution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.value = 6.7e-3
        cls.uexp = ((40e-3 * 19e-3) / 100)
        cls.k = 3
        cls.coverage = 1 - norm.pdf(cls.k)
        cls.definition = "Sample normal Definition"
        cls.description = "Sample normal Description"
        cls.unit = "nm"

    def test_to_dict(self):
        # Setup the normal distribution
        normal = Normal(self.value, self.uexp, k=self.k, unit=self.unit)
        normal.definition = self.definition
        normal.description = self.description


        self.assertEqual(
            normal.to_dict(),
            {'coverage': self.coverage,
             'definition': self.definition,
             'description': self.description,
             'type': 'Type B',
             'distribution': 'Normal',
             'uexp': self.uexp,
             'unit': self.unit,
             'value': self.value}
        )

    def test_from_dict(self):
        normal_reference = Normal(self.value, self.uexp, k=self.k, unit=self.unit)
        normal_reference.definition = self.definition
        normal_reference.description = self.description


        from_dict = {'coverage': self.coverage,
             'definition': self.definition,
             'description': self.description,
             'type': 'Type B',
             'distribution': 'Normal',
             'uexp': self.uexp,
             'unit': self.unit,
             'value': self.value}

        normal_from_dict = Normal.from_dict(from_dict)

        self.assertEqual(type(normal_from_dict), Normal)

        self.assertEqual(
            normal_from_dict.to_dict(),
            from_dict
        )

class TestRectangularDistribution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.value = 100.0
        cls.hlim = 5e-3
        cls.a = 100 - 5e-3
        cls.b = 100 + 5e-3
        cls.k = 3
        cls.coverage = 1 - norm.pdf(3)
        cls.definition = "Sample Rect Definition"
        cls.description = "Sample Rect Description"
        cls.unit = "nm"

    def test_to_dict(self):
        # Setup the normal distribution
        rect = Rectangular(self.value, self.a, k=self.k, unit=self.unit)
        rect.definition = self.definition
        rect.description = self.description

        print(rect.to_dict())
        self.assertEqual(
            rect.to_dict(),
            {'coverage': self.coverage,
             'definition': self.definition,
             'description': self.description,
             'type': 'Type B',
             'distribution': 'Rectangular',
             'a': self.a,
             'b': self.b,
             'hlim': self.hlim,
             'unit': self.unit,
             'value': self.value}
        )

    def test_from_dict(self):
        normal_reference = Normal(self.value, self.uexp, k=self.k, unit=self.unit)
        normal_reference.definition = self.definition
        normal_reference.description = self.description


        from_dict = {'coverage': self.coverage,
             'definition': self.definition,
             'description': self.description,
             'type': 'Type B',
             'distribution': 'Normal',
             'uexp': self.uexp,
             'unit': self.unit,
             'value': self.value}

        normal_from_dict = Normal.from_dict(from_dict)

        self.assertEqual(type(normal_from_dict), Normal)

        self.assertEqual(
            normal_from_dict.to_dict(),
            from_dict
        )


if __name__ == '__main__':
    unittest.main()
