__author__ = 'lena'

# equations
"""
Minimum monthly payment = Minimum monthly payment rate x Balance (Minimum monthly payment gets split into interest paid
                                                                  and principal paid)
Interest Paid = Annual interest rate / 12 months x Balance
Principal paid = Minimum monthly payment – Interest paid
Remaining balance = Balance – Principal paid
"""


def credit_card(running_bal, ir, min_paymnt_pct):
    total_paid = 0
    for month in range(1, 13):
        min_month_pmt = round(min_paymnt_pct * running_bal, 2)
        int_paid = round((ir/12) * running_bal, 2)
        princ_paid = round(min_month_pmt - int_paid, 2)
        running_bal = round(running_bal - princ_paid, 2)
        total_paid += min_month_pmt
        print("Month:", month, "\nMininum monthly payment:", min_month_pmt)
        print("Principle paid:", princ_paid)
        print("Remaining balance:", running_bal)

    print("RESULTS")
    print("Total amount paid is", round(total_paid, 2))
    print("Remaining balance", running_bal)


def main():
    debt = int(input("Enter the outstanding balance on your credit card: "))
    interest_rate = float(input("Enter the interest rate as a decimal: "))
    payment_percentage = float(input("Enter the minimum payment percentage as a decimal: "))

    credit_card(debt, interest_rate, payment_percentage)


if __name__ == "__main__":
    main()