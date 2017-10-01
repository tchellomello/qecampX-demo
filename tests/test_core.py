"""QECampX test core."""
import unittest
from qecampx.core import QECampX


class QECampXBaseTest(unittest.TestCase):
    """Example tests for QECampX module."""

    def test_name(self):
        data1 = QECampX('Awesome', 20)
        data2 = QECampX('Bad', 2)

        self.assertIsInstance(data1.name, str)
        self.assertIsInstance(data2.name, str)

    def test_score(self):
        data1 = QECampX('Awesome', 20)
        data2 = QECampX('Bad', 2)

        self.assertGreater(data1.score_average, 1)
        self.assertEqual(data2.score, 8)
