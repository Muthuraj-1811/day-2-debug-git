def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)
    return average


def main():
    numbers = [10, 20, 30, 40, 100]

    result = calculate_average(numbers)

    print("Average:", result)


if __name__ == "__main__":
    main()