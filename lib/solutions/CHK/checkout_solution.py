

# noinspection PyUnusedLocal
# skus = unicode string
PRODUCTS = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

OFFERS = {
    "A": (3, 130),
    "B": (2, 45),
}

def checkout(skus):
    basket = {}
    
    for product in skus:
        if product not in PRODUCTS:
            return -1

        if product in basket:
            basket[product] += 1
        else:
            basket[product] = 1
    
    res = 0
    
    for product in basket:
        if product in OFFERS:
            pass
        else:
            res += basket[product] * PRODUCTS[product]


