def tax_calculator(wage_yearly):
    """
    Calculates monthly salary after tax and returns the salary and tax rate.
    :param wage_yearly: Yearly salary
    :return: Tuple (salary_monthly, tax_rate)
    """
    # The following if-elif statements represent different tax brackets based on yearly income.
    # Each bracket applies a specific tax rate to the income, as per the Spanish tax system.
    i = wage_yearly
    if i <= 12450:
        # First tax bracket: income up to 12,450 EUR is taxed at 19%
        solution1 = wage_yearly * 0.19
        solution2 = wage_yearly - solution1
        salary_monthly = solution2 / 12
        tax_rate = 0.19
    elif i >= 12450 and i <= 20200:
        # Second tax bracket: income from 12,451 to 20,200 EUR is taxed at 24%
        solution1 = wage_yearly * 0.24
        solution2 = wage_yearly - solution1
        salary_monthly = solution2 / 12
        tax_rate = 0.24
    elif i >= 20200 and i <= 35200:
        # Third tax bracket: income from 20,201 to 35,200 EUR is taxed at 30%
        solution1 = wage_yearly * 0.3
        solution2 = wage_yearly - solution1
        salary_monthly = solution2 / 12
        tax_rate = 0.3
    elif i >= 35200 and i <= 60000:
        # Fourth tax bracket: income from 35,201 to 60,000 EUR is taxed at 37%
        solution1 = wage_yearly * 0.37
        solution2 = wage_yearly - solution1
        salary_monthly = solution2 / 12
        tax_rate = 0.37
    elif i >= 60000 and i <= 300000:
        # Fifth tax bracket: income from 60,001 to 300,000 EUR is taxed at 45%
        solution1 = wage_yearly * 0.45
        solution2 = wage_yearly - solution1
        salary_monthly = solution2 / 12
        tax_rate = 0.45
    else:
        # Sixth tax bracket: income above 300,000 EUR is taxed at 47%
        solution1 = wage_yearly * 0.47
        solution2 = wage_yearly - solution1
        salary_monthly = solution2 / 12
        tax_rate = 0.47
    return salary_monthly, tax_rate

# Example usage:
# salary, tax = tax_calculator(30000)
# print(f"Monthly salary after tax: {salary} euro, Tax rate: {tax*100}%")