import unittest
from day_3 import duplicate_per_rucksack, priority, analyze_file_part_1, analyze_file_part_2

class MyTestCase(unittest.TestCase):
    def test_duplicate(self):
        assert duplicate_per_rucksack("vJrwpWtwJgWrhcsFMMfFFhFp") == "p"
        assert duplicate_per_rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L"
        assert duplicate_per_rucksack("PmmdzqPrVvPwwTWBwg") == "P"
        assert duplicate_per_rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn") == "v"
        assert duplicate_per_rucksack("ttgJtRGJQctTZtZT") == "t"
        assert duplicate_per_rucksack("CrZsJsPPZsGzwwsLwLmpwMDw") == "s"

    def test_priority(self):
        assert priority("a") == 1
        assert priority("B") == 28

    def test_analyze_file(self):
        assert analyze_file_part_1("test-input-data") == 157

    def test_analyze_file2(self):
        assert analyze_file_part_2("test-input-data") == 70
if __name__ == '__main__':
    unittest.main()
