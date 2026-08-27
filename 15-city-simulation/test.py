from src.worker import Worker
from src.teacher import Teacher
from src.engineer import Engineer
from src.mine import Mine
from src.school import School
from src.company import Company
from src.work_place import WorkPlaceIsFull
from src.person import Person
from src.work_place import WorkPlace


def run_test():
    print("--- City Simulation Test Start ---\n")

    # 1. Create Workplaces
    mine = Mine("Gold Mine")
    school = School("City High School")
    company = Company("Tech Corp")

    # Upgrade to increase capacity
    mine.upgrade()
    school.upgrade()
    school.upgrade()
    school.upgrade()
    company.upgrade()
    print("Workplaces created and upgraded successfully.")

    # 2. Create Citizens
    worker1 = Worker("Ali", 30)
    worker2 = Worker("Reza", 25)
    teacher = Teacher("Sara", 40)
    eng1 = Engineer("Mina", 28)
    eng2 = Engineer("Nima", 35)
    eng3 = Engineer("Omid", 22)
    print("Citizens created successfully.")

    # 3. Hire Citizens
    mine.hire(worker1)
    mine.hire(worker2)
    school.hire(teacher)
    company.hire(eng1)
    company.hire(eng2)
    print("Citizens hired successfully.")

    # 4. Test Workplace Full Exception
    print("\n--- Testing Workplace Exception ---")
    try:
        company.hire(eng3)
        print("Error: Exception did not trigger!")
    except WorkPlaceIsFull as e:
        print(f"Exception caught correctly: {e}")

    # 5. Financial Reports
    print("\n--- Financial Reports ---")
    print(f"{worker1.name} (Worker) net income: {worker1.calc()}")
    print(f"{teacher.name} (Teacher) net income: {teacher.calc()}")
    print(f"{eng1.name} (Engineer) net income: {eng1.calc()}")

    print(f"\n{mine.name} costs: {mine.calc()}")
    print(f"{school.name} costs: {school.calc()}")
    print(f"{company.name} costs: {company.calc()}")

    # 6. Overall Economy Status
    print("\n--- Overall Economy ---")
    print(f"Total People Net Income (Person.calc_all): {Person.calc_all()}")
    print(
        f"Total Workplaces Costs (WorkPlace.calc_all): {WorkPlace.calc_all()}")
    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    run_test()
