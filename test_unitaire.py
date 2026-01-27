import codeSource

#Test unitaire pour la loi binomiale
assert codeSource.binomiale(10, 0.5, 6) == 0.2051, "Test unitaire '=' échoué(binomiale)"
assert codeSource.inferieur(codeSource.binomiale(10, 0.3, 4), 4) == 0.6496, "Test unitaire '<' échoué(binomiale)"
assert codeSource.inferieurOuEgal(codeSource.binomiale(10, 0.3, 4), 4) == 0.8497, "Test unitaire '<=' échoué(binomiale)"
assert codeSource.superieur(codeSource.binomiale(10, 0.3, 4), 4) == 0.1507, "Test unitaire '>' échoué(binomiale)"
assert codeSource.superieurOuEgal(codeSource.binomiale(10, 0.3, 4), 4) == 0.3504, "Test unitaire '>=' échoué(binomiale)"

#Test unitaire pour la loi géométrique
assert codeSource.geometrique(0.2, 2) == 0.16, "Test unitaire égalité/géométrique échoué"

#Test unitaiare pour la loi de poisson
assert codeSource.poisson(3, 2) == 0.2240, "Test unitaire égalité/poisson échoué"


assert codeSource.binomiale(10, 0.5, 5) == 0.2051, "Erreurrrrrrrrrrrrrrrr"


