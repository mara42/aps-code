from unittest import TestCase
from pancake_sort import pancake_sort


class TestPancakeSort(TestCase):

    def test_pancake_sort1(self):
        self.assertEqual(pancake_sort([5, 4, 3, 2, 1]), [0])

    def test_pancake_sort2(self):
        self.assertEqual(pancake_sort([1, 2, 3, 4, 5]), [1, 0])

    def test_pancake_sort3(self):
        self.assertEqual(pancake_sort([4, 3, 2, 1, 5]), [1, 2, 0])

    def test_pancake_sort4(self):
        self.assertEqual(pancake_sort([4, 1, 5, 2, 3]), [3, 1, 2, 4, 3, 0])

