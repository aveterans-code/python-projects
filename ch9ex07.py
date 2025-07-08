#ch9ex07

from random import randrange

def main():
    printIntro()
    n = getInputs()
    wins = simNGames(n)
    printResults(wins, n)

def printIntro():
    print("This program simulates multiple games of craps to estimate wins\n")

def getInputs():
    return int(input("Number of games to simulate? "))

def simNGames(n):
    wins = 0
    for i in range(n):
        if winCraps():
            wins +=1
    return wins

def winCraps():
    roll = rollDice()
    if roll == 7 or roll == 11:
        return True
    elif roll == 2 or roll == 3 or roll == 12:
        return False
    else:
        return rollForPoint(roll)

def rollForPoint(point):
    roll = rollDice()
    while roll != 7 and roll != point:
        roll = rollDice()
    return roll == point

def rollDice():
    return randrange(1,7) + randrange(1,7)

def printResults(wins, n):
    print("The player wins", wins, "of", n, "games.")
    print(f'The percentage of wins is {wins/n:0.2%}')

if __name__ == '__main__':
    main()
    
