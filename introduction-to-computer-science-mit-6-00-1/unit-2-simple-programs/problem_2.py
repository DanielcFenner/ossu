balance = 999999
annualInterestRate = 0.18
payment = 0
balanceCopy = balance

while balanceCopy > 0:
    payment += 0.00000001
    balanceCopy = balance
    print(payment)
    for i in range(12):
        balanceCopy = balanceCopy - payment
        balanceCopy = balanceCopy + (balanceCopy * (annualInterestRate / 12))

print("Lowest payment: " + str(payment))
    
    