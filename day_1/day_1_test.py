import unittest
from day_1 import elf_calorie_counter


class MyTestCase(unittest.TestCase):
    def test_something(self):
        assert max(elf_calorie_counter("test-input-data")) == 24000


if __name__ == '__main__':
    unittest.main()
