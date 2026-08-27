# City Economy Simulation 🏙️

An Object-Oriented Programming (OOP) project in Python that simulates the economic interactions between citizens and their workplaces.

## Features
* **Polymorphism & Inheritance:** Base classes (`Person` and `WorkPlace`) extended by specific entities (Workers, Engineers, Teachers, Mines, Schools, and Companies).
* **Economic Modeling:** Calculates life costs, base incomes, and adjusted wages based on age, job level, and workplace capacity.
* **Custom Exceptions:** Implementation of custom error handling such as `WorkPlaceIsFull`.
* **Clean Code Structure:** Modular design separating logical components into distinct python packages.

## Getting Started

### Prerequisites
* Python 3.8+

### Installation & Execution
1. Clone this repository:
   ```bash
   git clone [https://github.com/YourUsername/City-Simulation.git](https://github.com/YourUsername/City-Simulation.git)
   cd City-Simulation

### Run the simulation entry point:
```bash
python main.py

### Run the simulation entry point:
```bash
python main.py
```
## Project Structure
* `src/person.py`: Base class for managing demographics and personal finances.
* `src/work_place.py`: Base class for hiring logic, capacities, and corporate expenses.
* **Job Extensions:** `worker.py`, `teacher.py`, `engineer.py`
* **Workplace Extensions:** `mine.py`, `school.py`, `company.py`