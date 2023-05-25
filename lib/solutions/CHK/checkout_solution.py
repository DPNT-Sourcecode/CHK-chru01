

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

OFFERS_MULTIPLE = {
    "A": [(5, 200), (3, 130)], #
    "B": [(2, 45)],#
    "F": [(3, 20)],#
    "H": [(10, 80), (5, 45)],#
    "K": [(2, 150)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "U": [(4, 120)],
    "V": [(3, 130), (2, 90)],
}

OFFERS_GET_FREE = {
    "E": (2, "B"),#
    "N": (3, "M"),
    "R": (3, "Q"),
}


def checkout(skus):
    basket = {}
    
    for product in skus:
        if product not in PRICES:
            return -1

        if product in basket:
            basket[product] += 1
        else:
            basket[product] = 1
    
    res = 0
    
    for product in basket:
        if product in OFFERS_GET_FREE:
            temp_count = basket[product]
            temp_free_items = temp_count // OFFERS_GET_FREE[product][0]
            if OFFERS_GET_FREE[product][1] in basket:
                basket[OFFERS_GET_FREE[product][1]] -= min(basket[OFFERS_GET_FREE[product][1]], temp_free_items)         
            
    
    for product in basket:
            
        if product in OFFERS_MULTIPLE:
            temp_count = basket[product]
            for offer in OFFERS_MULTIPLE[product]:
                temp_offer_count = temp_count // offer[0]
                temp_count = temp_count % offer[0]
                res += temp_offer_count * offer[1]
            res += temp_count * PRICES[product]
        else:
            res += basket[product] * PRICES[product]
            
    return res

