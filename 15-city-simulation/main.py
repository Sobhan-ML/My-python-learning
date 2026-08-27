# main.py
from src.worker import Worker
from src.mine import Mine
from src.work_place import WorkPlaceIsFull


def get_valid_number(prompt_text: str) -> int:
    while True:
        user_input = input(prompt_text)
        try:
            return int(user_input)
        except ValueError:
            print("❌ Invalid input. Please enter a valid number!")


def main():
    print("--- City Economy Simulation ---")

    # 1. Create a Workplace
    coal_mine = Mine("Dark Coal Mine")
    coal_mine.upgrade()

    # 2. Get Employee Details Safely
    print("\n--- Hire a New Employee ---")
    emp_name = input("Enter employee's name: ")
    emp_age = get_valid_number(f"Enter {emp_name}'s age: ")

    jack = Worker(emp_name, emp_age)

    # 3. Hire Employee
    try:
        coal_mine.hire(jack)
        print(f"✅ Successfully hired {jack.name} at {coal_mine.name}!")
    except WorkPlaceIsFull as e:
        print(f"❌ {e}")

    # 4. Calculate Economics
    print(f"💰 {jack.name}'s Net Income: {jack.calc()}")
    print(f"📉 Mine's Costs: {coal_mine.calc()}")


if __name__ == "__main__":
    main()
