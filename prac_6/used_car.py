from prac_6.car import Car


def main():
    my_car = Car("lancer", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)
    print(limo)


main()
