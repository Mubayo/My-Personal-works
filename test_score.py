
LINE = "-" * 45
PERFECT = 100


def get_test_scores() -> list:
    print("Welcome to Test Score Analysis Program" + "\n------------------------------")
    items = []
    done = False
    count = 1
    while not done:
        score = int(input(f"Enter score #{count} in the range 1-100: "))
        while not (1<=score<=100):
            score = int(input(f"Enter score #{count} in the range 1-100: "))
        count += 1
        if count == 6:
            done = True
        items.append(score)
    return items

def find_lowest(items: list) -> (int,float):
    lowest = items[0]
    for item in items:
        if item < lowest:
            lowest = item
    return lowest

def find_highest(items: list) -> (int,float):
    highest = items[0]
    for item in items:
        if item > highest:
            highest = item
    return item


def get_average(items : list) -> float:
    total = 0
    for item in items:
        total += item
    return total / len(items)

def get_perfect_num(items: list) -> (int,float):
    total = 0
    for item in items:
        if item == PERFECT:
            total += 1
        else:
            continue
    return total


def print_results(low,high,average,count):
    print(LINE)
    print(f"Lowest score = {low}")
    print(f"Highest score = {high}")
    print(f"Average score = {average : .2f}")
    print(f"Number of perfect test scores = {count}")


def main():
    tests = []
    tests = get_test_scores()
    lowest = find_lowest(tests)
    highest = find_highest(tests)
    average = get_average(tests)
    perfect_count = get_perfect_num(tests)
    print_results(lowest,highest,average,perfect_count)

main()


def compute_sum_from_file(filename: str) -> int:
    """computes the sum of integers in a file if there are single intergers per line"""
    with open(filename,"r") as file:
        total = 0
        for line in file.readlines():
            for item in line:
                if item != "\n":
                    total += int(item)
        return total