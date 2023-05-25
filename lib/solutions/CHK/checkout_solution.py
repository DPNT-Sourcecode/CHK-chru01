

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

OFFERS_MULTIPLE = {
    "A": (3, 130),
    "B": (2, 45),
}

OFFERS_GET_FREE = {
    "E": (2, "B"),
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
        if product in OFFERS:
            temp_count = basket[product]
            temp_regular_count = temp_count % OFFERS[product][0]
            temp_offer_count = temp_count // OFFERS[product][0]
            
            res += temp_regular_count * PRICES[product]
            res += temp_offer_count * OFFERS[product][1]
        else:
            res += basket[product] * PRICES[product]
            
    return res






