from pprint import pprint


with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    keys = ['ingredient_name', 'quantity', 'measure']
    read = file.read()
    read = read.split('\n\n')
    for dish in read:
        dish = dish.split('\n')
        cook_book[dish[0]] = [dict(zip(keys, dish.split(' | '))) for dish in dish[2:]]
# print(cook_book)


def get_shop_list_by_dishes(dishes, person_count=1):
    shop_list = {}

    for menu in dishes:
        try:
            for cook in cook_book[menu]:
                quantity = float(cook['quantity']) * person_count
                measure = cook['measure']

                if cook['ingredient_name'] in shop_list.keys():
                    quantity += shop_list[cook['ingredient_name']]['quantity']

                composition = {
                        'quantity': quantity,
                        'measure': measure
                    }

                shop_list[cook['ingredient_name']] = composition

        except KeyError:
            print(f"Error in entering: '{menu}'")

    return shop_list


shop = get_shop_list_by_dishes(['Запеченный картофель', 'Уха'], 3)
pprint(shop)
