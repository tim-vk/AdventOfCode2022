import csv


def pair_within_each_other(pair: [str]):
    min1, max1 = map(int, pair[0].split("-", 2))
    min2, max2 = map(int, pair[1].split("-", 2))
    if min1 <= min2 and max1 >= max2:
        return True
    elif min2 <= min1 and max2 >= max1:
        return True
    return False


def pairs_overlap(pair: [str]):
    min1, max1 = map(int, pair[0].split("-", 2))
    min2, max2 = map(int, pair[1].split("-", 2))
    if min1 <= min2 <= max1:
        return True
    elif min2 <= min1 <= max2:
        return True
    return False


def parse_file_part_1(filename):
    total = 0
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if pair_within_each_other(row):
                total += 1
    return total


def parse_file_part_2(filename):
    total = 0
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if pairs_overlap(row):
                total += 1
    return total


if __name__ == "__main__":
    print(parse_file_part_1("input-data"))
    print(parse_file_part_2("input-data"))
