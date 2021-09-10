import itertools

# actions = (prix en euros, bénéfice en % après 2 ans)
actions_data = [(20, 5), (30, 10), (50, 15), (70, 20), (60, 17), (80, 25), (22, 7), (26, 11), (48, 13), (34, 27),
                (42, 17), (110, 9), (38, 23), (14, 1), (18, 3), (8, 8), (4, 12), (10, 14), (24, 21), (114, 18)]

stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
combinaisons = []


def calcul_prix_combinaison(combinaison, actions_list):
    total_price = 0
    for action in combinaison:
        price = actions_list[action-1][0]
        total_price += price
    return total_price


def calcul_benefice_combinaison(combinaison, actions_list):
    total_benefits = 0
    for action in combinaison:
        price = actions_list[action - 1][0]
        benefits_percent = actions_list[action - 1][1]
        benefit = price*benefits_percent/100
        total_benefits += benefit
    return total_benefits


def calcul_meilleur_invest(combinaisons_list, actions_list):
    max_benefit_sub_500 = 0
    i = 0
    imax_benefit = 0
    for combinaison in combinaisons_list:
        if calcul_benefice_combinaison(combinaison, actions_list) > max_benefit_sub_500:
            max_benefit_sub_500 = calcul_benefice_combinaison(combinaison, actions_list)
            imax_benefit = i
        i += 1
    best_combinaison = combinaisons_list[imax_benefit]
    return best_combinaison


for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        if calcul_prix_combinaison(subset, actions_data) < 500:
            combinaisons.append(subset)

best_combo = (calcul_meilleur_invest(combinaisons, actions_data))
print(f"Meilleure combinaison : {best_combo}")
print(f"Bénéfice : {calcul_benefice_combinaison(best_combo, actions_data)} €")
print(f"Prix : {calcul_prix_combinaison(best_combo, actions_data)} €")
