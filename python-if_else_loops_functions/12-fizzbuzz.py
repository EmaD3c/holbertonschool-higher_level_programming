#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):  # Start from 1 and go up to 100 inclusive
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
