import unittest
from parse_csv import ParseCSV


class testParseCSVTest(unittest.TestCase):

    def setUp(self):
        self.data = 'test.csv'
        self.test = ParseCSV(self.data)
        self.parsed_data = self.test.read_data()

    def test_csv_read_data_headers(self):
        self.assertEqual(
            self.parsed_data[0],
            ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
            )

    def test_csv_read_random_data_points(self):
        self.assertEqual(self.test.read_data()[1][0], '5/8/14')
        self.assertEqual(self.test.read_data()[1][6], '511')

    def test_get_min_difference(self):
        self.assertEqual(self.test.get_min_difference(self.parsed_data, 2, 3), 6)

    def test_get_name(self):
        index_value = self.test.get_min_difference(self.parsed_data, 2, 3)
        self.assertEqual(self.test.get_team(index_value, self.parsed_data), '4/30/14')


if __name__ == '__main__':
    unittest.main()
