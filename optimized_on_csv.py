import csv
from pprint import pprint


def clean_list(actions_list):
    cleaned_list = [x for x in actions_list if float(x[1]) > 0]
    return cleaned_list


def turn_csv_into_actions_list(csv_file):
    actions_list = []
    with open(csv_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            actions_list.append(row)
        actions_list.remove(actions_list[0])
    return actions_list


def sort_by_efficiency(actions_list):
    sorted_list = sorted(actions_list, key=lambda x: float(x[2]), reverse=True)
    return sorted_list


def get_sorted_actions_list(csv_file):
    dataset = turn_csv_into_actions_list(csv_file)
    cleaned_list = clean_list(dataset)
    sorted_list = sort_by_efficiency(cleaned_list)
    return sorted_list


# dataset1 = turn_csv_into_actions_list("dataset1.csv")
# dataset2 = turn_csv_into_actions_list("dataset2.csv")
# print(f"DATASET 1: {dataset1}")
# print(f"DATASET 2: {dataset2}")
# cleaned1 = clean_list(dataset1)
# cleaned2 = clean_list(dataset2)
# delta1 = ((len(dataset1))-(len(cleaned1)))
# delta2 = ((len(dataset2))-(len(cleaned2)))
# print(f"Elements supprimés DATASET 1: {delta1}")
# print(f"CLEAN DATASET 1: {cleaned1}")
# print(f"Elements supprimés DATASET 2: {delta2}")
# print(f"CLEAN DATASET 2: {cleaned2}")
# sorted_dataset1 = sort_by_efficiency(cleaned1)
# sorted_dataset2 = sort_by_efficiency(cleaned2)
# print(f"SORTED DATASET 1: {sorted_dataset1}")
# print(f"SORTED DATASET 2: {sorted_dataset2}")

dataset1 = get_sorted_actions_list("dataset1.csv")
dataset2 = get_sorted_actions_list("dataset2.csv")
action_wallet1 = []
action_wallet2 = []
wallet1 = 500
wallet2 = 500


def get_best_invest(actions_list, wallet, action_wallet):
    for action in actions_list:
        if wallet > 0 and wallet > float(action[1]):
            action_wallet.append(action)
            wallet -= float(action[1])
    return action_wallet


def calcul_prix_combinaison(combinaison):
    total_price = 0
    for action in combinaison:
        price = float(action[1])
        total_price += price
    return total_price


def calcul_benefice_combinaison(combinaison):
    total_benefits = 0
    for action in combinaison:
        price = float(action[1])
        benefits_percent = float(action[2])
        benefit = price * benefits_percent / 100
        total_benefits += benefit
    return total_benefits


actions_list1 = get_best_invest(dataset1, wallet1, action_wallet1)
actions_list2 = get_best_invest(dataset2, wallet2, action_wallet2)


def print_results(actions_list):
    print(f"Nombres d'actions achetées: {len(actions_list)}")
    print("Liste Nom / Prix / Bénéfice en %: ")
    pprint(actions_list)
    print(f"Prix: {calcul_prix_combinaison(actions_list)}")
    print(f"Bénéfice: {calcul_benefice_combinaison(actions_list)}")


print_results(actions_list1)
print()
print_results(actions_list2)



