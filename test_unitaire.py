import codeSource

#Test unitaire pour la loi binomiale
assert codeSource.binomiale(10, 0.5, 6) == 0.2051, "Test unitaire '=' échoué(binomiale)"
assert codeSource.inferieur(codeSource.binomiale(10, 0.3, 4), 4) == 0.6496, "Test unitaire '<' échoué(binomiale)"
assert codeSource.inferieurOuEgal(codeSource.binomiale(10, 0.3, 4), 4) == 0.8497, "Test unitaire '<=' échoué(binomiale)"
assert codeSource.superieur(codeSource.binomiale(10, 0.3, 4), 4) == 0.1507, "Test unitaire '>' échoué(binomiale)"
assert codeSource.superieurOuEgal(codeSource.binomiale(10, 0.3, 4), 4) == 0.3504, "Test unitaire '>=' échoué(binomiale)"

#Test unitaire pour la loi géométrique
assert codeSource.geometrique(0.2, 2) == 0.16, "Test unitaire égalité/géométrique échoué"
assert codeSource.inferieur(codeSource.geometrique(0.2, 3), 3) == 0.36, "Test unitaire '<' échoué(géométrique)"
assert codeSource.inferieurOuEgal(codeSource.geometrique(0.2, 3), 3) == 0.488, "Test unitaire '<=' échoué(géométrique)"
assert codeSource.superieur(codeSource.geometrique(0.2, 3), 3) == 0.512, "Test unitaire '>' échoué(géométrique)"
assert codeSource.superieurOuEgal(codeSource.geometrique(0.2, 3), 3) == 0.64, "Test unitaire '>=' échoué(géométrique)"

#Test unitaiare pour la loi de poisson
assert codeSource.poisson(2, 2) == 0.2707, "Test unitaire égalité/poisson échoué"
assert codeSource.inferieur(codeSource.poisson(2, 2), 2) == 0.4060, "Test unitaire '<' échoué(géométrique)"
assert codeSource.inferieurOuEgal(codeSource.poisson(2, 2), 2) == 0.6767, "Test unitaire '<=' échoué(géométrique)"
assert codeSource.superieur(codeSource.poisson(2, 2), 2) == 0.3233, "Test unitaire '>' échoué(géométrique)"
assert codeSource.superieurOuEgal(codeSource.poisson(2, 2), 2) == 0.5940, "Test unitaire '>=' échoué(géométrique)"

#Test unitaire pour la loi exponentielle
assert codeSource.inferieur(codeSource.exponentielle(0.5, 4), 4) == 0.865, "Test unitaire '<' échoué(exponentielle)"
assert codeSource.inferieurOuEgal(codeSource.exponentielle(0.5), 4) == 0.865, "Test unitaire '<=' échoué(exponentielle)"
assert codeSource.superieur(codeSource.exponentielle(0.5), 4) == 0.135, "Test unitaire '>' échoué(exponentielle)"
assert codeSource.superieurOuEgal(codeSource.exponentielle(0.5, 4), 4) == 0.135, "Test unitaire '>=' échoué(exponentielle)"


#Test unitaire pour la loi gamma
assert codeSource.inferieur(codeSource.gamma(3, 2), 3) == 0.801, "Test unitaire '<' échoué(gamma)"
assert codeSource.inferieurOuEgal(codeSource.gamma(3, 2), 3) == 0.801, "Test unitaire '<=' échoué(gamma)"
assert codeSource.superieur(codeSource.gamma(3, 2), 3) == 0.199, "Test unitaire '>' échoué(gamma)"
assert codeSource.superieurOuEgal(codeSource.gamma(3, 2), 3) == 0.199, "Test unitaire '>=' échoué(gamma)"




