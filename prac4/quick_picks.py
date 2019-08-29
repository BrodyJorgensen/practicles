import random

NUMBERS_PERLINE = 6
MIN = 1
MAX = 45

number_of_picks = int(input("how many numbers do you pick? "))
while number_of_picks < 0:
    print(" invalid number, try again ")
    number_of_picks = int(input("how many numbers do you pick? "))

for i in range(number_of_picks):
    quick_pick = []
    for number in range(NUMBERS_PERLINE):
        numbers = random.randint(MIN, MAX)
        while numbers in quick_pick:
            numbers = random.randint(MIN, MAX)
        quick_pick.append(numbers)
    quick_pick.sort()

    print(" ".join("{:2}".format(numbers) for numbers in quick_pick))
