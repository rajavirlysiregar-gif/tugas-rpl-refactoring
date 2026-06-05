TAX_RATE = 0.11
DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 100000

def apply_discount(price):
    if price > DISCOUNT_THRESHOLD:
        return price * (1 - DISCOUNT_RATE)
    return price

def apply_tax(price):
    return price * (1 + TAX_RATE)

def calculate_total_payment(quantity, unit_price):
    initial_price = quantity * unit_price
    discounted_price = apply_discount(initial_price)
    final_price = apply_tax(discounted_price)
    
    print("Total:", final_price)
    return final_price

calculate_total_payment(2, 60000)