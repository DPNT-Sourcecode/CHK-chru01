

# noinspection PyUnusedLocal
# skus = unicode string
from .constants import PRICES, OFFERS_MULTIPLE, OFFERS_GET_FREE, OFFERS_GROUP


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
    
    
    for offer in OFFERS_GROUP:
        temp_count = 0
        for product in offer:
            if product in basket:
                temp_count += basket[product]
        
        res += (temp_count // OFFERS_GROUP[offer][0]) * OFFERS_GROUP[offer][1]
        temp_count %= OFFERS_GROUP[offer][0]
        
        for product in offer:
            if product in basket:
                remain = min(temp_count, basket[product])
                temp_count -= remain
                basket[product] = remain

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
