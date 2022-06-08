x = 25
epsilon = 0.01
step = 0.00001
guess = 0.0

while guess <= x:
    print(abs(guess**2 -x))
    print(epsilon)
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))