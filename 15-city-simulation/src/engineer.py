# engineer.py
import math
from src import person


class Engineer(person.Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.job = "engineer"

    def get_price(self) -> int:
        price = math.floor(
            person.Consts.BASE_PRICE[self.job] * math.sqrt(person.Consts.MIN_AGE / self.age))
        return int(price)

    def calc_life_cost(self) -> int:
        costs = math.floor(
            person.Consts.BASE_COST[self.job] * math.sqrt(self.age / person.Consts.MIN_AGE))
        return int(costs)

    def calc_income(self) -> int:
        income = math.floor(person.Consts.BASE_INCOME[self.job][self.work_place.get_expertise(
        )] * math.sqrt(person.Consts.MIN_AGE / self.age))
        return int(income)
