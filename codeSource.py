import math

def binomiale(n, p, k):
    return round(math.comb(n, k) * p**k *(1-p)**(n-k), 4)

def geometrique(p, k):
    return (1-p)**(k-1) * p

def poisson(lambdaLettre, k):
    return (lambdaLettre ** k * math.exp(-lambdaLettre)) / math.factorial(k)

def exponentielle(lambdaLettre, k):
    return lambdaLettre * math.exp(-lambdaLettre*k)

def gamma(x, k, lambda_):
    if x < 0:
        return 0
    return (
        (lambda_ ** k)
        / math.gamma(k)
        * (x ** (k - 1))
        * math.exp(-lambda_ * x)
    )

#------------------------
def estEgal(func, k):
    return func(k)

def superieurOuEgal(func, k):
    return 1 - inferieurOuEgal(func, k - 1)

def inferieurOuEgal(func, k):
    resultat = 0
    for i in range(k + 1):
        resultat += func(i)
    return resultat

def superieur(func, k):
    return 1 - inferieurOuEgal(func, k)

def inferieur(func, k):
    return inferieurOuEgal(func, k - 1)

print("Bienvenue dans le calculateur des lois de probabilités!")
print("-"*25)
print("Loi discrète: ")
print("1 - Loi Bernoulli")
print("2 - Loi Binomiale")
print("3 - Loi Géométrique")
print("4 - Loi Poisson")
print("Loi continue: ")
print("5 - Loi Exponentielle")
print("6 - Loi Gamma")
print("-"*25)
choix = input("Entrez le numéro de votre choix: ")
#Bloc pour la loi Bernoulli
if choix == "1":
    valeur_p = float(input("Entrez la probabilité(p): "))
    print("-"*25)
    print("E[X] = ", valeur_p)
    esperance = valeur_p * (1 - valeur_p)
    print("Var[X] = ", esperance)
#Bloc pour la loi Binomiale
if choix == "2":
    valeur_n = int(input("Entrez le nombre de fois que le test doit être fait(n): "))
    valeur_p = float(input("Entrez la probabilité(p): "))
    valeur_k = int(input("Quelle est la valeur de k(Nombre de succès)? "))
    signe = input("X (<, >, <=, >=, =) k ? ")
    esperance = valeur_n * valeur_p
    variance = esperance * (1 - valeur_p)
    print("-"*25)
    print("E[X] = ", esperance)
    print("Var[X] = ", variance)
    if signe == "=":
        f = lambda k: binomiale(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", estEgal(f, valeur_k))
    if signe == "<":
        f = lambda k: binomiale(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", inferieur(f, valeur_k))
    if signe == ">":
        f = lambda k: binomiale(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", superieur(f, valeur_k))
    if signe == "<=":
        f = lambda k: binomiale(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", inferieurOuEgal(f, valeur_k))
    if signe == ">=":
        f = lambda k: binomiale(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", superieurOuEgal(f, valeur_k))

#Bloc pour la loi Géométrique
if choix == "3":
    valeur_p = float(input("Entrez la probabilité(p): "))
    valeur_k = int(input("Combien d'essai sont nécessaires afin d'obtenir un succès(k)? "))
    signe = input("X (<, >, <=, >=, =) k ? ")
    esperance = 1 / valeur_p
    variance = (1-valeur_p)/valeur_p**2
    print("-"*25)
    print("E[X] = ", esperance)
    print("Var[X] = ", variance)
    if signe == "=":
        f = lambda k : geometrique(valeur_p, valeur_k)  
        print(f"P[X{signe}{valeur_k}] = ", estEgal(f, valeur_k))
    if signe == "<":
        f = lambda k: geometrique(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", inferieur(f, valeur_k))
    if signe == ">":
        f = lambda k: geometrique(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", superieur(f, valeur_k))
    if signe == "<=":
        f = lambda k: geometrique(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", inferieurOuEgal(f, valeur_k))
    if signe == ">=":
        f = lambda k: geometrique(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", superieurOuEgal(f, valeur_k))

#Bloc pour la loi de Poisson
if choix == "4":
    valeur_lambda = int(input("Quelle est la moyenne d'observation par heure(lambda)? "))
    valeur_k = int(input("Quelle est la valeur observée? "))
    print("-"*25)
    print("E[X] = ", valeur_lambda)
    print("Var[X] = ", valeur_lambda)
    if signe == "=":
        f = lambda k : geometrique(valeur_p, valeur_k)  
        print(f"P[X{signe}{valeur_k}] = ", estEgal(f, valeur_k))
    if signe == "<":
        f = lambda k: geometrique(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", inferieur(f, valeur_k))
    if signe == ">":
        f = lambda k: geometrique(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", superieur(f, valeur_k))
    if signe == "<=":
        f = lambda k: geometrique(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", inferieurOuEgal(f, valeur_k))
    if signe == ">=":
        f = lambda k: geometrique(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", superieurOuEgal(f, valeur_k))
#Bloc pour la loi exponentielle
if choix == "5":
    valeur_lambda = int(input("Quelle est le taux d'occurence(lambda)? "))
    valeur_k = int(input("Quelle est le temps d'attente avant le prochain évènement? "))
    print("-"*25)
    print("E[X] = ", 1 / valeur_lambda)
    print("Var[X] = ", 1 / (valeur_lambda)**2)
    if signe == "=":
        f = lambda k : exponentielle(valeur_p, valeur_k)  
        print(f"P[X{signe}{valeur_k}] = ", estEgal(f, valeur_k))
    if signe == "<":
        f = lambda k: exponentielle(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", inferieur(f, valeur_k))
    if signe == ">":
        f = lambda k: exponentielle(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", superieur(f, valeur_k))
    if signe == "<=":
        f = lambda k: exponentielle(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", inferieurOuEgal(f, valeur_k))
    if signe == ">=":
        f = lambda k: exponentielle(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", superieurOuEgal(f, valeur_k))
#Bloc pour la loi Gamma
if choix == "6":
    valeur_lambda = float(input("Quel est le taux d'occurrence (lambda) ? "))
    valeur_k = float(input("Quel est le paramètre de forme (k) ? "))
    print("-" * 25)
    print("E[X] =", valeur_k / valeur_lambda)
    print("Var[X] =", valeur_k / (valeur_lambda ** 2))
    if signe == "=":
        f = lambda k : gamma(valeur_p, valeur_k)  
        print(f"P[X{signe}{valeur_k}] = ", estEgal(f, valeur_k))
    if signe == "<":
        f = lambda k: gamma(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", inferieur(f, valeur_k))
    if signe == ">":
        f = lambda k: gamma(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", superieur(f, valeur_k))
    if signe == "<=":
        f = lambda k: gamma(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", inferieurOuEgal(f, valeur_k))
    if signe == ">=":
        f = lambda k: gamma(valeur_n, valeur_p, k)
        print(f"P[X{signe}{valeur_k}] = ", superieurOuEgal(f, valeur_k))

