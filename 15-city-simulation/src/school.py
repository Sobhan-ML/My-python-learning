# school.py
import math
from src import work_place


class School(work_place.WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self) -> None:
        self.capacity = int(math.floor(math.sqrt(self.level)))

    def calc_costs(self) -> int:
        costs = work_place.Consts.BASE_PLACE_COST * \
            math.floor(math.sqrt(self.level))
        return costs
