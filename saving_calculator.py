from tax_calculator import tax_calculator # type: ignore

def savings_calculator(income, expenses):
    """
    Calculates yearly savings after tax and expenses.
    :param income: Yearly income
    :param expenses: Yearly expenses
    :return: Yearly savings
    """
    salary_monthly, tax_rate = tax_calculator(income)  # Get monthly salary and tax rate based on income
    yearly_tax = income * tax_rate  # Calculate yearly tax from the tax rate
    savings = income - expenses - yearly_tax  # Calculate yearly savings after tax and expenses
    return savings  # Return yearly savings only

# Ask user for input values
# income = float(input("Enter your yearly income: "))  # Get yearly income from user (before tax)
#expenses = float(input("Enter your yearly expenses: "))  # Get yearly expenses from user (such as rent, food, etc.)

# Call the savings calculator with user inputs
# yearly_savings = savings_calculator(income, expenses)

# Display the results
# print(f"Yearly savings: {yearly_savings}$")