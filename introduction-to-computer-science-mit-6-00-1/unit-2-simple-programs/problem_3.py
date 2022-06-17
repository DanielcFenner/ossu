balance = 999999
annualInterestRate = 0.18

# Return final balance after payment over 1 year of accruing interest
def BalanceAfterTwelveMonths(balance, annualInterestRate, payment):
    for i in range(12):
        balance -= payment
        balance = balance + (balance * (annualInterestRate / 12))
    return balance

epsilon = 0.00000001
monthlyInterestRate = annualInterestRate / 12
high = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
low = balance / 12
payment = (high + low) / 2.0

# Binary search to find precise lowest payment
while abs(BalanceAfterTwelveMonths(balance, annualInterestRate, payment)) >= epsilon:
    payment = (high + low) / 2.0
    balanceTest = BalanceAfterTwelveMonths(balance, annualInterestRate, payment)
    if balanceTest > 0:
        low = payment
    else:
        high = payment

print("Lowest Payment: " + str(round(payment, 2)))
