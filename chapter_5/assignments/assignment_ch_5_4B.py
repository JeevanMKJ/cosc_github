def main():
    factor = 12

    with open('car_costs.txt', 'r') as costs_file:

        line = costs_file.readline()
        total = 0

        while line != '':
            cost = float(costs_file.readline())
            total += cost
            print(f"{line.strip('\n')} : {cost}")

            line = costs_file.readline()

    print(f"\nTotal monthly cost: {total}")


if __name__ == '__main__':
    main()