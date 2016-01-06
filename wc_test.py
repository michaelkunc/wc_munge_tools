import unittest

import wc


class WCTests(unittest.TestCase):

    def test_the_tests(self):
        self.assertEqual('is this thing on?', wc.test_the_tests())

    def test_open_file(self):
        lines = wc.open_and_split('test_data.txt')
        self.assertEqual('##############################################', lines[0])

    def test_clean_lines(self):
        lines = wc.open_and_split('test_data.txt')
        cleaned_lines = wc.clean_lines(lines, '@', 'include')
        self.assertEqual("(1)  13 July     France     4-1 (3-0)  Mexico    @ Estadio Pocitos, Montevideo", cleaned_lines[0])


if __name__ == '__main__':
    unittest.main()
