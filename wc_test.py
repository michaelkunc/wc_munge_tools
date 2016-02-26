import unittest

import wc


class WCTests(unittest.TestCase):
    @classmethod
    def setUpClass(WCTests):
        WCTests.lines = wc.open_and_split('test_data.txt')


    def test_open_file(self):
        self.assertEqual(
            '##############################################', WCTests.lines[0])

    def test_remove_lines_include(self):
        cleaned_lines = wc.remove_lines(WCTests.lines, '@', 'include')
        test_text = "(1)  13 July     France     4-1 (3-0)  Mexico    @ Estadio Pocitos, Montevideo"
        self.assertEqual(test_text, cleaned_lines[0])

    def test_remove_lines_include_uppercase(self):
        lines = wc.open_and_split('test_data.txt')
        cleaned_lines = wc.remove_lines(lines, '@', "INclude")
        self.assertEqual(
            "(1)  13 July     France     4-1 (3-0)  Mexico    @ Estadio Pocitos, Montevideo", cleaned_lines[0])

    def test_remove_lines_exclude(self):
        lines = wc.open_and_split('test_data.txt')
        cleaned_lines = wc.remove_lines(lines, '#', 'exclude')
        self.assertEqual("", cleaned_lines[0])

    def test_remove_lines_exclude_uppercase(self):
        lines = wc.open_and_split('test_data.txt')
        cleaned_lines = wc.remove_lines(lines, '#', 'exCLUDE')
        self.assertEqual("", cleaned_lines[0])

    def test_remove_lines_error(self):
        lines = wc.open_and_split('test_data.txt')
        self.assertRaises(ValueError, wc.remove_lines, lines, "#", 'keep')

    def test_clear_empty_lines(self):
        lines = wc.open_and_split('test_data.txt')
        lines = wc.clear_empty_lines(lines)
        self.assertEqual(60, len(lines))

    def test_remove_substring(self):
        lines = wc.open_and_split('test_data.txt')
        lines = wc.remove_substring(lines, "#")
        lines = wc.clear_empty_lines(lines)
        self.assertEqual(' World Cup 1930 Uruguay, 13 July - 30 July', lines[0])

    def test_replace_substring(self):
        lines = wc.open_and_split('test_data.txt')
        lines = wc.replace_substring(lines, "#", "$")
        self.assertEqual('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$',lines[0])

    def test_smaller(self):
        first_list = [1,2,3]
        second_list = [1,2,3,4]
        self.assertFalse(wc.smaller(first_list, second_list))

    def test_replace_single_substring(self):
        lines = wc.open_and_split('test_data.txt')
        lines[0] = wc.replace_single_substring(lines, 0, '#', '$')
        self.assertEqual('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$',lines[0])





if __name__ == '__main__':
    unittest.main()
