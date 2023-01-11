"""
Contains all of the unit tests for
random_person_generator.py.
Since the random module was used heavily
in random_person_generator.py, mock objects
were used to facilitate testing.
"""

import unittest
import random_person_generator as r
from unittest.mock import patch


class TestRandomPerson(unittest.TestCase):

    @patch('random_person_generator.male_first_name')
    def test_read_male_first_names(self, mocked):
        mocked.return_value = 'Matt'
        self.assertEqual(r.male_first_name(), 'Matt')

if __name__ == '__main__':
    unittest.main()