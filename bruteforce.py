# actions = (prix en euros, bénéfice en % après 2 ans)
actions_data = [(20, 5), (30, 10), (50, 15), (70, 20), (60, 17), (80, 25), (22, 7), (26, 11), (48, 13), (34, 27),
                (42, 17), (110, 9), (38, 23), (14, 1), (18, 3), (8, 8), (4, 12), (10, 14), (24, 21), (114, 18)]
wallet1 = 500
action_wallet1 = []


def get_max_benefits_action(actions_list):
    i = 0
    max_benefits = 0
    imax = 0
    for price, benefits in actions_list:
        if benefits > max_benefits:
            max_benefits = benefits
            imax = i
        i += 1
    return imax


def get_best_invest(actions, wallet, action_wallet):
    bonus = 0
    while wallet > 0 and len(actions) > 0:
        imax_benefits = get_max_benefits_action(actions)
        price = actions[imax_benefits][0]
        if wallet - price >= 0:
            wallet -= price
            bonus += price*(actions[imax_benefits][1]/100)
            actions.remove(actions[imax_benefits])
            action_wallet.append(imax_benefits + 1)
        elif wallet - price < 0 and len(actions) > 0:
            actions.remove(actions[imax_benefits])

    print(f"Argent restant: {wallet}€")
    print(f"Liste des actions: {action_wallet}")
    print(f"Gain: {bonus}")


get_best_invest(actions_data, wallet1, action_wallet1)
