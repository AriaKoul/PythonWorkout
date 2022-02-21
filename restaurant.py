MENU = {'sandwich':10, 'tea':7, 'salad':9}

def restaurant():
    total = 0
    while True:
        order = input('What is your order?: ').strip()
        
        if not order:
            break
        if order in MENU:
            price = MENU[order]
            total += price
            print(f"A {order} costs {price}. Your total is now {total} dollars.")
        elif order not in MENU:
            print(f"Sorry! {order} is not in stock right now.")
        
    print(f'Your total is {total} dollars.')

restaurant()


