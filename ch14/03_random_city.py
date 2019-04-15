import random


CITIES = ['Berlin', 'London', 'Paris', 'Tokyo', 'Rome', 'Oslo', 'Bangkok']


def main():
    for i in range(10):
        city = random.choice(CITIES)
        print('random selection', i, city)


main()
