for i in range(12):
    balance = balance - (balance * monthlyPaymentRate)
    balance = balance + (balance * (annualInterestRate / 12))


print("Remaining balance: " + str(round(balance, 2)))