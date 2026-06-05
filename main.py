def calculate_total_payment(quantity, unit_price):
    base_price = quantity * unit_price
    if base_price > 100000:
        base_price = base_price - (base_price * 0.1)
    
    tax_amount = base_price * 0.11
    final_price = base_price + tax_amount
    print("Total:", final_price)
    return final_price

calculate_total_payment(2, 60000)