def simple_interest():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time in years: "))

    interest = (principal * rate * time) / 100
    total_amount = principal + interest

    print("\nSimple Interest:", interest)
    print("Total Amount:", total_amount)


simple_interest()