import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.simple_iteration_method import IterativeSolver
import numpy as np


class TestIterativeSolver(unittest.TestCase):

    def test_basic_functionality(self):
        A = [[4, 1], [1, 3]]
        b = [1, 2]
        x0 = [0, 0]

        solver = IterativeSolver(A, n=2, b=b, x0=x0, tau=0.2, tolerance=1e-6, Nmax=100)
        solver.preprocess()
        solution, iterations, error = solver.Solver()

        self.assertIsInstance(solution, np.ndarray)
        self.assertTrue(iterations <= 100)
        self.assertTrue(error >= 0)


if __name__ == '__main__':
    unittest.main()