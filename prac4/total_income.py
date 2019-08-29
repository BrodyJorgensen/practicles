def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)
    print_report(incomes)


def print_report(incomes):  # had trouble with this function referred to solutions and still am unsure
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):  # TODO inquire why this is uesed
        total += income
        print("Month {:2} - Income: &{:10.2f} Total: ${:10.2f}".format(month + 1, income, total))


main()
