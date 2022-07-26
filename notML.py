def get_price(max, screen_broken, burn_in, dent, scratch, battery, color):
    price = max
    if screen_broken == True:
        price -= 100000
    elif burn_in == True:
        price -= 50000
    
    if dent >= 3:
        price -= 30000
    elif scratch == True:
        price -= 10000
    
    if battery < 80:
        price -= 30000
    
    if color.lower() not in ["white", "black", "silver"]:
        price -= 50000

    return price

