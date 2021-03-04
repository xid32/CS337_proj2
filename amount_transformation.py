from unidecode import unidecode
from fractions import Fraction
import copy
from get_ingredients import get_ingredients_withURL


def amount_transformation(recipe_link):
    ingradient_list = get_ingredients_withURL(recipe_link)
    ingradient_double = copy.deepcopy(ingradient_list)
    ingradient_half = copy.deepcopy(ingradient_list)

    for i in range(len(ingradient_list)):
        get_quantity = unidecode(ingradient_list[i]['quantity']).split()
        if len(get_quantity) == 1:
            quantity_num = float(Fraction(get_quantity[0]))
        else:
            quantity_num = float(Fraction(get_quantity[0]) + Fraction(get_quantity[1]))

        # double
        quantity_double = quantity_num * 2
        ingradient_double[i]['quantity'] = str(quantity_double)


        # half
        if len(ingradient_list[i]['measurement']) != 0:
            quantity_half = quantity_num / 2
        else:
            quantity_half = quantity_num // 2
        ingradient_half[i]['quantity'] = str(quantity_half)

    return ingradient_double, ingradient_half
