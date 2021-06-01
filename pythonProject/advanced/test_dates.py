import unittest
from unittest.mock import patch
from io import StringIO
from dates import *
import sys


class DatesTests(unittest.TestCase):
    """ test class for glob"""

    # def setUp(self):
    #     se

    def test_invalid_day(self):

        expected = "Could not process date - For the given month and year, the day should be of range 1-28\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Date(29, 2, 2021)
            self.assertEqual(expected, fake_out.getvalue())

    def test_correct_date(self):
        date = Date(26,6,1993)
        self.assertIsNot(date, None)

class EventsTests(unittest.TestCase):
    def setUp(self):
        with open("eventLog.txt", "r") as f:
            events = f.read()
        self.file = events
        self.calender = Calender()

    def to_date(self, date):
        d, m, y = filter(lambda x: x != '.', date.split('.'))
        d, m, y = int(d), int(m), int(y)
        if not isinstance(d, int) or not isinstance(m, int) or not isinstance(y, int):
            raise ValueError("Date must be a number")
        return Date(d, m, y)

    def test_load_valid_events(self):
        lines = self.file.split('\n')
        for i in range(4):
            print(lines[i])
            t = lines[i].split(' ')
            self.calender.add_event(t[0], self.to_date(t[1]))


if __name__ == '__main__':
    unittest.main()
