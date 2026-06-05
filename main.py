TAX_RATE = 0.11
DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 100000

def calculate_total_payment(quantity, unit_price):
    base_price = quantity * unit_price
    if base_price > DISCOUNT_THRESHOLD:
        base_price = base_price - (base_price * DISCOUNT_RATE)
    
    tax_amount = base_price * TAX_RATE
    final_price = base_price + tax_amount
    print("Total:", final_price)
    return final_price

calculate_total_payment(2, 60000)