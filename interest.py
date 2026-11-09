def compound_interest(principal, rate, years):
    # Future Value = principal * (1 + rate) ** years
    return principal * (1 + rate) ** years

def simple_interest(principal, rate, years):
    # Future Value = principal + (principal * rate * years)
    return principal + (principal * rate * years)