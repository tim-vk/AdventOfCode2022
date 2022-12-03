import unittest
from day_2_part_2 import match_player, match

class MyTestCase(unittest.TestCase):
    def test_match(self):
        assert match("A", "Y") == 4
        assert match("B", "X") == 1
        assert match("C", "Z") == 7

    def test_match_player(self):
        assert match_player("test-input-data") == 12


if __name__ == '__main__':
    unittest.main()
