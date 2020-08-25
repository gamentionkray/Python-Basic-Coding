num = input("Enter  a number: ")


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_primenumbers(n):
    if (type(n) == str and n.isalpha()):
        print("You have entered wrong input")
    else:
        num = int(float(n))
        if(num <= 0):
            print("You have entered wrong input")
        else:
            for i in range(2, num + 1):
                if checkPrime(i):
                    print(i, end=" ")


get_primenumbers(num)
