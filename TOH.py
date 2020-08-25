n = int(input("Enter number of discs: "))

source = list(reversed(range(1, n+1)))
dest = []
support = []
counter = 0


def towerOfHanoi(n, source, dest, support):
    global counter
    if n > 0:
        towerOfHanoi(n - 1, source, support, dest)
        print(("Initial condition = " if counter == 0 else "Step " +
               str(counter) + " = "), source, dest, support)
        if source:
            dest.append(source.pop())
            counter += 1
        towerOfHanoi(n - 1, support, dest, source)


towerOfHanoi(len(source), source, dest, support)

print("Step " + str(counter) + " = ", source, dest, support)
