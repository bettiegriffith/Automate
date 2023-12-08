import random
numberOfStreaks = 0

for experimentNumber in range (10000):
    oneTry = []
    streakNumber = 0
    for i in range (5):
        n = random.randint(0, 1)
        oneTry.append(n)
    for i in range (95):
        n = random.randint(0, 1)
        oneTry.append(n)
        last6 = oneTry[-6:]
        if last6 == [0, 0, 0, 0, 0, 0]:
            streakNumber = streakNumber + 1
        elif last6 == [1, 1, 1, 1, 1, 1]:
            streakNumber += 1

print('Chance of streak: %s%%' % (streakNumber / 100))

