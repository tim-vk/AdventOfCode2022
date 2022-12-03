def duplicate_per_rucksack(rucksack):
    middle_index = int(len(rucksack) / 2)
    for item in rucksack[:middle_index]:
        if item in rucksack[middle_index:]:
            return item
    return None


def duplicate_per_row(elves: [str]):
    duplicates = list(elves[0])
    for index, elf in enumerate(elves[1:]):
        for item in duplicates.copy():
            if item not in elf:
                duplicates.remove(item)
    return duplicates[0]


def priority(letter: str):
    if letter.isupper():
        shift = 38
    else:
        shift = 96
    return ord(letter) - shift


def analyze_file_part_1(filename):
    with open(filename, 'r') as file:
        prioritySum = 0
        for line in file.readlines():
            prioritySum += priority(duplicate_per_rucksack(line))
    return prioritySum


def analyze_file_part_2(filename):
    with open(filename, 'r') as file:
        prioritySum = 0
        content = file.readlines()
        for i in range(int(len(content) / 3)):
            prioritySum += priority(duplicate_per_row(content[i*3:(i*3 + 3)]))
    return prioritySum


if __name__ == "__main__":
    result = analyze_file_part_1("input-data")
    print(f"answer to part 1: {result}")

    result = analyze_file_part_2("input-data")
    print(f"anser to part 2: {result}")
