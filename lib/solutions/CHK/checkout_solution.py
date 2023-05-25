

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
    "I": 35,    |                        |
    "J": 60,    |                        |
    "K": 80,    | 2K for 150             |
    "L": 90,    |                        |
    "M": 15,    |                        |
    "N": 40,    | 3N get one M free      |
    "O": 10,    |                        |
    "P": 50,    | 5P for 200             |
    "Q": 30,    | 3Q for 80              |
    "R": 50,    | 3R get one Q free      |
    "S": 30,    |                        |
    "T": 20,    |                        |
    "U": 40,    | 3U get one U free      |
    "V": 50,    | 2V for 90, 3V for 130  |
    "W": 20,    |                        |
    "X": 90,    |                        |
    "Y": 10,    |                        |
    "Z": 50,    |                        |
    
}

OFFERS_MULTIPLE = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "F": [(3, 20)],
    "K": [(2, 50)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
}

OFFERS_GET_FREE = {
    "E": (2, "B"),
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


