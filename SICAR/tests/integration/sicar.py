from pathlib import Path
import unittest
from SICAR import Sicar, State, Polygon
import os

class TestSicarBase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self._car = Sicar()

    def test_download_state(self):
        data = self._car.download_state(State.RR, Polygon.AREA_FALL, debug=True)
        self.assertIsInstance(
            data,
            Path,
        )

    def test_get_release_dates(self):
        self.assertIsInstance(self._car.get_release_dates(), dict)
