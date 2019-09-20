import unittest
import get_column_stats
import random
import os
import sys


class TestStat(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(get_column_stats.calc_mean([1, 1, 1, 1, 1]), 1)
        self.assertEqual(get_column_stats.calc_mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(get_column_stats.calc_mean([2, 3, 9, 11, 45]), 14)
        self.assertEqual(get_column_stats.calc_mean([2, 2, 2, 10, 6]), 4.4)
        with self.assertRaises(ZeroDivisionError) as context:
            get_column_stats.calc_mean([])
            self.assertTrue('division by zero' in context.exception)
        rand_data = [random.randint(1, 100) for _ in range(100)]
        rand_mean = (sum(rand_data)/len(rand_data))
        self.assertEqual(get_column_stats.calc_mean(rand_data), rand_mean)

    def test_stdev(self):
        self.assertAlmostEqual(
            get_column_stats.calc_stdev([1, 1, 1, 1, 1], 1),
            0,
            places=2)
        self.assertAlmostEqual(
            get_column_stats.calc_stdev([1, 2, 3, 4, 5], 3),
            1.58,
            places=2)
        self.assertAlmostEqual(
            get_column_stats.calc_stdev([2, 3, 9, 11, 45], 14),
            17.75,
            places=2)
        self.assertAlmostEqual(
            get_column_stats.calc_stdev([2, 2, 2, 10, 6], 4.4),
            3.577,
            places=2)


if __name__ == '__main__':
    unittest.main()
