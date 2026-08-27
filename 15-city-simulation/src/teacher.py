# teacher.py
from src import person


class Teacher(person.Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.job = "teacher"

    def get_price(self) -> int:
        price = person.Consts.BASE_PRICE[self.job] - \
            (self.age - person.Consts.MIN_AGE) * person.Consts.AGE_MUL
        return int(price)

    def calc_life_cost(self) -> int:
        costs = person.Consts.BASE_COST[self.job] + \
            (self.age - person.Consts.MIN_AGE) * person.Consts.AGE_MUL
        return int(costs)

    def calc_income(self) -> int:
        income = person.Consts.BASE_INCOME[self.job][self.work_place.get_expertise(
        )] - (self.age - person.Consts.MIN_AGE) * person.Consts.AGE_MUL
        return int(income)
