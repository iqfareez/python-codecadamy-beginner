def calculateDiscount(price, discount):
    return price - (price * discount / 100)


item_price = 100
item_discount = 20
discounted_price = calculateDiscount(item_price, item_discount)

print(discounted_price)