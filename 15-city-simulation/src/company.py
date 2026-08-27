# company.py
from src import work_place


class Company(work_place.WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "company"

    def calc_capacity(self) -> None:
        self.capacity = self.level

    def calc_costs(self) -> int:
        costs = work_place.Consts.BASE_PLACE_COST * self.level
        return costs
