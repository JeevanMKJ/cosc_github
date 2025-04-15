"""
9. Population Data
If you have downloaded the source code you will find a file
named USPopulation.txt in the Chapter 07 folder.
The file contains the midyear population of the United States,
in thousands, during the years 1950 through 1990.
The first line in the file contains the population for 1950,
the second line contains the population for 1951, and so forth.
Write a program that reads the file’s contents into a list.
The program should display the following data:
• The average annual change in population during the time period
• The year with the greatest increase in population during the time period
• The year with the smallest increase in population during the time period
"""
import random

def main():
    #generate_population_list()
    population_list = read_file()
    extract_data(population_list)

def generate_population_list():
    population_years = 40
    population_in_thousands = 8
    with open('USPopulation.txt', 'w') as population_file:
        for i in range(population_years):
            population = ""
            for num in range(population_in_thousands):
                population += str(random.randint(1, 9))
            population_file.write(f"{population}\n")
    print("Population numbers added to file.")

def read_file():
    with open('USPopulation.txt', 'r') as population_file:
        population_num = [int(line.strip('\n')) for line in population_file]
    return population_num

def extract_data(population_list):
    population_growth = [0] * (len(population_list) -1)
    for i in range(len(population_list) - 1):
        population_div = population_list[i] - population_list[i - 1]
        population_growth[i] = population_div

    population_average = sum(population_list) / len(population_list)
    population_growth_max = max(population_growth)
    population_growth_min = min(population_growth)

    print(population_average)
    print(population_growth_max)
    print(population_growth_min)



if __name__ == '__main__':
    main()