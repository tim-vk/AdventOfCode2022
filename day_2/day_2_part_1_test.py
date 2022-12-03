import unittest
from day_2_part_1 import match_player, match

class MyTestCase(unittest.TestCase):
    def test_match(self):
        assert match("A", "Y") == 8
        assert match("B", "X") == 1
        assert match("C", "Z") == 6

    def test_match_player(self):
        assert match_player("test-input-data") == 15


if __name__ == '__main__':
    unittest.main()
