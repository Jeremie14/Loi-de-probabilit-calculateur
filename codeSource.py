import math

def binomiale(n, p, k):
    return round(math.comb(n, k) * p**k *(1-p)**(n-k), 4)

def geometrique(p, k):
    return (1-p)**(k-1) * p

def poisson(lambdaLettre, k):
    return (lambdaLettre**k * e**(-k))/math.factorial(k)

def estEgal(func, k):
    resultat = 0
    for i in range(k + 1):
        resultat += func(i)
    return resultat

def superieurOuEgal(func, k): pass

def inferieurOuEgal(func, k): pass

def superieur(func, k): pass

def inferieur(func, k): pass

print("Bienvenue dans le calculateur des lois de probabilités!")
print("-"*25)
print("Loi discrète: ")
print("1 - Loi Bernoulli")
print("2 - Loi Binomiale")
print("3 - Loi Géométrique")
print("4 - Loi Poisson")
print("Loi continue: ")
print("5 - Loi Uniforme")
print("6 - Loi Exponentielle")
print("7 - Loi Gamma")
print("8 - Loi Normale")
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

#Bloc pour la loi Géométrique
if choix == "3":
    valeur_p = float(input("Entrez la probabilité(p): "))
    valeur_k = int(input("Combien d'essai sont nécessaires afin d'obtenir un succès(k)? "))
    signe = input("X (<, >, <=, >=, =) k ? ")
    esperance = 1 / valeur_p
    variance = (1-p)/p**2
    print("-"*25)
    print("E[X] = ", esperance)
    print("Var[X] = ", variance)
    if signe == "=":
        f = lambda k : geometrique(valeur_p, valeur_k)  
        print(f"P[X{signe}{valeur_k}] = ", estEgal(f, valeur_k))
        
#Bloc pour la loi de Poisson

