import unittest

import wc


class WCTests(unittest.TestCase):

    @classmethod
    def setUpClass(WCTests):
        WCTests.lines = wc.open_and_split('test_data.txt')

    def test_open_file(self):
        test_text = '##############################################'
        self.assertEqual(test_text, WCTests.lines[0])

    def test_remove_lines_include(self):
        cleaned_lines = wc.remove_lines(WCTests.lines, '@', 'include')
        test_text = "(1)  13 July     France     4-1 (3-0)  Mexico    @ Estadio Pocitos, Montevideo"
        self.assertEqual(test_text, cleaned_lines[0])

    def test_remove_lines_include_uppercase(self):
        cleaned_lines = wc.remove_lines(WCTests.lines, '@', "INclude")
        test_text = "(1)  13 July     France     4-1 (3-0)  Mexico    @ Estadio Pocitos, Montevideo"
        self.assertEqual(test_text, cleaned_lines[0])

    def test_remove_lines_exclude(self):
        cleaned_lines = wc.remove_lines(WCTests.lines, '#', 'exclude')
        self.assertEqual("", cleaned_lines[0])

    def test_remove_lines_exclude_uppercase(self):
        cleaned_lines = wc.remove_lines(WCTests.lines, '#', 'exCLUDE')
        self.assertEqual("", cleaned_lines[0])

    def test_remove_lines_error(self):
        self.assertRaises(ValueError, wc.remove_lines,
                          WCTests.lines, "#", 'keep')

    def test_clear_empty_lines(self):
        self.assertEqual(60, len(wc.clear_empty_lines(WCTests.lines)))

    def test_remove_substring(self):
        lines = wc.remove_substring(WCTests.lines, "#")
        lines = wc.clear_empty_lines(lines)
        test_text = ' World Cup 1930 Uruguay, 13 July - 30 July'
        self.assertEqual(test_text, lines[0])

    def test_replace_substring(self):
        lines = wc.replace_substring(WCTests.lines, "#", "$")
        test_text = '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
        self.assertEqual(test_text, lines[0])

    def test_smaller(self):
        first_list = [1, 2, 3]
        second_list = [1, 2, 3, 4]
        self.assertFalse(wc.smaller(first_list, second_list))

    def test_replace_single_substring(self):
        lines = wc.replace_single_substring(WCTests.lines, 0, '#', '$')
        test_text = '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
        self.assertEqual(test_text, lines)


if __name__ == '__main__':
    unittest.main()
