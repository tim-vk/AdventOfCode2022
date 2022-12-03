def elf_calorie_counter(filename):
    with open(filename, 'r') as file:
        elf_calories = [0]
        elfIndex = 0
        for meal in file.readlines():
            if meal != '\n':
                elf_calories[elfIndex] += int(meal)
            else:
                elfIndex += 1
                elf_calories.append(0)
    return elf_calories


if __name__ == '__main__':
    elf_calories = elf_calorie_counter('input-data')
    elf_calories_max = max(elf_calories)
    print(f"The elf with the most nutricious snacks has : {elf_calories_max} calories")
    elf_calories.sort(reverse=True)
    print(elf_calories)
    top_three = sum(elf_calories[0:3])
    print(f"Top three have {top_three} calories all together")

