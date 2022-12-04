import unittest
from day_4 import pair_within_each_other, parse_file_part_1, pairs_overlap, parse_file_part_2


class MyTestCase(unittest.TestCase):
    def test_pair_within_each_other(self):
        assert not pair_within_each_other(["1-5", "2-6"])
        assert pair_within_each_other(["1-5", "2-4"])
        assert pair_within_each_other(["2-4", "1-5"])
        assert not pair_within_each_other(["2-7", "1-5"])
        assert not pair_within_each_other(["7-7", "8-42"])

    def test_pair_overlap(self):
        assert pairs_overlap(["1-5", "2-6"])
        assert pairs_overlap(["1-5", "2-4"])
        assert pairs_overlap(["2-4", "1-5"])
        assert pairs_overlap(["2-7", "1-5"])
        assert not pairs_overlap(["7-7", "8-42"])

    def test_parse_file(self):
        assert parse_file_part_1("test-input-data") == 2

    def test_parse_file2(self):
        assert parse_file_part_2("test-input-data") == 4

if __name__ == '__main__':
    unittest.main()
