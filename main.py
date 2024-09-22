from math import sqrt

#### Fonction secondaire


def isprime(p):

    # votre code ici
    if p<=1:
        return False
    for i in range(2,int(sqrt(p)+1)):
        if p%i==0:
            return False
    return True


    

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    

    for n in range(50):
        if isprime(n):
            print(n, end=", est un nombre premier. ")
        else:
            print(n, end=", n'est pas un nombre premier.")

    print()


if __name__ == "__main__":
    main()
