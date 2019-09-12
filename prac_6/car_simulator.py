from prac_6.car import Car

MENU = "Menu:\nd) drive\nr) refuel\nq) quit"


def main():
    """Car simulator program, demonstrating use of Car class."""
    print("Let's drive!")
    name = input("Enter your car name: ")
    # create a Car instance with initial fuel of 100 and user-provided name
    car = Car(type, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            distance_to_drive = int(
                input("How far do you want to go? "))
            while distance_to_drive < 0:
                print("Distance must be >= 0")
                distance_to_drive = int(
                    input("How far do you want to go? "))
            distance_driven = car.drive(distance_to_drive)
            print("The car has driven {}km".format(distance_driven), end="")
            if car.fuel == 0:
                print(" out of fuel", end="")
            print(".")
        elif choice == "r":
            fuel_to_add = int(input(
                "How much fule are you putting in? "))
            while fuel_to_add < 0:
                print("Fuel must be >= 0")
                fuel_to_add = int(input(
                    "How much fule are you putting in? "))
            car.add_fuel(fuel_to_add)
            print("Added {} L of fuel.".format(fuel_to_add))
        else:
            print("Invalid choice")
        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("\nGood bye {}'s driver.".format(car.type))


main()