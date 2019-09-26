CURRENT_YEAR = 2019
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year_made=0, cost=0):
        self.name = name
        self.year_made = year_made
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year_made, self.cost)

    def get_age(self):
        return CURRENT_YEAR - self.year_made

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year_made < other.year_made
