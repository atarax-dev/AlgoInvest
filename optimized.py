actions_data = [(20, 5, 1), (30, 10, 2), (50, 15, 3), (70, 20, 4), (60, 17, 5), (80, 25, 6), (22, 7, 7), (26, 11, 8),
                (48, 13, 9), (34, 27, 10), (42, 17, 11), (110, 9, 12), (38, 23, 13), (14, 1, 14), (18, 3, 15),
                (8, 8, 16), (4, 12, 17), (10, 14, 18), (24, 21, 19), (114, 18, 20)]
wallet1 = 500
action_wallet1 = []


# tri par bénef/cout
def sort_by_efficiency(actions_list):
    # sorted_list = sorted(actions_list, key=lambda x: (x[1]/100)*x[0], reverse=True)
    sorted_list = sorted(actions_list, key=lambda x: x[1], reverse=True)
    return sorted_list


def get_best_invest(actions_list, wallet, action_wallet):
    for action in actions_list:
        if wallet > 0 and wallet > action[0]:
            action_wallet.append(action)
            wallet -= action[0]
    return action_wallet


def calcul_prix_combinaison(combinaison):
    total_price = 0
    for action in combinaison:
        price = action[0]
        total_price += price
    return total_price


def calcul_benefice_combinaison(combinaison):
    total_benefits = 0
    for action in combinaison:
        price = action[0]
        benefits_percent = action[1]
        benefit = price * benefits_percent / 100
        total_benefits += benefit
    return total_benefits


best_combo = get_best_invest(sort_by_efficiency(actions_data), wallet1, action_wallet1)
print(f"Meilleure combinaison : {[i[2] for i in best_combo]}")
print(f"Bénéfice : {calcul_benefice_combinaison(best_combo)} €")
print(f"Prix : {calcul_prix_combinaison(best_combo)} €")
