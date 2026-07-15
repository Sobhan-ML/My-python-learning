import re

def solve_equation(equation):
    """
    Solves a masked addition equation (e.g., '1# + 2 = 14') 
    and returns the completed equation or '-1' if invalid.
    """
    parts = equation.split()
    
    # Basic validation for the expected equation format (A + B = C)
    if len(parts) != 5 or parts[1] != '+' or parts[3] != '=':
        return '-1'
        
    a_str, b_str, c_str = parts[0], parts[2], parts[4]

    expected_val = 0
    masked_part = ""

    try:
        # Identify which part is masked and calculate the expected value
        if '#' in a_str:
            expected_val = int(c_str) - int(b_str)
            masked_part = a_str
        elif '#' in b_str:
            expected_val = int(c_str) - int(a_str)
            masked_part = b_str
        elif '#' in c_str:
            expected_val = int(a_str) + int(b_str)
            masked_part = c_str
        else:
            return '-1' # No mask indicator '#' found
    except ValueError:
        # Prevents crashing if multiple parts contain '#' or invalid characters
        return '-1'

    if expected_val < 0:
        return '-1'

    expected_str = str(expected_val)

    # Build regex pattern: replace '#' with '\d*' to match missing digits
    pattern = "^" + masked_part.replace('#', r'\d*') + "$"

    # Check if the calculated expected value matches the regex pattern
    if re.match(pattern, expected_str):
        if '#' in a_str:
            return f"{expected_str} + {b_str} = {c_str}"
        elif '#' in b_str:
            return f"{a_str} + {expected_str} = {c_str}"
        elif '#' in c_str:
            return f"{a_str} + {b_str} = {expected_str}"
    
    return '-1'


def main():
    print("========================================")
    print("Welcome to the Masked Equation Solver! 🧮")
    print("========================================")

    while True:
        try:
            # 1. Validation loop for user input
            print("\nEnter an addition equation with '#' as the missing part (e.g., '1# + 5 = 20').")
            print("Type 'exit' to quit.")
            user_input = input("-> ").strip()
            
            if user_input.lower() == 'exit':
                break
                
            if not user_input:
                print("❌ Error: Input cannot be empty.\n")
                continue
                
            # Run the solver
            result = solve_equation(user_input)
            
            if result == '-1':
                print("-> Result: -1 (No valid solution found or invalid format)")
            else:
                print(f"-> Result: {result} ✨")

        except Exception as e:
            print(f"❌ Warning: An unexpected error occurred: {e}\n")

    print("\nProgram closed successfully! 🚀")


if __name__ == "__main__":
    main()