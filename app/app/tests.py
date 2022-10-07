"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test Calc module"""
    def test_add_numbers(self):
        """Adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
    
    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.sub(4, 1)
        self.assertEqual(res, 3)

