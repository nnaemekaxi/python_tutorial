import random


tray = []
def coinSimulator(n):
    tail = 0
    head = 0
    for x in range(n):
        toss = random.randint(0,1)
        if (toss == 0):
            tail = tail + 1
        else:
            head = head + 1
    print("Total Tails = ", tail)
    print("Total Heads = ", head)

coinSimulator(20)