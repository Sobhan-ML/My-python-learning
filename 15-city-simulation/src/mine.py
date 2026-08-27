# mine.py
from src import work_place


class Mine(work_place.WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "mine"

    def calc_capacity(self) -> None:
        self.capacity = self.level ** 2

    def calc_costs(self) -> int:
        costs = work_place.Consts.BASE_PLACE_COST + \
            work_place.Consts.LEVEL_MUL * self.level
        return costs
