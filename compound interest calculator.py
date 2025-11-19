from saving_calculator import savings_calculator  # Import the savings_calculator function

def compound_interest_calculator():
    """
    Calculates compound interest based on user's savings, interest rate, time, and compounding frequency.
    Uses savings_calculator to determine the principal (yearly savings).
    """
    want_interest = input("Do you want to know your interest plan? (yes/no): ")
    if want_interest == "yes":
        # Get yearly income and expenses to calculate savings
        income = float(input("Enter your yearly income: "))
        expenses = float(input("Enter your yearly expenses: "))
        principal = savings_calculator(income, expenses)  # Use savings_calculator to get principal
        print(f"Your yearly savings (principal): {principal:.2f}")
        rate = float(input("Enter annual interest rate (in %): ")) / 100  # Convert percentage to decimal
        time = float(input("Enter time in years: "))
        n = int(input("Enter number of times interest is compounded per year: "))
        # Compound interest formula
        amount = principal * (1 + rate/n) ** (n * time)
        interest = amount - principal
        print(f"Final Amount: {amount:.2f}")
        print(f"Interest Earned: {interest:.2f}\n")

# Example usage:
compound_interest_calculator()  # Uncomment to run the calculator
